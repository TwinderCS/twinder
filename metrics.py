import numpy as np
emotions = ["joy", "sadness", "fear", "anger", "surprise"]
topics = ["politics", "health", "emotion", "financial", "sport", "science"]

def user_dist(u1, u2):
    global topics
    global emotions
    return np.sqrt(((u1-u2)**2).sum())
