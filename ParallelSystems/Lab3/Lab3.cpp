/**
Реализовать параллельный алгоритм решения задачи, последовательный код которой имеет вид:
	  int a[N1][N2];
	  for (i = 1;i<N1; i++)
		  for (j = 0;j<N2; j++)
			   a[i][j] = a[i-1][j]+1;

В рамках этого кода происходит последовательная инициализация элементов двумерного массива: 
элементы i-строки инициализируются соответствующими (стоящими в том же столбце) элементами (i-1)-строки, увеличенными на единицу.
С параллельной точки зрения, двумерный массив нарезается на ленты строк по количеству процессов. 
Каждая лента содержит N1/P строк. Ленты распределяются между процессами: расчет строк i-ленты осуществляется на i-процессе. 
Значения первой строки ленты на процессе зависят от значений последней строки ленты соседнего процесса с меньшим номером. 
Данные зависимости порождают необходимость в обмене данными между процессами.

С целью оптимизации коммуникаций ленты строк нарезаются по столбцам на блоки. Всего N2/r блоков, где r – размер блока. 
В рамках параллельного алгоритма, каждый MPI-процесс последовательно блок за блоком инициализирует их элементы. 
Расчет блоков перемежается операциями обмена данными. Перед расчетом элементов i-блока процесс должен получить элементы последней строки 
i-блока от соседнего процесса с меньшим номером, затем с помощью полученных значений выполнить инициализацию элементов своего i-блока и, после этого,
передать последнюю строку этого блока соседнему процессу с большим номером.

Важно!

Вычислительная нагрузка в данном алгоритма на самом деле не принципиальна и выбрана просто для конкретики. 
Главное в этом задании -  оптимальная организация обменов данными. 
В идеале, все коммуникации необходимо спрятать под вычисления (overlapping communication and computation).
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mpi.h>
#include <iostream>

using namespace std;

int* init_block(int* matrix, int block_start, int str_in_block, int col_in_block, int str_len) {
	for (int i = 1; i < str_in_block; ++i) {
		for (int j = block_start; j < block_start + col_in_block; j++) {
			matrix[i * str_len + j] = matrix[(i - 1) * str_len + j] + 1;
		}
	}
	return matrix;
}

void print_matrix(int* matrix, int N_1, int N_2) {
	for (int i = 0; i < N_1; ++i) {
		for (int j = 0; j < N_2; ++j) {
			printf("%d ", matrix[i * N_2 + j]);
		}
		printf("\n");
	}
}

int main(int argz, char **argv) {
	int myrank = 0;
	int p = 0;
	if (sizeof(argv) / sizeof(char) <= 3) {
		printf("We have a problem: no enought argv.\n");
		return 0;
	}
	MPI_Status status;
	MPI_Init(&argz, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &p);
	MPI_Comm_rank(MPI_COMM_WORLD, &myrank);

	if (p == 1) {
		MPI_Finalize();
		return 0;
	}

	int n = atoi(argv[1]);
	int m = atoi(argv[2]);
	int r = atoi(argv[3]);
	if (n <= 0 || m <= 0 || r <= 0) {
		printf("We have a problem with argv.\n");
		MPI_Finalize();
		return 0;

	}
	int str_in_block = n / p;
	int block_in_row = m / r;


	if (myrank == p - 1) {
		str_in_block += (n % p);
	}

	int init_value = 0;

	MPI_Request request;
	int* matrix = new int[(str_in_block + 1) * m];
	int len = r;

	if (myrank == 0) {
		matrix = new int[str_in_block * m];
		for (int j = 0; j < block_in_row; ++j) {
			int current_block_num = j;
			if (j == block_in_row - 1) {
				len += m % r;
			}

			for (int k = 0; k < len; ++k) {
				//matrix[j * r + k] = j * r + k;
				matrix[j * r + k] = j;
			}
			for (int l = 1; l < str_in_block; ++l) {
				for (int k = 0; k < len; ++k) {
					matrix[l * m + j * r + k] = matrix[(l - 1) * m + j * r + k] + 1;
				}
			}
			int* help = new int[len];
			for (int k = 0; k < len; ++k) {
				help[k] = matrix[(str_in_block - 1) * m + current_block_num * r + k];
			}
			if (j) {
				MPI_Wait(&request, &status);
			}
			MPI_Isend(help, len, MPI_INT, myrank + 1, current_block_num, MPI_COMM_WORLD, &request);
		}
		int* result_matrix = new int[n * m];
		for (int i = 0; i < n * m; ++i) {
			result_matrix[i] = 0;
		}

		cout << "All blocks from main process are sent." << endl;
		
		int element_count;
		for (int i = 0; i < str_in_block * m; ++i) {
			result_matrix[i] = matrix[i];
		}
		for (int i = 1; i < p; ++i) {
			MPI_Probe(MPI_ANY_SOURCE, 666, MPI_COMM_WORLD, &status);
			element_count = 0;
			MPI_Get_count(&status, MPI_INT, &element_count);
			MPI_Recv(&result_matrix[status.MPI_SOURCE * str_in_block * m], element_count, MPI_INT, status.MPI_SOURCE, status.MPI_TAG, MPI_COMM_WORLD, &status);
		}
		cout << "End..." << endl;
		print_matrix(result_matrix, n, m);
	}
	else {
		if (block_in_row == 1) {
			len += m % r;
		}
		MPI_Irecv(matrix, len, MPI_INT, myrank - 1, 0, MPI_COMM_WORLD, &request);

		MPI_Request new_request, next_request;

		for (int j = 0; j < block_in_row; ++j) {
			if (j != block_in_row - 1) {
				int len_new = r;
				if (j + 1 == block_in_row - 1) {
					len_new += m % r;
				}
				MPI_Irecv(&matrix[(j + 1) * r], len_new, MPI_INT, myrank - 1, j + 1, MPI_COMM_WORLD, &new_request);
			}

			MPI_Wait(&request, &status);
			int element_count = 0;
			MPI_Get_count(&status, MPI_INT, &element_count);
			matrix = init_block(matrix, j * r, str_in_block + 1, element_count, m);
			if (myrank != p - 1) {
				MPI_Wait(&request, &status);
				MPI_Isend(&matrix[str_in_block * m + j * r], element_count, MPI_INT, myrank + 1, j, MPI_COMM_WORLD, &next_request);
			}
			if (j != block_in_row - 1) {
				request = new_request;
			}

		}
		MPI_Send(&matrix[m], str_in_block * m, MPI_INT, 0, 666, MPI_COMM_WORLD);
		cout << "Sent from process " << myrank << endl;
	}
	MPI_Finalize();
}