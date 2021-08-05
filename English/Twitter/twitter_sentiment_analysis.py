'''
Description: This is a sentiment analysis program that parses the tweets fetched from Twitter usin Python
'''

# Import the libraries
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Get 