/** 
Напишите на языке C программу, которая иллюстрирует создание нового процесса в UNIX-системе.

Родительский процесс выводит на экран свой PID.
Родительский процесс создаёт дочерний процесс с помощью системного вызова fork.
Родительский процесс выводит на экран PID нового процесса.
Родительский процесс входит в режим ожидания завершения дочернего процесса.
Дочерний процесс выводит на экран свой PID.
Дочерний процесс спит в течение одной секунды.
Дочерний процесс завершается с кодом 42.
Родительский процесс получает код выхода дочернего процесса и выводит его на экран. 

При этом на стандартный вывод должны выводиться сообщения в таком формате (порядок вывода некоторых строк может быть случайным):
[parent] My PID is 1000
[parent] Child's PID is 1001
[child] Hello, my PID is 1001
[child] Bye
[parent] Child exited with code 42
*/
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
 
int main() {
    pid_t parent_pid = getpid();
    printf("[parent] My PID is %d\n", parent_pid);
    
    pid_t child_pid;
    child_pid = fork();
    if (child_pid > 0) {
    	printf("[parent] Child's PID is %d\n", child_pid);
    	int status;
        waitpid(child_pid, &status, 0);
       	printf("[parent] Child exited with code %d\n", WEXITSTATUS(status));
     }
    else {
    	child_pid = getpid();
    	printf("[child] Hello, my PID is %d\n", child_pid);
        sleep(1);
        printf("[child] Bye\n");
        exit(42);
    }

    //printf("[parent] Finish this\n");

    return 0;
}