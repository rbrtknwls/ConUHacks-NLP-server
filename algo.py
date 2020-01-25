from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


stopWords = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')



yeet = "TODAY I WOKE UP AND HAD SOME COFFEE. Next I walked to school. I SAW TOM!!!! YAY"

def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
    
def findpnouns(text):
    doc = nlp(text);
    for x in doc.ents:
        print(x.text);
    
def start(text):
    
    phara = sent_tokenize(text)
    for rawsent in phara:
        
        propnoun = findpnouns(rawsent)
        #sent = preproc(rawsent)
        #doc = nlp("Google is");
        #print([(X.text, X.label_) for X in doc.ents])



start(yeet)


