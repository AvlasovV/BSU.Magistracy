/**
Разработайте на языке C свою собственную версию утилиты cat.
Если программа запущена без параметров, то она должна просто копировать все данные с stdin на stdout без изменений. Если задан один или несколько аргументов, то все они трактуются как пути к файлам, данные из которых нужно прочитать и последовательно вывести на stdout.
В случае, если указан несуществующий файл или в процессе чтения файла возникла ошибка, выведите сообщение об ошибке на stderr (в произвольной форме) и продолжите обработку следующих аргументов. Если всё прошло успешно, код выхода должен быть равен нулю, иначе — единице.
Реализовывать опции для вывода справки (-h, –help) не нужно.
Example
$ ./cat <<<"I like cats"
I like cats
$ echo "meow" > f1.txt
$ echo "purr" > f3.txt
$ ./cat f{1..3}.txt
meow
cat: f2.txt: No such file or directory
purr
*/


#include <unistd.h> 
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h> 
#include <stdlib.h>
 
#define BUF_SIZE 512

char buf[BUF_SIZE];


int Run(char* arg) {
	
	int fd = open(arg, O_RDONLY); 
	
	if (fd == -1) 
	{
	    write(2, "Error, can't open\n", 18);
	    return 1;
	}
	
	size_t n;
        while(1) {
            n = read(fd, buf, BUF_SIZE);
            
            if (n < 0) {
            	close(fd);
                return 1;
            }

            if (n == 0) {
                break;
            }

            int code = write(STDOUT_FILENO, buf, n);

            if (code != n) {
            	close(fd);
                return 1;
            }
        }
    
    	close(fd);
    	return 0;
}
 
int main(int argc, char* args[]) {

    int exit_code = 0;
  
    if (argc > 1){
        for (int i = 1; i < argc; ++i){
            if(Run(args[i]) == 1){
            	exit_code = 1;
            }
        }
    }
    else{
        size_t n;
        
        while(1) {
            n = read(STDIN_FILENO, buf, BUF_SIZE);

            if (n < 0) {
                return 1;
            }

            if (n == 0) {
                break;
            }

            int code = write(STDOUT_FILENO, buf, n);

            if (code != n) {
                return 1;
            }
        }
    }
    return exit_code;
}