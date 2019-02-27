import cleanData
import sentenceVectors
import calculateSimilarity


def createSummary(orginalSentences, pageRankScores):
    ranked_sentences = sorted(((pageRankScores[i], s) for i, s in enumerate(orginalSentences)), reverse=True)
    s= ""
    for i in range(3):
        s = s + " " + ranked_sentences[i][1]
    return s
        # print(ranked_sentences[i][1])


def runitAll(inputText):
    originalSentences1 = cleanData.split_sentences(inputText)
    cleanSentences1 = cleanData.clean_text(originalSentences1)
    sentenceVectors1 = sentenceVectors.create_sentenceVectors(cleanSentences1)
    matrix1 = calculateSimilarity.calculate_cosine_similarity(originalSentences1, sentenceVectors1)
    scores1 = calculateSimilarity.pageRank(matrix1)
    answer = createSummary(originalSentences1, scores1)
    return answer

text = "We have known since 2014, when City reluctantly accepted a settlement with Uefa that included a £49m fine (two-thirds of which was suspended and avoided) along with restrictions on their European squad and incoming transfers, that the club were found to have breached the FFP rules. What Der Spiegel's revelations claim to have shown for the first time however is how it was done, and the extent of the alleged deception.So far the claims of financial malpractice fall into two broad categories; firstly, that sponsorship deals were artificially inflated and not valued fairly or independent (as City previously insisted), with tens of millions of pounds thought to have been paid by commercial partners, actually coming directly and discreetly from the club's owner. And secondly, that City under a scheme called Project Longbow set up a shell company to pay players for image rights, saving millions more from the wage bill.The BBC has not been able to verify the leaked emails published by Der Spiegel, and City have refused to comment, beyond saying that the documents are purportedly hacked or stolen and an organised attempt to smear the club. But crucially, nor have they denied they are genuine. If they are authentic - (and Der Spiegel insist that their source - purportedly the founder of the Football Leaks whistleblower website - has assured them that he did not hack or steal the documents) - then many will inevitably conclude that they do not reflect well on the club, and raise serious questions over its integrity and its respect for the rules.What is not yet fully known is how much of this Uefa was already aware of, and how much it really cares."

print(runitAll(text))