# Book: Python 3 Text Processing with NLTK 3 Cookbook By Jacob Perkins
# Program: Tokeinizing text into sentence
# Date: 11/05/2017 06:55 PM

import nltk
import nltk.data
from nltk.tokenize import sent_tokenize

def test_sent_tokenize():    
    para = "Hello Mister. How is your days going on? Have you bathed yet? Okay, See you."
    result = sent_tokenize(para)
    print(result)
    #['Hello Mister.', 'How is your days going on?', 'Have you bathed yet?', 'Okay, See you.']

    
def test_tokenizer():
    tokenizer = nltk.data.load("tokenizers\punkt\english.pickle")
    para = "This is NLTK. How much I am going to learn depends on me, right? I am going to have a bath now, See ya!."
    result = tokenizer.tokenize(para)
    print(result)
    #['This is NLTK.', 'How much I am going to learn depends on me, right?', 'I am going to have a bath now, See ya!.']


if __name__ == '__main__':
    test_sent_tokenize()
    test_tokenizer()
