import numpy as np


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
