#!/usr/bin/env python3

import pandas as pd
import sklearn
import torch
import numpy as np
import math

from sklearn.model_selection import train_test_split

from dataAnalysis import graphPositiveNegative
from dataAnalysis import graphTweetsPerDay
from dataAnalysis import graphTweetsPerHour
from dataAnalysis import printInfo
from dataAnalysis import graphTweetsPerUser
from dataAnalysis import printMostUsedWords
from dataAnalysis import findTweetsWithSpecificWord

from models import vectorizeWords


data = pd.read_csv('sentimentDataset/training.1600000.processed.noemoticon.csv',                encoding='latin1', names=['target', 'id', 'date', 'flag', 'user', 'text'])

#modify data
# rename columns from 0/4 to negative/positive
data['target'] = data['target'].map({0: 'negative', 2:'neutral', 4: 'positive'})
# drop flag column
data = data.drop('flag', axis=1)


print("general info of data")
printInfo(data)

# check for duplicates
dups = data.duplicated().any()
print("are there duplicates: ", dups)


print(data.head())


print("graph the data")
# time related
# histogram how many tweets per day, percentage positive/negative
# print(data['text'].iloc[0])
# graphTweetsPerDay(data)
# histogram how many tweets per hour in 24 hour cycle, percentage positive/negative
# graphTweetsPerHour(data)

# how many different users, distribution of users and the amount of tweets (people who tweet more are more negative?)
# graphTweetsPerUser(data)

# graphPositiveNegative(data) # ratio negative / positive / neutral tweets


# find the most commonly used words and find if they are negative or positive
print("find if words are negative or positives")
# printMostUsedWords(data)
# findTweetsWithSpecificWord(data, "i")


print("models")
# vectorize the words using bag of words (BoW) method
X, y = vectorizeWords(data)
# split data in to test/train split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# It contains the following 6 fields:
#
#     target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
#
#     ids: The id of the tweet ( 2087)
#
#     date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
#
#     flag: The query (lyx). If there is no query, then this value is NO_QUERY.
#
#     user: the user that tweeted (robotickilldozr)
#
#     text: the text of the tweet (Lyx is cool)




