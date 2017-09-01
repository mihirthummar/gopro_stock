#!/usr/bin/env python3
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
##################################################################################
def moving_avg_100():
	style.use('ggplot')
	df = pd.read_csv('gopro.csv',index_col = 0) #read from csv file

	#moving average for previous 100 days
	df['100 Moving Avg'] = df['High'].rolling(window=100).mean()
	print(df)
	df.dropna(inplace = True)
	df.to_csv('gopro.csv')

##################################################################################
# print the most recent day's open, high, low, close, volume
start = dt.datetime(2000, 1, 1)
df = web.DataReader("NASDAQ:GPRO", 'google', start)# read the live stock charts from google
def today_prices():
	print('Open: $'+str(df['Open'][-1]),'  ',\
		'High: $' +str(df['High'][-1]),'  ',\
		'Low: $'+str(df['Low'][-1]),'  ',\
		'Close: $'+str(df['Close'][-1]),'  ',\
		'Volume: '+str(df['Volume'][-1]))
	df['High'].plot()#plot the high and the low over the last 17 years
	df['Low'].plot()
	plt.legend()
	plt.title("GOPRO STOCK")
	plt.show()
##################################################################################


def linear_regression():
#Machine learning using linear regression to predict the high prices of the stock market
	start = dt.datetime(2000, 1, 1)
	df2 = web.DataReader("NASDAQ:GPRO", 'google', start)# read the live stock charts from google
	length_of_half_data = len(df2)//2 # length of half of training data

	time_train = []#x train using days
	for time in range(0,length_of_half_data):
		time_train.append([time])
	high_train = []
	for high in df['High'][0:length_of_half_data]:
		high_train.append([high]) #y train using high prices

	time_test = []
	for time in range(length_of_half_data, len(df)):
		time_test.append([time]) #x test using days
	high_test = []
	for high in df['High'][length_of_half_data:]:
		high_test.append([high]) #y test using high prices

	#length tests
	print(len(time_train))
	print(len(high_train))
	print(len(time_test))
	print(len(high_test))
	print(len(df))
	# Create linear regression object
	regr = linear_model.LinearRegression()

	#Train the model using the training sets

	regr.fit(time_train, high_train)

	# Make predictions using the testing set
	high_predictions = regr.predict(time_test)

	# The coefficients
	print('Coefficients: \n', regr.coef_)
	# The mean squared error
	print("Mean squared error: %.2f" % mean_squared_error(high_test, high_predictions))
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.2f' % r2_score(high_test, high_predictions))

	print(regr.predict(100))
	# Plot outputs
	plt.scatter(time_test, high_test,  color='black')
	plt.plot(time_test, high_predictions, color='blue', linewidth=3)

	plt.xticks(())
	plt.yticks(())

	plt.show()










