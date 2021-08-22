library(data.table)
library(forecast)
library(ggplot2)

filename = "/Volumes/data/projects/django-mms/data/demand_daily/luzon-hourly-demand.csv"

dt = fread(filename,sep=",")

head(dt)

n_date <- unique(dt[, TIME_INTERVAL])
length(n_date)

dt_train <- dt[TIME_INTERVAL %in% n_date[1:1000]]
dt_test <- dt[TIME_INTERVAL %in% n_date[1001:1201]]
head(dt_test)

plot(ts(dt_train$MKT_REQT, freq = 24*365))

data_ts <- ts(dt_train$MKT_REQT, freq = 24*7)

decomp_ts <- stl(data_ts, s.window = "periodic", robust = TRUE)$time.series
 

autoplot(stl(data_ts, s.window = "periodic", robust = TRUE))


