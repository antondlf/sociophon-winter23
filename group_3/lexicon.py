## File loads NRC-VAD-Lexicon into a python dictionary, and sets up a function 

lexicon_path = 'NRC-VAD-Lexicon.txt'

class Lexicon:
    """Define class for the lexicon"""
    
    # Initialize with hardcoded path for ease
    def __init__(self, path=lexicon_path):
    
        with open(path) as f: 

            rows = (line.split('\t') for line in f)
            # The format of the lexicon is word, valence, arousal, dominance
            # Grab valence and arousal and cast to float
            self.dictionary = {row[0]: {'valence': float(row[1]), 'arousal': float(row[2])} for row in rows}


    def valence(self, word):
        
        return self.dictionary[word]['valence']
        
  
  
    def arousal(self, word):
        
        return self.dictionary[word]['arousal']
        
        

if __name__ == '__main__':
    
    data_path = #insert path '../Group_1/all_vowel_measurements_TOTALLY_YinLin_24Feb2023.csv'
    word_row = # insert word_row name
    lexicon = Lexicon()
    
    df = pd.read_csv(data_path)
   
    df['valence'] = df.word_row.map(lambda x: lexicon.valence(x))
    df['arousal'] = df.word_row.map(lambda x: lexicon.arousal(x))
    
    df.to_csv('data_affect.csv')
