import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


def split_sentences(text):
    sentences = sent_tokenize(text)
    return sentences


def clean_stopwords(text):
    stop_words = stopwords.words('english')
    # Checks if any of the words are in the list of stopwords, if they are, they are removed
    new_sentence = " ".join([i for i in text if i not in stop_words])
    return new_sentence


def clean_text(text):
    # Removes special characters, non-text numbers, and unnecessary punctuations
    clean_sentences = pd.Series(text).str.replace("[^a-zA-Z]", " ")

    # Return all sentences as lowercase
    clean_sentences = [i.lower() for i in clean_sentences]

    # Remove stopwords
    clean_sentences = [clean_stopwords(i.split()) for i in clean_sentences]
    return clean_sentences


def remove_short_words(text):
    for i in range(len(text)):
        text[i] = " ".join([w for w in text[i].split() if len(w) > 3])
        text[i] = " ".join([w for w in text[i].split() if w != "said"])

    return text
