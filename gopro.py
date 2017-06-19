import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
#style.use('fivethirtyeight')

start = dt.datetime(2017, 1, 1)
end = dt.datetime(2017, 12, 31)

df = web.DataReader("NASDAQ:GPRO", 'google', start, end)
print(df)

print('Open: $'+str(df['Open'][-1]),'  ',\
	'High: $' +str(df['High'][-1]),'  ',\
	'Low: $'+str(df['Low'][-1]),'  ',\
	'Close: $'+str(df['Close'][-1]),'  ',\
	'Volume: '+str(df['Volume'][-1]))
# df['High'].plot()
# df['Low'].plot()
# plt.legend()
# plt.title("GOPRO STOCK")
# plt.show()