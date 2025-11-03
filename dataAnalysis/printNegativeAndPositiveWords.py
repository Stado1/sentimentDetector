#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import re

def printMostUsedWords(data):
    top_n = 50
     # Combine all tweets into one big string
    all_text = " ".join(data['text'].astype(str))

    # Lowercase everything
    all_text = all_text.lower()

    # Remove URLs, mentions, hashtags, punctuation, and numbers
    all_text = re.sub(r'http\S+|www\S+|@\w+|#\w+|[^a-z\s]', '', all_text)

    # Split into individual words
    words = all_text.split()
    print("words")
    print(type(words))
    print(len(words))

    # Count word frequencies
    word_counts = Counter(words)

    # Get the top N most common words
    most_common = word_counts.most_common(top_n)

    # Print results
    print(f"Top {top_n} most used words:")
    for word, count in most_common:
        print(f"{word}: {count}")
        findTweetsWithSpecificWord(data, word)
        print("---------------------------")




def findTweetsWithSpecificWord(data, search_word):
    # Define your search term
    # search_word = "i"
    print("search word = ", search_word)
    # Filter tweets containing the word (case insensitive)
    results = data[data['text'].str.contains(search_word, case=False, na=False)]
    print(results.shape)
    # print(results.head())

    positiveData = results[results['target'] == 'positive']
    negativeData = results[results['target'] == 'negative']

        # find amount of data per type
    positiveCount = positiveData.shape[0]
    negativeCount = negativeData.shape[0]

    print("positve = ", positiveCount)
    print("negative = ", negativeCount)
    print("positve / negative+positive = ", positiveCount/(positiveCount+negativeCount))

    # Show some results
    # print(results.iloc[0]['text'])
    # print(results.iloc[1]['text'])
    # print(results.iloc[2]['text'])
    # print(results.iloc[3]['text'])
