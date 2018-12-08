# 1.	Вернуть вектор всех чисел Мерсена от 1 до заданного числа. 
# Числом Мерсена называется простое число n, которое представимо в виде, 
# где р – также простое число. 
# При решении задачи использовать функцию для определения простоты числа.

is.prime <- function(n) n == 2L || all(n %% 2L:ceiling(sqrt(n)) != 0) 
is.prime(1) 
is.prime(2) 
is.prime(3) 
is.prime(5) 
is.prime(63) 
is.mersen.and.prime <- function(n){ 
  two.per.degree <- 2 
  x <- c(1) 
  while (two.per.degree < n){ 
    two.per.degree <- two.per.degree * 2 
    if (is.prime(two.per.degree - 1)){ 
      x <- c(x, two.per.degree - 1) 
    } 
  } 
  x
} 
is.mersen.and.prime(1000000)
#

library(Rcpp)
sourceCpp("D:\\!UNIVERSITY\\BSU.Magistracy\\Language R\\CPlusPlusForR\\CforR.cpp")

tictoc::tic()
is.mersen.and.prime(1000000000000)
tictoc::toc()

tictoc::tic()
mersen_seq(1000000000000)
tictoc::toc()