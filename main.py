import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd
from sklearn.linear_model import LinearRegression
tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM', '^GSPC']
start = dt.datetime(2016, 12, 1)
end = dt.datetime(2022, 10, 19)
data = pdr.get_data_yahoo(tickers, start, end, interval="m")
data = data['Adj Close']
log_returns = np.log(data/data.shift())

# calculating Beta
cov = log_returns.cov()
var = log_returns['^GSPC'].var()
beta = cov.loc['AAPL', '^GSPC']/var


print(beta)
