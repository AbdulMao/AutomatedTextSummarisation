from extractive_summarisation.summariser.src import cleanData
from extractive_summarisation.summariser.src import sentenceVectors
from extractive_summarisation.summariser.src import calculateSimilarity
import math
import json


def createSummary(orginalSentences, pageRankScores):
    summaryLength50 = math.ceil(len(orginalSentences) * 0.5)
    summaryLength30 = math.ceil(len(orginalSentences) * 0.3)
    summaryLength20 = math.ceil(len(orginalSentences) * 0.2)
    summaryLength10 = math.ceil(len(orginalSentences) * 0.1)
    ranked_sentences = sorted(((pageRankScores[i], s) for i, s in enumerate(orginalSentences)), reverse=True)
    s50 = ""
    s30 = ""
    s20 = ""
    s10 = ""
    for i in range(summaryLength50):
        s50 = s50 + " " + ranked_sentences[i][1]

    for i in range(summaryLength30):
        s30 = s30 + " " + ranked_sentences[i][1]

    for i in range(summaryLength20):
        s20 = s20 + " " + ranked_sentences[i][1]

    for i in range(summaryLength10):
        s10 = s10 + " " + ranked_sentences[i][1]

    return(
        {
            'summary50': s50,
            'summary30': s30,
            'summary20': s20,
            'summary10': s10
        }
    )



def runitAll(inputText):
    originalSentences1 = cleanData.split_sentences(inputText)
    cleanSentences1 = cleanData.clean_text(originalSentences1)
    sentenceVectors1 = sentenceVectors.create_sentenceVectors(cleanSentences1)
    matrix1 = calculateSimilarity.calculate_cosine_similarity(originalSentences1, sentenceVectors1)
    scores1 = calculateSimilarity.page_rank(matrix1)
    answer = createSummary(originalSentences1, scores1)
    return answer
