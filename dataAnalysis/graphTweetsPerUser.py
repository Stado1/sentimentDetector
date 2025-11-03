#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def graphTweetsPerUser(data):
    # group by user and target, then count tweets
    tweetsPerUser = data.groupby(['user', 'target']).size().unstack(fill_value=0)

    # add a total column
    tweetsPerUser['total'] = tweetsPerUser.sum(axis=1)

    # sort by total tweets
    # tweetsPerUser = tweetsPerUser.sort_values('total', ascending=False)

    print(tweetsPerUser.head())
    print(tweetsPerUser.tail())
    print(tweetsPerUser.shape)

    num_unique_totals = tweetsPerUser['total'].nunique()
    print(num_unique_totals)

    summary = tweetsPerUser.groupby('total').agg(
        num_users=('total', 'size'),
        positive=('positive', 'sum'),
        negative=('negative', 'sum')
    ).reset_index()

    # add column with percentage of positive comments
    summary['positive_ratio'] = summary['positive'] / (summary['positive'] + summary['negative'])


    # REMOVE SOME DATA
    # summary = summary.drop(index=[172, 173, 174, 175, 176, 177]) # remove multiple rows
    summary = summary[summary['num_users']>=5] # remove sparse data


    print(summary.head())
    print(summary.tail())
    print(summary.shape)

    plt.figure(figsize=(10,6))
    plt.scatter(summary['total'], summary['positive_ratio'])
    plt.title('Positive Ratio vs Total Tweets per User')
    plt.xlabel('Total Tweets per User')
    plt.ylabel('Positive Ratio')
    plt.grid(True, alpha=0.3)
    plt.savefig("graphs/graphPositiveRatio.png")
    plt.close()

    plt.figure(figsize=(10,6))
    plt.scatter(summary['total'], summary['num_users'])
    plt.title('Positive Ratio vs Total Tweets per User')
    plt.xlabel('Total Tweets per User')
    plt.ylabel('Positive Ratio')
    plt.grid(True, alpha=0.3)
    plt.savefig("graphs/graphAmountUsersVsAmountTweets.png")
    plt.close()
    # # user_counts = data.groupby('user').size()
    # # print(user_counts.head())
    # one = (tweetsPerUser['total'] == 1).sum()
    # two = (tweetsPerUser['total'] == 2).sum()
    # three = (tweetsPerUser['total'] == 3).sum()
    # four = (tweetsPerUser['total'] == 4).sum()
    # five = (tweetsPerUser['total'] == 5).sum()
    # more = (tweetsPerUser['total'] > 5).sum()
    # print(f"ONe: {one}")
    # print(f"two: {two}")
    # print(f"3: {three}")
    # print(f"4: {four}")
    # print(f"O5: {five}")
    # print(f"More: {more}")











