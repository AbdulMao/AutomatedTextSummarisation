from extractive_summarisation.summariser.src import cleanData
from extractive_summarisation.summariser.src import sentenceVectors
from extractive_summarisation.summariser.src import calculateSimilarity


def createSummary(orginalSentences, pageRankScores):
    ranked_sentences = sorted(((pageRankScores[i], s) for i, s in enumerate(orginalSentences)), reverse=True)
    s= ""
    for i in range(3):
        s = s + " " + ranked_sentences[i][1]
    return s


def runitAll(inputText):
    originalSentences1 = cleanData.split_sentences(inputText)
    cleanSentences1 = cleanData.clean_text(originalSentences1)
    sentenceVectors1 = sentenceVectors.create_sentenceVectors(cleanSentences1)
    matrix1 = calculateSimilarity.calculate_cosine_similarity(originalSentences1, sentenceVectors1)
    scores1 = calculateSimilarity.page_rank(matrix1)
    answer = createSummary(originalSentences1, scores1)
    return answer



