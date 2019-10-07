#!/usr/bin/env python
# coding: utf-8

# # Market Basket Analysis
# ## Using FP-growth algorithm with mlxtend Python library

import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


#save timestamp to check script's running time
startTime = datetime.now()


# ### Load and clean transactions data to be used in the analysis


#read transactions data from csv file
df = pd.read_excel(r'C:\Downloads\Online_Retail.xlsx')


#plot 10 most frequent products in dataset
sns.countplot(x = 'Description', data = df, order = df['Description'].value_counts().iloc[:10].index)
plt.xticks(rotation=-90)


#clean the product names
df['Description'] = df['Description'].str.strip()
df['InvoiceNo'] = df['InvoiceNo'].astype('str')


# ### Create basket datafarme from transactions data with each row representing one basket

#create basket dataframe
basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')
basket.head()


#one hot encode the basket
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.head()


# ### Run FP-growth algorithm on frequent item sets (items that frequently appear in the same basket)


#create minTransactions variable to represent the minimum number of baskets for support parameter
minTransaction = 300
totalTransactions = len(basket_sets.index)
min_support_calc = minTransaction/totalTransactions

print('number of baskets for analysis is', totalTransactions)
print('minimum support value is', round(min_support_calc*100, 4), '%')


#create frequent items sets with clculated minimum support
frequent_itemsets = fpgrowth(basket_sets, min_support=min_support_calc, use_colnames=True)
frequent_itemsets.describe()


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.sort_values('confidence', ascending = False, inplace = True)
rules.head(10)


# ### Save results to csv file based on desired association parameters


rules[(rules['lift'] >= 1.4) & (rules['confidence'] >= 0.3)].sort_values(by=['confidence', 'lift'], ascending=False).to_excel(r'C:\Downloads\Online_Retail_Results_FPGrowth.xlsx', index=False)


print('It took ', datetime.now() - startTime, ' to run')

