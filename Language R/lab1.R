# 1 Авласов Владислав

len <- nchar('Авласов')
num <- 1

# Арифметическая
v1 <- (seq(from = num, to = 6.5, length.out = len))
v1

# Геометрическая
len <- nchar('Владислав')
start <- (13 - num)+2
step <- (100 / start) ** (1/(len - 1))
v2 <- start * step ^ (1 : len-1)
v2

# Рандомный вектор 3
big_v <- c(v1,v2)
big_v
v3 <- sample(big_v, 3)
v3

# Алфавит
alph <- "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
len <-nchar(alph)
s <-"эюяя"
sub_len <- nchar(s)
sum = 0
alph_v<-unlist(strsplit(alph, ""))
s_v<-unlist(strsplit(s, ""))

positions <- match(s_v, alph_v)
positions
sum(positions)

# Матрица
v3[1]
if(v3[1] <= 10){
  matr <- matrix(v1, nrow = 13, ncol = 13)
} else{
  matr <- matrix(v1, nrow = 13, ncol = 13, byrow = T)
}
extent_month <- c(month.name, month.name)
rownames(matr, do.NULL = FALSE)
rownames(matr) <- extent_month[1:13]
colnames(matr) <- extent_month[1:13]

strsplit(rownames(matr), "")[[2]][1]
unlist(strsplit(rownames(matr), ""))

x <- (1:13)
unlist(strsplit(rownames(matr), "")[2])[1]

english <- c("A", "B", "B", "D", "E", "F")
vec <- c()
for (i in (1:13)) {
      if(unlist(strsplit(rownames(matr), "")[i])[1] %in% english){
        vec <- c(vec, i)
      }
}
m1 <- matr[-vec, -vec]
determinant <- det(m1)
determinant
m_vects <- eigen(m1)
m_vects

diag_vector <- diag(m1)
m1_pow2 <- m1 %*% m1
m1_pow2

m2 <- apply(m1, c(1,2), function(x) x^2)
m2

# Таблица
i <- seq(1,10,3)
n <- c("Igor", "Ivan", "Sam", "Jack")
c <- c(T, F, T, F)
d <- data.frame(ind = i, name = n, cond = c, stringsAsFactors = F)
d.f <- factor(c)

subset(d, d$ind > 4 & d.f == FALSE, select = name)


# Выражение
n <- 3
x1 <- sample(1:20, n, replace=TRUE)
x2 <- sample(1:20, n, replace=TRUE)
x3 <- sample(1:20, n, replace=TRUE)

t1 <- data.frame(x1 = x1, x2 = x2, x3 = x3)

x <- (1:n)
sum1 <- sum(x * (t1[[1]][x] ^ 2) * (t1[[2]][(x / n) + 1] ^ 4) + (t1[[3]][((x+1) / n) + 1] ^ 3) )

sum2 <- 0
for (x in (1:n)) {
  sum2 <- sum2 + x * (t1[[1]][x] ^ 2) * (t1[[2]][(x / n) + 1] ^ 4) + (t1[[3]][((x+1) / n) + 1] ^ 3)
}

sum1
sum2
print("Does Sum1 == Sum2?")
sum1 == sum2
