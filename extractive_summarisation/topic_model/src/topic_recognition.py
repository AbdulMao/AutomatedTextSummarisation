from extractive_summarisation.topic_model.src import prepare_data as pd
from extractive_summarisation.topic_model.src import svd_model as svd

def topic_recognition(text):
    text = pd.split_sentences(text)
    text = pd.clean_text(text)
    text = pd.remove_short_words(text)

    topics = svd.create_svd(text)

    return topics

