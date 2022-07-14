from nltk import word_tokenize
import difflib
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

class KeyWord:
    def __init__(self, text):
        self.text = word_tokenize(text)
    def __str__(self):
        return f"{self.text}"

class Word:
    def __init__(self, word, index, rate=0,):
        self.word = morph.normal_forms(word)[0]
        self.rate = rate
        self.index = index
    def __str__(self):
        return f"{self.word}"

def comporation(word_f, word_s):
    """f-first, s-second"""
    word_f = word_f.lower()
    word_s = word_s.lower()
    if len(word_f) - len(word_s) <= 2:
        matcher = difflib.SequenceMatcher(None, word_f, word_s)
        return matcher.ratio()
    else:
        return 0


