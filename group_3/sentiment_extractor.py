import stanza
import numpy as np


class SentimentAnalyzer:

    def __init__(self):
        stanza.download('en', processors='tokenize, sentiment')
        self.nlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment')

    def get_sent_sentiment(self, word):
        """Code assumes there is only one sentence"""
        if type(word) == str:
            try:
                return self.nlp(word.lower()).sentences[0].sentiment

            except AttributeError:

                return np.nan
