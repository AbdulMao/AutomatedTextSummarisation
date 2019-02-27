import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity


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
