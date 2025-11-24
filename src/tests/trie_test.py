import unittest
import src.trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_create_trie(self):
        test_trie = src.trie.Trie()
        sentence = src.trie.Trie.get_sentence(test_trie, 0, 0)
        self.assertEqual(sentence, [])
