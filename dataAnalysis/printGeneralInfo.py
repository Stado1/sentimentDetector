#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def printInfo(data):
    print("amount of rows: ")
    print(data.shape[0])

    print("amount of columns: ")
    print(data.shape[1])

    print("example of one data entry: ")
    print(data.columns)

    print("amount of users")
    numUsers = data['user'].nunique()
    print(data['user'].nunique())

    print("average amount of tweets per user")
    print(data.shape[0]/numUsers)

    test = data[data['user'] == 'zzzunzinnn']
    print(test)

