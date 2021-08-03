""" 
Cleaning Text Steps
1. Create a text file and take text from it
2. Convert the letter into lowercase (Apple != apple)
3. Remove punctuations like .,!? etc
"""

import string
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def load_data_excel(file_path):
    data_frame = pd.read_excel(file_path, usecols='B')
    return data_frame['Data'].tolist()


def load_data_txt(file_path):
    text = open('read.txt', encoding="utf-8").read()
    return text


def convert_lowercase(text):
    # Converting to lowercase
    lowercase = text.lower()
    return lowercase


def remove_punctuation(text):
    # Remove punctuation
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text


def split2words(text):
    # Spliting text into words
    tokenizer_words = word_tokenize(text, "english")
    # tokenizer_words = cleaned_text.split()
    # print(tokenizer_words)
    final_words = []
    for word in tokenizer_words:
        if word not in stopwords.words('english'):
            final_words.append(word)
    return final_words

# # stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
# #               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
# #               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
# #               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
# #               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
# #               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
# #               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
# #               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
# #               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
# #               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


'''
NLP Emotion Algorithm
1. Check if the word in the final word list is also present in emotion.txt
    - Open the emotion file
    - Loop through each line and clear it
    - Extract the word and emotion using split
2. If word is present -> Add the emotion to emotion_list
3. Finally count each emotion in the emotion list
'''


def emotion_analysis(emotion_path, final_words):
    emotion_list = []
    with open(emotion_path, 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(
                ',', '').replace("'", '').strip()
            word, emotion = clear_line.split(': ')
            # print(f"Word: {word}, Emotion: {emotion}")

            if word in final_words:
                emotion_list.append(emotion)
    return emotion_list


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        score['sentiment'] = "Negative"
    elif pos > neg:
        score['sentiment'] = "Positive"
    else:
        score['sentiment'] = "Neutral"
    print(score)
    return score


if __name__ == '__main__':
    data = load_data_excel('./Data/game.xlsx')
    emotion_list = []
    for sentence in data:
        text_lowercase = convert_lowercase(sentence)
        clean_text = remove_punctuation(text_lowercase)
        word_list = split2words(clean_text)
        # print(word_list)
        emotion_list.extend(emotion_analysis('emotions.txt', word_list))
        sentiment_analyse(clean_text)
    w = Counter(emotion_list)
    print(w)

    # Plotting the emotions on the graph
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('emotion_graph.png')
    plt.show()

    # Plotting the sentiment on the graph
    