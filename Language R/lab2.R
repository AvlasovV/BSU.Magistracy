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
  print(x) 
  while (two.per.degree < n){ 
    two.per.degree <- two.per.degree * 2 
    print(two.per.degree) 
    print(is.prime(two.per.degree - 1)) 
    if (is.prime(two.per.degree - 1)){ 
      x <- c(x, two.per.degree - 1) 
      print(x) 
    } 
  } 
  x 
} 
is.mersen.and.prime(1000000)
#