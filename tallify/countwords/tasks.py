from collections import defaultdict
from nltk.corpus import stopwords

def wordCount(words,stopwords):
    d = defaultdict(int)
    for word in words.split():
        if word not in stopwords:
            d[word] += 1
    return d

def getStopwords(stopcsv):
    stopcsv = stopcsv.replace(" ","")
    stopwords = stopcsv.split(",")
    return stopwords

def getDefaultStopWords():
    return stopwords.words('english')
