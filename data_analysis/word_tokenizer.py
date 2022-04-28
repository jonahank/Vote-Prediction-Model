import pandas as pd
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
import lemmy


#Adding ., to the stopwords and inizializing the stopwords list.
stop_words = set(stopwords.words('danish'))

lst = ['.',',','!','?',':',';']

for i in lst:
    stop_words.add(i)


lemmatizer = lemmy.load("da")


def tokenize(text):
    word_tokens = word_tokenize(text, language='danish')
    return [lemmatizer.lemmatize("", w.lower())[0] for w in word_tokens if not w.lower() in stop_words]
   