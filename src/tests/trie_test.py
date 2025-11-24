import unittest
import src.trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_create_empty_trie(self):
        test_trie = src.trie.Trie()
        sentence = src.trie.Trie.get_sentence(test_trie, 0, 0)
        self.assertEqual(sentence, [])

    def test_create_trie_with_nodes(self):
        test_trie = src.trie.Trie()
        sentence = ["testaaminen", "on", "ihan", "kivaa"]
        src.trie.Trie.insert_sentence(test_trie, sentence)
        self.assertEqual(src.trie.Trie.get_sentence(test_trie, 4, 3), sentence)
