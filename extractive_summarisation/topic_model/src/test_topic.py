import unittest
import prepare_data as pd

class TestTopic(unittest.TestCase):

    def test_split_sentences(self):
        sentence = "This is SENTENCE one. Sentence 2 is all about him and her. This is a sentence about a cat"
        expected = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
        result = pd.split_sentences(sentence)
        self.assertEqual(result, expected)

    def test_clean_stopwords(self):
        sentence = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
        expected = ['sentence one', 'sentence', 'sentence cat']
        result = pd.clean_text(sentence)
        self.assertEqual(result, expected)

    def test_remove_short_words(self):
        sentence = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
        expected = ['This SENTENCE one.', 'Sentence about her.', 'This sentence about']
        result = pd.remove_short_words(sentence)
        self.assertEqual(result, expected)


# sentence = "This is SENTENCE one. Sentence 2 is all about him and her. This is a sentence about a cat"
# split_sentences = ['This is SENTENCE one.', 'Sentence 2 is all about him and her.', 'This is a sentence about a cat']
# results1 = pd.split_sentences(sentence)
# results2 = pd.clean_text(split_sentences)
# results3 = pd.remove_short_words(split_sentences)
#
# print(results1)
# print(results2)
# print(results3)
#
#
# _results2 =  ['sentence one', 'sentence', 'sentence cat']
# _results3 =  ['This SENTENCE one.', 'Sentence about her.', 'This sentence about']

