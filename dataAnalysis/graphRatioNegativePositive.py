#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def graphPositiveNegative(data):
    # divide dataset into positive, negative and neutral
    positiveData = data[data['target'] == 'positive']
    negativeData = data[data['target'] == 'negative']
    neutralData = data[data['target'] == 'neutral']

    # find amount of data per type
    positiveCount = positiveData.shape[0]
    negativeCount = negativeData.shape[0]
    neutralCount = neutralData.shape[0]

    labels = ['Positive', 'Negative', 'Neutral']
    counts = [positiveCount, negativeCount, neutralCount]

    plt.figure()
    plt.bar(labels, counts)
    plt.title("Tweet Sentiment Bar Graphs")
    plt.xlabel("Sentiment")
    plt.ylabel("Amount of tweets")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("graphs/graphPositiveNegativeNeutral.png")
    plt.close()
