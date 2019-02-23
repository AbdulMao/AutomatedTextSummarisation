import numpy as np
import pandas as pd
import networkx as nx
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

# Execute once
# nltk.download('punkt')
# nltk.download('stopwords')

test_article = open("test-article.txt", "r")

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


text1 = split_sentences(test_article2)
text2 = clean_text(text1)


# print(text2)


def create_sentenceVectors(text):
    # Create word vector of words in dictionary. Using GloVe word embeddings.
    # This uses pre-trained vectors based on Wikipedia and Gigawaord.
    wordEmbeddings = {}
    glove_embeddings = open('C:\git\data\glove.6B.100d.txt', encoding='utf-8')
    for data in glove_embeddings:
        word_embeddings = data.split()
        words = word_embeddings[0]
        number_value = np.asarray(word_embeddings[1:], dtype='float32')
        wordEmbeddings[words] = number_value
    glove_embeddings.close()

    # Create sentence vectors, by finding embedding for each word in the sentence.
    # And then working out average vector of the sentence by using mean vector value.
    sentenceVectors = []
    for i in text:
        if len(i) != 0:
            new_vector = sum([wordEmbeddings.get(word, np.zeros((100,))) for word in i.split()]) / (
                        len(i.split()) + 0.001)
        else:
            new_vector = np.zeros((100,))
        sentenceVectors.append(new_vector)
    return sentenceVectors


def calculate_cosine_similarity(originalSentences, sentenceVectors):
    # Create empty Matrix to populate
    matrix = np.zeros([len(originalSentences), len(originalSentences)])

    # Populate the Matrix with cosine similarity values
    for i in range(len(originalSentences)):
        for j in range(len(originalSentences)):
            if i != j:
                matrix[i][j] = \
                cosine_similarity(sentenceVectors[i].reshape(1, 100), sentenceVectors[j].reshape(1, 100))[0, 0]
    return matrix


def pageRank(matrix):
    graph = nx.from_numpy_array(matrix)
    scores = nx.pagerank(graph)
    return scores


def createSummary(orginalSentences, pageRankScores):
    ranked_sentences = sorted(((pageRankScores[i], s) for i, s in enumerate(orginalSentences)), reverse=True)
    for i in range(6):
        print(ranked_sentences[i][1])


originalSentences1 = split_sentences(test_article2)
cleanSentences1 = clean_text(originalSentences1)
sentenceVectors1 = create_sentenceVectors(cleanSentences1)
matrix1 = calculate_cosine_similarity(originalSentences1, sentenceVectors1)
scores1 = pageRank(matrix1)
createSummary(originalSentences1, scores1)

# print(calculate_cosine_similarity(text1, create_sentenceVectors(text2)))
