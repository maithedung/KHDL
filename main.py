""" 
Cleaning Text Steps
1. Create a text file and take text from it
2. Convert the letter into lowercase (Apple != apple)
3. Remove punctuations like .,!? etc
"""

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt', encoding="utf-8").read()

# Converting to lowercase
lowercase = text.lower()

# Remove punctuation
cleaned_text = lowercase.translate(str.maketrans('', '', string.punctuation))
# print(cleaned_text)

# Spliting text into words
tokenizer_words = word_tokenize(cleaned_text, "english")
# tokenizer_words = cleaned_text.split()
# print(tokenizer_words)

# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenizer_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

'''
NLP Emotion Algorithm
1. Check if the word in the final word list is also present in emotion.txt
    - Open the emotion file
    - Loop through each line and clear the
    - Extract the word and emotion using split
2. If word is present -> Add the emotion to emotion_list
3. Finally count each emotion in the emotion list
'''

emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(
            ',', '').replace("'", '').strip()
        word, emotion = clear_line.split(': ')
        # print(f"Word: {word}, Emotion: {emotion}")

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print('Positive Sentiment')
    else:
        print('Neutral Sentiment')
    print(score)


sentiment_analyse(cleaned_text)

# Plotting the emotions on the graph

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
