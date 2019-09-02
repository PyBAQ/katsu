# -*- coding: utf-8 -*-
"""random-winner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/119HtcYscAQL6l0IJWEw2QkWiTMuAI_cf

# Random Winner Generator
"""

# Import Pandas
import pandas as pd
import random as rd
import datetime as dt

# Load files
print('*** Random Winner Generator ***')
Attendees=pd.read_csv('Attendees.csv')
Prizes=pd.read_csv('Prizes.csv')

# Show how many total attendees and how many total prizes
len_attendees = len(Attendees)
print('Total number of attendees =',len_attendees)
prizes_sum = Prizes.iloc[:,1].sum()
print('Total number of prizes =',prizes_sum)
len_prizes =len(Prizes)

# Picking up the winners id
print('Picking up the winners...')
population = range(len(Attendees))
winner = rd.sample(population, k=prizes_sum)

# Finding out the winners names
print('Locating the names...')
Winners = Attendees.loc[winner]

# Assigning each prize to each winner
print('Assigning the prizes...')
z = 0
Prizes_List = []
for x in range(len_prizes):
  for y in range(Prizes.iat[x,1]):
    Prizes_List.append(Prizes.iat[x,0])
    z = z +1

# Adding the column Prizes to the winners list
print('Creating the list...')
Winners['Prizes'] = Prizes_List

print('And the winners are:')
print(Winners)

# Writing the winners name and prizes to csv file
today=dt.date.today().strftime('%Y-%m-%d')
today=today.strip()
print('Winners writed to Winners_'+today+'.csv')
Winners.to_csv('Winners_'+today+'.csv')