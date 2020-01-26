from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag

import spacy 
  
nlp = spacy.load('en_core_web_sm') 

stopWords = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')

yeet = "I run to google"

# FUNCTIONS THAT RUN BEFORE TO CLEAN CODE
def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
# QUERY CODE
def nnouns(text):
    final = []
    for tup in text:
        if (tup.pos_ == "NOUN" or tup.pos_ == "PROPN"): 
            final.append(tup.text)
    return final

def classifyverbs(text):
    final = []
    for tup in text:
        if (tup.pos_ == "VERB"): 
            final.append(tup.text)
    return final

# find how simmilar they are to Sports / Work / Rec

def simindexv (text):
    index = 0
    ttext = nlp(text)
    active = ['swim', 'drown', 'swimming', 'float', #index for swim
              'jog','jogged', 'ramble', 'nudge', 'trot', 'lope', #index for jog
             'walk','walking','walked','pass', #index for jog
             'ski', #index for ski
             'run', 'go'] #index for ski
    for word in active:
        z = nlp(word)
        index = max(index, z.similarity(ttext))
    if (index > 0.8):
        return ("active")
    
    return("ass")

def gensudonyms(text):
    synonyms = [] 
  
    for syn in wordnet.synsets(text): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    
    return set(synonyms)
  

    
def start(text):
    
    phara = sent_tokenize(text)
    for rawsent in phara:
        print(rawsent)
        sent = nlp(' '.join(preproc(rawsent)))
        
        for word in sent:
            print(word.pos_)
            
        verb = classifyverbs(sent);
        noun = nnouns(sent);
        
        if (len(verb) == 0 or len(noun) == 0):
            print("SENT DOESNT MAKE SENSE")
        
        else:
            verb = verb[0]
            noun = noun[0]
            print(verb)
            
            vresult = simindexv(verb)

            print("PARENT:" +vresult)
            print("CHILD:   " + verb )
            print("CHILD:         " + noun )
        
        
        
        
        '''

        print ("finding verbs!")
        print(classifyverbs(sent));
        print ("finding nouns!")
        print(nnouns(sent));
        '''



start(yeet)

