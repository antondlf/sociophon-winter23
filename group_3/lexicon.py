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
        
        
