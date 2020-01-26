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


yeet = "I hated work today. I loved talking to TOM. I got work"


# FUNCTIONS THAT RUN BEFORE TO CLEAN CODE
def preproc(text):
        final = []
        text = tokenizer.tokenize(text.lower());
        
        for n in text:
            if n not in stopWords:
                final.append(n);
        return final
    
# QUERY CODE
def intentfram (sent):
    score = sid.polarity_scores(sent);
    mat = 100* score['pos'] -100 * score['neg']
    return mat



def display (z):
    for x in z:
        print(x)
        
        
def start(text):
    #JANK
    inde = []
    total = 0;
    count = 0;
    
    
    phara = sent_tokenize(text)
    for rawsent in phara:
        count += 1;
        sent = pos_tag(preproc(rawsent))
        inde.append(intentfram(rawsent));
        total += intentfram(rawsent);
    
    total = total/count;
    print("SENTANCE SCORE:")
    display(inde);
    print("TOTAL SCORE:")
    print(total)

    


start(yeet)

