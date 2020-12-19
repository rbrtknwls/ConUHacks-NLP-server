# ----- IMPORTS -----

from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk import pos_tag


# ----- REFs -----
stopWords = set(stopwords.words('english'))
# get rid of words we dont like
tokenizer = RegexpTokenizer(r'\w+')
# Tokenize AKA split into words without including periods
sid = SentimentIntensityAnalyzer()
# Call the prebuilt Sentiment ML algo

#SAMPLE TEXT, PASSED INFO FROM THE MV WILL GO HERE
yeet = "I hated work today. I loved talking to TOM. I got work"


# ----- FUNCTIONS -----
def preproc(text):
    #Pass in string
        final = []
        text = tokenizer.tokenize(text.lower());
        #Split string into words
        for n in text:
            if n not in stopWords:
                #Check if each word is not in words we dont like
                final.append(n);
        #return list of words we like
        return final
    
# QUERY CODE
def intentfram (sent):
    #Code to find intensisty
    score = sid.polarity_scores(sent);
    #Score is a dict with entries for [pos] = positivity and [neg] = negitivity
    mat = 100* score['pos'] -100 * score['neg']
    return mat


#Display Code
def display (z):
    for x in z:
        print(x)
        
        
def start(text):
    #inde = list of final points
    inde = []
    #To find average we do total/count (the number of data points)
    total = 0;
    count = 0;
    
    #Split the paragraph into sentances
    phara = sent_tokenize(text)
    for rawsent in phara:
        count += 1;
        
        #Add intent point onto inde
        inde.append(intentfram(rawsent));
        #Add to the sum of the total
        total += intentfram(rawsent);
    
    total = total/count;
    print("SENTANCE SCORE:")
    display(inde);
    print("TOTAL SCORE:")
    print(total)

    


start(yeet)

