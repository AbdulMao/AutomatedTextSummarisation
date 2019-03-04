import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(original_sentences, sentence_vectors):
    # Create empty Matrix to populate
    matrix = np.zeros([len(original_sentences), len(original_sentences)])

    # Populate the Matrix with cosine similarity values
    for i in range(len(original_sentences)):
        for j in range(len(original_sentences)):
            if i != j:
                matrix[i][j] = \
                    cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]
    return matrix


def page_rank(matrix):
    graph = nx.from_numpy_array(matrix)
    scores = nx.pagerank(graph)
    return scores
