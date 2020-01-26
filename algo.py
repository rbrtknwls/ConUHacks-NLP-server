from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag

import spacy 
  
nlp = spacy.load('en_core_web_sm') 

stopWords = set(stopwords.words('english') + ["hate","dislike","like","love","hated","disliked","liked",'loved','today'])
tokenizer = RegexpTokenizer(r'\w+')

yeet = "I like playing tennis. I learned about math."
#yeet = "I ran today. I participated in a hackathon. I sleep at the hackathon. "

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
    indexa = 0
    indexr = 0
    indexw = 0
    ttext = nlp(text)
    active = ['swim', 'drown', 'swimming', 'float', #index for swim
              'jog','jogged', 'ramble', 'nudge', 'trot', 'lope', #index for jog
             'walk','walking','walked','pass','run', #index for jog
             'ski', #index for ski
             'run','ran', 'go'] #index for ski
    
    rec = ['consume', 'eat', 'munch', #index for eat
             'observe','watch','watch', 'see', 'view','viewed', #index for see
             'blab','lecture','speak','talk','talked','sing' #index for talk
             'play','played', #index for play
             'dance', 'sleep'] #index for dance 
    
    wor = ['code', 'learn', 'study', #index for eat
             'memorize','instruct','work', 'cram', 'do','did', #index for see
             'remember','consider'] 
    
    for word in active:
        z = nlp(word)
        indexa = max(indexa, z.similarity(ttext))
        
    for word in rec:
        z = nlp(word)
        indexr = max(indexr, z.similarity(ttext))
        
    for word in wor:
        z = nlp(word)
        indexw = max(indexr, z.similarity(ttext))
        
    
    
    if (indexa > indexr and indexa > indexw):
        return ("active")
    elif (indexr > indexa and indexr > indexw):
        return ('recreational')
    else:
        return('work')
    
    
    
    return("ass")

def gensudonyms(text):
    synonyms = [] 
  
    for syn in wordnet.synsets(text): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
    
    return set(synonyms)
  

    
def start(text):
    li = [["active"],["recreational"],["work"]]
    phara = sent_tokenize(text)
    for rawsent in phara:
        print(rawsent)
        sent = nlp(' '.join(preproc(rawsent)))
        
        for word in sent:
            print(word.pos_)
            
        verb = classifyverbs(sent);
        noun = nnouns(sent);
        
        
        
        if (len(verb) == 0):
            print("SENT DOESNT MAKE SENSE")
        
        else:
            verb = verb[0]
            print(verb)
            
            vresult = simindexv(verb)
            
            
            print("PARENT:" +vresult)
            print("CHILD:   " + verb )
            if (len(noun) != 0):
                noun = noun[0]
                print("CHILD:         " + noun )
            
            
        
       
        
        
        
        '''
        print ("finding verbs!")
        print(classifyverbs(sent));
        print ("finding nouns!")
        print(nnouns(sent));
        '''



        
def saving(group, text):
    val = {}
    
    if group in val and text in val[group]:
        print("PASS")
    else:
        val[group,text] = text
    
    print(val);
#start(yeet)
saving("active","ass")

