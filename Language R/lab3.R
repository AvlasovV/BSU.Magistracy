rm(list = ls())


# Task 1

library(Matrix)
library(MASS)
library(matlib)

n <- 4 # 4 values in vector

# covariance matrix generation
eigen_mean <- 2
Q <- matrix(rnorm(n*n), nrow=n, ncol=n)
Q
covm <- t(Q) %*% Diagonal(x=abs(eigen_mean+rnorm(n))) %*% Q
covm

# mean vector generation
ev <- c(1:4) * 3
ev

# sample generation
dt <- mvrnorm(400,ev,covm)  # mvrnorm produces one or more samples from the specified multivariate normal distribution.
colnames(dt) <- sprintf("x%d",seq(1:n))
df <- data.frame(dt)
head(df)

# linear regression
fit <- lm(x1~., data=df) # Nice name - Fitting Linear Models can be used to carry out regression
fit

# coefficients
fit$coefficients

# residual variance
summary(fit)$sigma**2  # sigma - extract the estimated standard deviation of the errors
sd(fit$residuals)      # sd - standard deviation, computes the standard deviation of the values in x

# residuals normality
shapiro.test(fit$residuals)
plot(cut(fit$residuals, 16))


# true coefs
sigma22 <- matrix(covm[-1, -1], ncol=3, nrow=3)
sigma12 <- matrix(covm[1, 2:4], nrow=1, ncol=3)
mu2 <- matrix(ev[2:4], ncol=1, nrow=3)
c0 <- ev[1] - (sigma12 %*% inv(sigma22)) %*% mu2
c123 <- t(sigma12 %*% inv(sigma22))

c0
c123
fit$coefficients


# Task 2

df2 <- read.csv(file="D:\\!UNIVERSITY\\Мага.Материалы\\R\\Labs\\for lab3\\Lab3Task2Var1.csv", header=TRUE)
head(df2)

f <- function(x,a) {
  return (I(sin(a*x)))
}
opt_a <- optimize(function(a) summary(lm(y~f(x,a), data=df2))$sigma**2, c(1,5))$minimum
opt_a
fit2 <- lm(y~f(x,opt_a), data=df2)
plot(df2$x,df2$y)
lines(sort(df2$x),sort(fitted(fit2)))

a_cmp <- nlm(function(a) summary(lm(y~f(x,a), data=df2))$sigma**2, 1)$estimate
a_cmp
fit3 <- lm(y~f(x,a_cmp), data=df2)
plot(df2$x,df2$y)
lines(sort(df2$x),sort(fitted(fit3)))


# Task 3
df3 <- read.csv(file="D:\\!UNIVERSITY\\Мага.Материалы\\R\\Labs\\for lab3\\Lab3Task3Var1.csv", header=TRUE)
head(df3)

# divide into train and test sets
test_numbers <- sample(1:length(df3$y), size=10, replace=F)
test_numbers
test_df <- df3[df3$X %in% test_numbers,]
head(test_df)
train_df <- df3[!df3$X %in% test_numbers,]
head(train_df)

oldpar <- par(mex=0.5)
pairs(train_df, gap=0, cex.labels=0.9)
par(oldpar)
plot(train_df)

summary(lm(y~.-X, data=train_df))
step(lm(y~.-X, data=train_df))
lm1 <- lm(y~x.1+x.5+x.6+x.10, data=train_df)
summary(lm1)
step(lm1)
lm1$