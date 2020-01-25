from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

from itertools import product


stopWords = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')



yeet = "TODAY I WOKE UP AND HAD SOME COFFEE. Next I walked to school"

def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
def start(text):
    
    phara = sent_tokenize(text)
    
    for rawsent in phara:
        sent = preproc(rawsent)
        print(sent)



start(yeet)


