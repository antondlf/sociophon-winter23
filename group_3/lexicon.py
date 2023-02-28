## File loads NRC-VAD-Lexicon into a python dictionary, and sets up a function 
import os
import pandas as pd
import numpy as np
import stanza
from sentiment_extractor import SentimentAnalyzer

# lemmatizer
stanza.download('en', processors='tokenize, mwt, pos, lemma')
nlp_en = stanza.Pipeline('en', processors='tokenize, lemma', lemma_pretagged=True, tokenize_pretokenized=True)

# All paths used
# Depending on where this is run you may have to change your working dir to
# The root of the project. Add your path and uncomment the lines below:

# root_dir = 'YOUR PATH TO THE PROJECT'
# rood_dir = os.chdir(root_dir)
# print(os.getcwd())

lexicon_path = 'group_3/NRC-VAD-Lexicon.txt'
group_1_dir = 'Group_1'
data_path_totally = 'Group_1/all_vowel_measurements_TOTALLY_YinLin_24Feb2023.csv'
data_path_so = 'Group_1/UPDATED_so_with_columns.csv'


def lemmatize_token(wrd):

    doc = nlp_en(wrd.lower())
    # function assumes single word string so 0 index
    return doc.sentences[0].words[0].lemma


class Lexicon:
    """Define class for the lexicon"""
    # Initialize with hardcoded path for ease
    def __init__(self, path=lexicon_path):
    
        with open(path) as f: 

            rows = (line.split('\t') for line in f)
            # The format of the lexicon is word, valence, arousal, dominance
            # Grab valence and arousal and cast to float
            self.dictionary = {row[0]: {'valence': float(row[1]), 'arousal': float(row[2])} for row in rows}

    # Functions check that input is a string, lower_case, and look up values
    def valence(self, word):

        if type(word) == str:

            try:

                lemma = lemmatize_token(word)

                return self.dictionary[lemma]['valence']

            except KeyError:
                pass

        return np.nan

    def arousal(self, word):

        if type(word) == str:
            try:

                lemma = lemmatize_token(word)
                return self.dictionary[lemma]['arousal']

            except KeyError:

                pass

        return np.nan
    
    
def main(data_path):

    df = pd.read_csv(data_path)

    lexicon = Lexicon()
    # Make sure words are lower cased
    df['valence'] = df.fol_word.map(lambda x: lexicon.valence(x))
    df['arousal'] = df.fol_word.map(lambda x: lexicon.arousal(x))
    
    return df
        

if __name__ == '__main__':
    
    main(data_path_totally).to_csv('group_3/vowels_totally_affect.csv')
    main(data_path_so).to_csv('group_3/vowels_so_affect.csv')
