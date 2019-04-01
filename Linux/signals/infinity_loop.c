/**
Напишите на языке С программу, в которой выполняется бесконечный цикл.
В процессе работы программа не должна ничего выводить в стандартные потоки.
При нажатии клавиш Ctrl+C программа должна завершаться и печатать число итераций, 
которые она успела выполнить, в формате Iterations: XXX.
Note
Разрешается использовать 64-битный счётчик итераций, 
«длинную арифметику» реализовывать не требуется.
Example
$ ./infinite-loop
^CIterations: 100500100500
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <stdint.h>


int64_t counter = 0;
volatile sig_atomic_t got_sigint;

void sigint_handler(int sig)
{
    got_sigint = 1;
}
 
int main(void)
{
    void sigint_handler(int sig); /* prototype */
    struct sigaction sa;
    sa.sa_handler = sigint_handler;
    sa.sa_flags = 0; // or SA_RESTART
    sigemptyset(&sa.sa_mask);
    
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        exit(1);
    }

    while (!got_sigint){
    	counter += 1;
	}

	printf("Iterations: %lld\n", counter);

	return 0;
}
