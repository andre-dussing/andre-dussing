import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def load_words():
    if os.path.exists('wordlist.json'):
        with open('wordlist.json', 'r') as f:
            return json.load(f)
    elif os.path.exists('wordlist.txt'):
        with open('wordlist.txt', 'r') as f:
            lines = f.readlines()
            return {line.strip(): 5 for line in lines if line.strip()}
    else:
        return {"AI": 10, "Python": 8, "Luxembourg": 5, "Security": 6}

words = load_words()

wc = WordCloud(width=800, height=400, background_color='white')
wc.generate_from_frequencies(words)
wc.to_file('wordcloud.png')
