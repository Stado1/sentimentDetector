#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def graphTweetsPerDay(data):
    # copy to silence error
    dataDay = data.copy()

    # remove useless data
    dataDay = dataDay[['target', 'date']]

    # remove timezone abbreviations (like "PDT") before parsing
    dataDay['date'] = (
        dataDay['date']
        .str.replace(r' [A-Z]{3} ', ' ', regex=True)  # remove timezone (3 uppercase letters)
        .pipe(pd.to_datetime, errors='coerce')
    )

    # BOTH 0 and 4
    dataDay['day'] = dataDay['date'].dt.date
    counts = dataDay.groupby(['day', 'target']).size().unstack(fill_value=0)
    counts = counts.sort_index()

    # print amount of tweets on specific day
    # target_date = pd.to_datetime('2009-05-23').date()
    # tweets_on_date = data[data['date'].dt.date == target_date]
    # print(f"Tweets from {target_date}:")
    # print(tweets_on_date)
    # print(f"\nTotal tweets: {len(tweets_on_date)}")


    # plot the histogram
    plt.figure(figsize=(15,6))
    counts.plot(kind='bar', width=0.6)  # bar plot for counts
    plt.xlabel('Date (Month Day)')
    plt.ylabel('Number of Entries')
    plt.title('Number of Entries per Date')
    plt.xticks(rotation=90)  # rotate x-axis labels for readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("graphs/graphTweetsPerDay.png")
    plt.close()








def graphTweetsPerHour(data):
    # print("IHIHIHIHIHI")
    # copy to silence error
    dataHour = data.copy()

    # Extract just the hour (two digits after the day/month)
    dataHour['hour'] = dataHour['date'].str.extract(r'\s(\d{2}):\d{2}:\d{2}\s')[0]

    # Check result
    print(dataHour[['target','date', 'hour']].head())
    print(dataHour[['target','date', 'hour']].tail())

    # convert to integer
    dataHour['hour'] = dataHour['hour'].astype(int)

    # counts = dataHour.groupby(['hour', 'target']).size().unstack(fill_value=0)
    counts = dataHour.groupby(['hour', 'target']).size().unstack(fill_value=0)
    counts = counts.sort_index()

    plt.figure(figsize=(10,6))
    # plt.hist(counts['hour'], bins=24, range=(0,24), color='skyblue', edgecolor='black')
    counts.plot(kind='bar', width=0.6)  # bar plot for counts
    plt.xticks(range(0, 24))
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Entries')
    plt.title('Number of Entries per Hour')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("graphs/graphTweetsPerHour.png")
    plt.close()





