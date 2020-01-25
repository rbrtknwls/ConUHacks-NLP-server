from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk import pos_tag



stopWords = set(stopwords.words('english'))

tokenizer = RegexpTokenizer(r'\w+')
sid = SentimentIntensityAnalyzer()


yeet = "I hated work today. I talked to TOM. I got work"


# FUNCTIONS THAT RUN BEFORE TO CLEAN CODE
def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
# QUERY CODE

def start(text):
    
    phara = sent_tokenize(text)
    for rawsent in phara:
        print("-------")
        sent = pos_tag(preproc(rawsent))
        
        
        print(sid.polarity_scores(rawsent));
        #doc = nlp("Google is");
        #print([(X.text, X.label_) for X in doc.ents])



start(yeet)

