library(data.table)
library(forecast)
library(ggplot2)
library(ggforce)
library(rpart)
library(lubridate)

filename = "/Volumes/data/projects/django-mms/data/demand_daily/luzon-hourly-demand.csv"

dt = fread(filename,sep=",")

head(dt)

n_date <- unique(dt[, TIME_INTERVAL])
length(n_date)

dt_train <- dt[TIME_INTERVAL %in% n_date[1:1000]]
dt_test <- dt[TIME_INTERVAL %in% n_date[1001:1201]]
head(dt_test)

plot(ts(dt_train$MKT_REQT, freq = 24))

data_ts <- ts(dt_train$MKT_REQT, freq = 24*7)

decomp_ts <- stl(data_ts, s.window = "periodic", robust = TRUE)$time.series
 

autoplot(stl(data_ts, s.window = "periodic", robust = TRUE))

fit = HoltWinters(data_ts, beta=FALSE, gamma=FALSE)


forecast(fit, 24)
plot(forecast(fit, 24))


# Automated forecasting using an ARIMA model
#fit <- auto.arima(data_ts)
#plot(forecast(fit, 5))


plot(forecast(fit, 24))

# remove last date
dt  <- dt[-nrow(dt),]

dt$TIME_INTERVAL  <-  ymd_hms(dt$TIME_INTERVAL)

dt$HOUR  <- hour(dt$TIME_INTERVAL) + 1

dt$WEEK_NUM  <-  as.numeric(strftime(as.Date(dt$TIME_INTERVAL, "%Y-%m-%d"), "%u"))

period  <- 24
N <- nrow(dt) # number of observations in the train set
window <- N / period # number of days in the train set
matrix_data <- data.table(Load = dt[, MKT_REQT],
                         Daily = rep(1:period, window),
                         Weekly = dt[, WEEK_NUM])



head(matrix_data)

n_date <- unique(dt[, TIME_INTERVAL])


data_train <- dt[TIME_INTERVAL %in% n_date[1:1176]]
data_test <- dt[TIME_INTERVAL %in% n_date[1177:1200]]

data_ts <- ts(data_train$MKT_REQT, freq = period * 7)
decomp_ts <- stl(data_ts, s.window = "periodic", robust = TRUE)$time.series
 
decomp_stl <- data.table(MKT_REQT = c(data_train$MKT_REQT, as.numeric(decomp_ts)),
                         TIME_INTERVAL = rep(data_train[,TIME_INTERVAL], ncol(decomp_ts)+1),
                         Type = factor(rep(c("original data", colnames(decomp_ts)),
                                       each = nrow(decomp_ts)),
                                       levels = c("original data", colnames(decomp_ts))))
 
ggplot(decomp_stl, aes(x = TIME_INTERVAL, y = MKT_REQT)) +
  geom_line() + 
  facet_grid(Type ~ ., scales = "free_y", switch = "y") +
  labs(x = "Date", y = NULL,
       title = "Time Series Decomposition by STL")

# multiseasonal object
data_msts <- msts(data_train$MKT_REQT, seasonal.periods = c(period, period*7))


# Fourier decomposition
K <- 2
fuur <- fourier(data_msts, K = c(K, K))

# 2 pairs of sine and cosine values for daily and weekly season
head(fuur)

trend_part <- ts(decomp_ts[,2])
trend_fit <- auto.arima(trend_part)
trend_for <- forecast(trend_fit, period)$mean

trend_data <- data.table(MKT_REQT = c(decomp_ts[,2], trend_for),
                         TIME_INTERVAL = c(data_train$TIME_INTERVAL, data_test$TIME_INTERVAL),
                         Type = c(rep("Real", nrow(data_train)), rep("Forecast",
                                                                     nrow(data_test))))
 
ggplot(trend_data, aes(TIME_INTERVAL, MKT_REQT, color = Type)) +
  geom_line(size = 1.2) +
  labs(title = paste(trend_fit))

N <- nrow(data_train)
window <- (N / period) - 1 # number of days in train set minus lag
 
new_MKT_REQT <- rowSums(decomp_ts[, c(1,3)]) # detrended load
lag_seas <- decomp_ts[1:(period*window), 1] # seasonal part of time series as lag feature
 
matrix_train <- data.table(MKT_REQT = tail(new_MKT_REQT, window*period),
                           fuur[(period + 1):N,],
                           Lag = lag_seas)

head(matrix_train)

# Accuracy MAPE - Mean Absolute Percentage Error
mape <- function(real, pred){
  return(100 * mean(abs((real - pred)/real)))
}


tree_1 <- rpart(MKT_REQT ~ ., data = matrix_train)


tree_1$variable.importance


paste("Number of splits: ", tree_1$cptable[dim(tree_1$cptable)[1], "nsplit"])


install.packages("rpart.plot")
library(rpart.plot)


rpart.plot(tree_1, digits = 2, 
           box.palette = viridis::viridis(10, option = "D", begin = 0.85, end = 0), 
           shadow.col = "grey65", col = "grey99")


datas <- data.table(MKT_REQT = c(matrix_train$MKT_REQT,
                             predict(tree_1)),
                    TIME_INTERVAL = rep(1:length(matrix_train$MKT_REQT), 2),
                    Type = rep(c("Real", "RPART"), each = length(matrix_train$MKT_REQT)))
 
ggplot(datas, aes(TIME_INTERVAL, MKT_REQT, color = Type)) +
  geom_line(size = 0.8, alpha = 0.75) +
  labs(y = "Detrended load", title = "Fitted values from RPART tree")

mape(matrix_train$MKT_REQT, predict(tree_1))


tree_2 <- rpart(MKT_REQT ~ ., data = matrix_train,
                control = rpart.control(minsplit = 2,
                                        maxdepth = 30,
                                        cp = 0.000001))

plot(tree_2, compress = TRUE)

tree_2$cptable[dim(tree_2$cptable)[1], "nsplit"] # Number of splits


datas <- data.table(MKT_REQT = c(matrix_train$MKT_REQT,
                             predict(tree_2)),
                    TIME_INTERVAL = rep(1:length(matrix_train$MKT_REQT), 2),
                    Type = rep(c("Real", "RPART"), each = length(matrix_train$MKT_REQT)))
 
ggplot(datas, aes(TIME_INTERVAL, MKT_REQT, color = Type)) +
  geom_line(size = 0.8, alpha = 0.75) +
  labs(y = "Detrended load", title = "Fitted values from RPART")

mape(matrix_train$MKT_REQT, predict(tree_2))

test_lag <- decomp_ts[((period*window)+1):N, 1]
fuur_test <- fourier(data_msts, K = c(K, K), h = period)
 
matrix_test <- data.table(fuur_test,
                          Lag = test_lag)

for_rpart <- predict(tree_2, matrix_test) + trend_for

data_for <- data.table(MKT_REQT = c(data_train$MKT_REQT, data_test$MKT_REQT, for_rpart),
                       TIME_INTERVAL = c(data_train$TIME_INTERVAL, rep(data_test$TIME_INTERVAL, 2)),
                       Type = c(rep("Train data", nrow(data_train)),
                                rep("Test data", nrow(data_test)),
                                rep("Forecast", nrow(data_test))))
 
ggplot(data_for, aes(TIME_INTERVAL, MKT_REQT, color = Type)) +
  geom_line(size = 0.8, alpha = 0.75) +
  facet_zoom(x = TIME_INTERVAL %in% data_test$TIME_INTERVAL, zoom.size = 1.2) +
  labs(title = "Forecast from RPART")


