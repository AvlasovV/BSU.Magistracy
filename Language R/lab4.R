library(moments)

x <- runif(200, min = -2, max = 3)
head(x, 10)
tail(x, 20)
min(x)
max(x)
mean(x)
var(x)
median(x)

# коэф.эксцесса
kurtosis(x)
# коэф.асимметрии
skewness(x)

quantile(x, probs = c(0.25, 0.75, 0.95))
