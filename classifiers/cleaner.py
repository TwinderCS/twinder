import nltk
from autocorrect import Speller
import re

#nltk.download('stopwords')
#nltk.download('wordnet')

def cleaner(text : str):
    """
    Cleans the text by
    - running a spellchecker
    - making the text lowercase
    - removing stopwords
    - removing punctuation
    - lemmatizing
    """
    
    speller = Speller(lang='en')
    unpunctuated = re.sub("[^a-zA-Z\s]+", " ", text)
    lowered = unpunctuated.lower()
    text = lowered
    stops = nltk.corpus.stopwords.words('english')
    words = [word for word in text.split(" ") if word not in stops]
    corrected = [speller(word) for word in words]
    lm = nltk.stem.WordNetLemmatizer()
    lemmatized = [lm.lemmatize(word) for word in corrected]
    return " ".join(lemmatized)
