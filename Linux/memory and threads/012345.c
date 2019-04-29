/**
Вам даётся некорректный код на C. При помощи примитивов синхронизации организуйте попеременную работу двух потоков так, чтобы в результате получилась последовательность 0, 1, 2, 3, 4, 5, ...
Для простоты в этом задании можно не реализовывать корректную обработку кодов ошибок при вызове pthread-функций. Ошибки, например, при взятии лока на мьютексе обычно говорят о том, что в системе что-то серьёзно пошло не так, и едва ли не лучшим решением будет вызвать abort().

        if (*counter >= MAX){
            pthread_mutex_unlock(&mutex);
            pthread_cond_signal(&condition);
            pthread_exit(0);
            return 0;
            //break;
        }



*/
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
//#include <unistd.h>

#define MAX 999

pthread_mutex_t mutex;
pthread_cond_t condition;

struct TContext {
    const char* Name;
    int* Counter;
    int Mod;
};

void* ThreadFunc(void* arg) {
    struct TContext* ctxt = arg;
    int* counter = ctxt->Counter;
    //fprintf(stderr, "This is %s thread\n", ctxt->Name);
    while (1) {
        pthread_mutex_lock(&mutex);
        
        if (*counter % 2 != ctxt->Mod){
            pthread_cond_wait(&condition, &mutex);
        }
        
        if (*counter % 2 == ctxt->Mod) {
            printf("%d ", (*counter)++);
            pthread_cond_signal(&condition);
        }
        
        if (*counter >= MAX){
            pthread_mutex_unlock(&mutex);
            pthread_cond_signal(&condition);
            pthread_exit(0);
            return 0;
            //break;
        }
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(0);
}

int main()
{
    pthread_t t1;
    pthread_t t2;

    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&condition, NULL);    

    int counter = 0;
    struct TContext ctxt1 = {"even", &counter, 0};
    struct TContext ctxt2 = {"odd", &counter, 1};
    pthread_create(&t1, 0, ThreadFunc, &ctxt1);
    pthread_create(&t2, 0, ThreadFunc, &ctxt2);

    pthread_join(t1, 0);
    pthread_join(t2, 0);
    printf("\n");
    pthread_mutex_destroy(&mutex); 
    return 0;
}
