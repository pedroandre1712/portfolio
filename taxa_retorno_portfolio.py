import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['CSNA3.SA', 'VALE3.SA']
my_data = pd.DataFrame()
for t in tickers:
  my_data[t] = wb.DataReader(t, data_source='yahoo', start='2019-07-25')['Adj Close']

my_data.info()
(my_data/my_data.iloc[0]*100).plot(figsize=(15, 6))
returns = (my_data/my_data.shift(1)) -1
returns.head()
weights = np.array([0.5, 0.5])
np.dot(returns, weights)
annual_returns = returns.mean()*250
annual_returns
np.dot(annual_returns, weights)

pfolio_1 = str(round(np.dot(annual_returns, weights), 5)*100)+' %'
print(pfolio_1)

weights_2 = np.array([0.7, 0.3])

pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5)*100)+ ' %'
print(pfolio_1)
print(pfolio_2)

#Deixar visualmente mais agradavel e organizar o codigo
#Calcular o melhor peso de cada acao para criacao do portfolio
