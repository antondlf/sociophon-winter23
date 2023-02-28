## File loads NRC-VAD-Lexicon into a python dictionary, and sets up a function 
import os
import pandas as pd
import numpy as np

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
                return self.dictionary[word.lower()]['valence']

            # Words that aren't in lexicon are likely inflected
            # and therefore probably not adjectives
            # worth running a lemmatizer at some point though.
            except KeyError:
                pass

        return np.nan

    def arousal(self, word):

        if type(word) == str:
            try:
                return self.dictionary[word.lower()]['arousal']

            except KeyError:

                pass

        return np.nan
    
    
def main(data_path, lexicon):
    
    df = pd.read_csv(data_path)

    # Make sure words are lower cased
    df['valence'] = df.fol_word.map(lambda x: lexicon.valence(x))
    df['arousal'] = df.fol_word.map(lambda x: lexicon.arousal(x))
    
    return df
        

if __name__ == '__main__':
    
    lexicon = Lexicon()    
    
    main(data_path_totally, lexicon).to_csv('group_3/vowels_totally_affect.csv')
    main(data_path_so, lexicon).to_csv('group_3/vowels_so_affect.csv')
