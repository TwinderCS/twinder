import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# Generates a word cloud (taking into account the frequency of hashtags in tweets)

def word_freq(texts):
    freq = {}
    for text in texts:
        for word in text.split(" "):
            try:
                if word[0] == "#":
                    val = freq.get(word.lower(), 0)
                    freq[word.lower()] = val + 1
            except:
                # only if the word is empty
                pass
    return freq

def create_image(frequencies):
    twitter_mask = np.array(Image.open("../dumps/twitter_logo.png"))

    wc = WordCloud(font_path="../dumps/font.ttf", max_words=1000, background_color="white", mask=twitter_mask, stopwords=STOPWORDS)
    wc.generate_from_frequencies(frequencies)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
  
    
df = pd.read_pickle("../dumps/df.pkl")
freq = word_freq(df['text'])
create_image(freq)
    
