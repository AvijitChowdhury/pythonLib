# -*- coding: utf-8 -*-
"""3.4. Seaborn Tutorial in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_unR_OcDLzO38kQBjoFJdviMSO8x-gQU

Seaborn:
- Data Visualization Library

Importing the Libraries
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""Note : Seaborn has some built-in datasets"""

# total bill vs tip dataset
# tips = sns.load_dataset('tips')
tips = sns.load_dataset('tips')

tips.head()

# setting a theme for the plots
sns.set_theme()

# visualize the data
# sns.relplot(data=tips, x ='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
# sns.relplot(data= tips, x = 'total_bill',y= 'tip',col= 'time', hue ='sex',style = 'sex' ,size='size')
sns.countplot(x="sex",data=tips)

# load the iris dataset
iris = sns.load_dataset('iris')

iris.head()

"""Scatter Plot"""

sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)

sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)

# loading the titanic dataset
titanic = sns.load_dataset('titanic')

titanic.head()

titanic.shape

"""Count Plot"""

sns.countplot(x='class',data=titanic)

sns.countplot(x='survived',data=titanic)

"""Bar Chart"""

sns.barplot(x='sex',y='survived',hue='class',data=titanic)

# house price dataset
from sklearn.datasets import load_boston
house_boston = load_boston()

house = pd.DataFrame(house_boston.data, columns=house_boston.feature_names)
house['PRICE'] = house_boston.target

print(house_boston)

house.head()

"""Distribution Plot"""

sns.distplot(house['PRICE'])

"""Correlation:
- Positive Correlation
- Negative Correlation

Heat Map
"""

correlation = house.corr()

# constructing a Heat Map
plt.figure(figsize=(10,10))
sns.heatmap(, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')
