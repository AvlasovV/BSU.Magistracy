/**
Нужно написать программку на C, которая будет выделять 10 ТБ виртуальной памяти. Напоминаем, что в одном тебибайте содержится 2^40 байт.
Проверка будет осуществляться на ОС Linux x64. Программа должна выделить память и ожидать ввода от пользователя, чтобы в этот момент можно было проверить объём памяти VIRT при помощи htop или другого инструмента. После нажатия клавиши ввода память должна корректно освобождаться, а процесс должен завершаться.
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <stdint.h>

#define SIZE (2UL << 40)

int main() {
    //int64_t n = 2 << 40; // 1 TB
    //long long n = 2 << 40;
    unsigned int n = 1024 * 1024 * 1024;   
    //size_t pagesize = getpagesize();    
    
    
    //void* addr = mmap(NULL, (uint64_t)n * 1024 * 10LL, PROT_READ | PROT_WRITE,
    void* addr = mmap(NULL, SIZE * 10, PROT_READ | PROT_WRITE,      
                MAP_ANONYMOUS | MAP_PRIVATE | MAP_NORESERVE, -1, 0);
 
    if (addr == MAP_FAILED) {
        perror("mmap()");
        return 1;
    }
 
    //sleep(60);   
    int a; 
    getchar();    

//    if (munmap(addr, (uint64_t)n * 1024 * 10LL) == -1) {
    if (munmap(addr, SIZE * 10) == -1) {     
        perror("munmap()");
        return 1;
    };
 
    return 0;
}