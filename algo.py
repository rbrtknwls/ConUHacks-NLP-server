from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag



stopWords = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')



yeet = "I walked to google. I talked to TOM. I got work"


# FUNCTIONS THAT RUN BEFORE TO CLEAN CODE
def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
# QUERY CODE
def classifynouns(text):
    final = []
    for tup in text:
        if (tup[1][0] == "N"): 
            final.append(tup[0])
    return final

def classifyverbs(text):
    final = []
    for tup in text:
        if (tup[1][0] == "V"): 
            final.append(tup[0])
    return final

def start(text):
    
    phara = sent_tokenize(text)
    for rawsent in phara:
        sent = pos_tag(preproc(rawsent))
        
        
        print ("finding nouns!")
        print(classifynouns(sent));
        print ("finding verbs!")
        print(classifyverbs(sent));
        #doc = nlp("Google is");
        #print([(X.text, X.label_) for X in doc.ents])



start(yeet)


