def createSummary(orginalSentences, pageRankScores):
    ranked_sentences = sorted(((pageRankScores[i], s) for i, s in enumerate(orginalSentences)), reverse=True)
    for i in range(6):
        print(ranked_sentences[i][1])


def runitAll():
    originalSentences1 = split_sentences(test_article2)
    cleanSentences1 = clean_text(originalSentences1)
    sentenceVectors1 = create_sentenceVectors(cleanSentences1)
    matrix1 = calculate_cosine_similarity(originalSentences1, sentenceVectors1)
    scores1 = pageRank(matrix1)
    createSummary(originalSentences1, scores1)