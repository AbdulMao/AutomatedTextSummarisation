import unittest
import cleanData as cd

class TestSummary(unittest.TestCase):

    def test_split_sentences(self):
        sentence = "This is SENTENCE one. Sentence 2 is all about him and her. This is a sentence about a cat"
        expected = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
        result = cd.split_sentences(sentence)
        self.assertEqual(result, expected)

    def test_clean_stopwords(self):
        sentence = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
        expected = ['sentence one', 'sentence', 'sentence cat']
        result = cd.clean_text(sentence)
        self.assertEqual(result, expected)

