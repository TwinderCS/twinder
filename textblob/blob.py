# NE PAS APPELER CE FICHIER TEXTBLOB

from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

print(wiki.tags)

print(wiki.noun_phrases)

print(wiki.sentiment)

