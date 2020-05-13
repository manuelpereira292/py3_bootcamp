import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('sales.csv')

dataset['rate'].fillna('zero', inplace=True)
dataset['sales_in_first_month'].fillna(0, inplace=True)

def convert_to_int(word):
    word_dict ={'zero':0, 'one':1, 'two':2, 'three':3,
                'four': 4, 'five':5, 'six':6, 'seven': 7,
                'eight':8, 'nine':9}
    return word_dict[word]

X= dataset.iloc[:,:3]
X['rate']=X['rate'].apply(lambda a: convert_to_int(a))

Y= dataset.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, Y)

pickle.dump(regressor, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2,2,500]])) # 300
print(model.predict([[4,600,200]])) # 400
print(model.predict([[4,300,500]])) # 50