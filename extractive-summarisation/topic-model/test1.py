
import pandas as pd

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


test_article = open("test-article2.txt", "r")

test_article2 = test_article.read()

def split_sentences(text):
    sentences = sent_tokenize(text)
    return sentences


def clean_stopwords(text):
    stop_words = stopwords.words('english')
    # Checks if any of the words are in the list of stopwords, if they are, they are removed
    new_Sentence = " ".join([i for i in text if i not in stop_words])
    return new_Sentence


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
    return text




mydoc = split_sentences(test_article2)
mydoc = clean_text(mydoc)
mydoc = remove_short_words(mydoc)


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english',
max_features= 1000, # keep top 1000 terms
max_df = 0.5,
smooth_idf=True)

X = vectorizer.fit_transform(mydoc)
print(X)

from sklearn.decomposition import TruncatedSVD

# SVD represent documents and terms in vectors
svd_model = TruncatedSVD(n_components=1, algorithm='randomized', n_iter=100, random_state=122)

svd_model.fit(X)

# len(svd_model.components_)
terms = vectorizer.get_feature_names()

for i, comp in enumerate(svd_model.components_):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:4]
    print("Topic "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])
        print(" ")