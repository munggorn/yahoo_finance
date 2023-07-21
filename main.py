import yfinance as yf
from datetime import datetime
import pandas as pd
import numpy as np
from test2 import SET50,WORLD

symbols =  WORLD #['SIRI.BK', 'AP.BK', 'SCB.BK']  # Replace 'SET' with the desired stock symbol
start_date = '2018-01-01'  # Define the start date of the historical data
end_date = datetime.today().strftime('%Y-%m-%d')  # Define the end date of the historical data
z_scores = pd.DataFrame()
delta_prices = pd.DataFrame()

# Fetch the historical data
for symbol in symbols:
    data_week = yf.download(symbol, start=start_date, interval='1wk')
    data_week_volume = data_week['Volume']
    data_week_open   = data_week['Open']
    data_week_close  = data_week['Close']
    # Calculate the Z-score of volume for the last 100 weeks
    window = 100
    m      = 1
    z_score = (data_week_volume - data_week_volume.rolling(window).mean()) / data_week_volume.rolling(window).std()
    z_score = z_score.rolling(m).mean()
    z_scores[symbol] = z_score
    
    delta_price = data_week_close - data_week_open
    delta_prices[symbol] = delta_price
#print(delta_prices)


# Get the Z-scores for the last 100 weeks
n = 3
last_100_weeks_z_scores = z_scores.tail(n)
last_100_weeks_delta_prices = delta_prices.tail(n)
# Select positive Z-scores and closing price > opening price
filtered_volume = last_100_weeks_z_scores[last_100_weeks_z_scores >= 0]

filtered_bull = filtered_volume.where(last_100_weeks_delta_prices > 0, np.nan)[symbols]

# Drop rows containing NaN values
filtered_bull = filtered_bull #.dropna(how='all', axis=0)

# Print the filtered data

#print(filtered_bull)


