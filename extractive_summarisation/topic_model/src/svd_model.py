from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


def create_svd(text):
    vector_model = TfidfVectorizer(stop_words='english',
                                   max_features=1000,  # keep top 1000 terms
                                   max_df=0.65,
                                   smooth_idf=True)
    textvector = vector_model.fit_transform(text)

    # SVD represent documents and terms in vectors
    svd_model = TruncatedSVD(n_components=3,
                             algorithm='randomized',
                             n_iter=100,
                             random_state=122)

    svd_model.fit(textvector)

    word_representations = vector_model.get_feature_names()

    for i, comp in enumerate(svd_model.components_):
        terms_comp = zip(word_representations, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:4]
        top_topics = []
        for t in sorted_terms:
            top_topics.append(t[0])
        return top_topics
