import nltk
import re
import string
from nltk.tokenize import TweetTokenizer

def tokenize(tweet):
    tweet = re.sub(r'\$\w*','',tweet)
    tweet = re.sub(r'RT^[\s]+','',tweet)
    tweet = re.sub(r'http?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#', '', tweet)

    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    tweet_token = tokenizer.tokenize(tweet)

    tweet_clean = []
    for word in tweet_token:
      if (word not in string.punctuation):
        tweet_clean.append(word)
    return tweet_clean
