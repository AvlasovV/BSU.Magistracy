/**
С помощью библиотеки POSIX Threads реализуйте на C следующую демо-программу.
Три потока одновременно безостановочно пишут на стандартный вывод символы: первый поток — букву a, второй поток — букву b, третий — букву c.
Каждый поток должен вывести ровно 10 000 букв и завершиться, главный поток должен дождаться завершения рабочих потоков.
Сравните, отличается ли результат при использовании разных способов вывода:

    printf("x");
    write(STDOUT_FILENO, "x", 1). 

Отправьте в систему обе программы.
Example
$ ./a.out
aaaaaababababcabcabcabcabcabc...

*/
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <stdlib.h>
 
#define N 10000
int main(void)
{
    pid_t wpid;
    int status = 0;
    
    pid_t pid = fork();
    
    if (pid == 0){
        for(int i = 0; i < N; i++){write(STDOUT_FILENO, "a", 1); }
        
        return 0;             
    }        
    else{
        pid = fork();
        if (pid == 0){
            for(int i = 0; i < N; i++){write(STDOUT_FILENO, "b", 1); }   
            return 0;   
        }    
        else{
            pid = fork();
            if (pid == 0){
                for(int i = 0; i < N; i++){write(STDOUT_FILENO, "c", 1); }
                return 0;      
            }            
        }
    }
    
    while ((wpid = wait(&status)) > 0);
    return 0;        

}