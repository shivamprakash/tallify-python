from collections import defaultdict


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
    stopcsv = "by,at,of,be,etc"
    return getStopwords(stopcsv)
