import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Create lists
years = []
yearly_income = []
yearly_expenses = []
yearly_investments = []
annual_returns = []

#Yearly income
income = 35000
#Yearly expense
expense = income/2
#Expected interest rate per year
interest_rate = 0.08
#Investing half of the income
investment = income/2
#Calculating annual return
annual_return = investment * interest_rate
#Current year
year = 2021

#Append the first values to the list
years.append(year)
yearly_income.append(income)
yearly_expenses.append(expense)
yearly_investments.append(investment)
annual_returns.append(annual_return)

#Loop for n years
invested_years = 10
for i in range(0, invested_years-1):
  #Update the investment
  investment = investment + annual_return + income/2
  annual_return = investment * interest_rate
  ano = year + i + 1
  years.append(ano)
  yearly_income.append(income)
  yearly_expenses.append(expense)
  yearly_investments.append(investment)
  annual_returns.append(annual_return)
  
  #Create a DataFrame
df = pd.DataFrame()
df['Year'] = years
df['Yearly_income'] = yearly_income
df['Yearly_Expenses'] = yearly_expenses
df['Yearly_Investments'] = yearly_investments
df['Annual_Returns'] = annual_returns

#Visually show the data
plt.figure(figsize=(12.2, 4.5))
plt.plot(df['Year'], df['Yearly_Expenses'], label='Yearly_Expenses')
plt.plot(df['Year'], df['Annual_Returns'], label='Annual_Returns')
plt.xticks(rotation = 45)
plt.title('Retire in 10 years')
plt.xlabel('Years')
plt.ylabel('$')
plt.xticks(df['Year'])
plt.legend()
plt.show()

#Show the year/row where you can live off of returns
df[df.Yearly_Expenses <= df.Annual_Returns].head(1)
