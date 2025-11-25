import unittest
import src.trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.test_trie = src.trie.Trie()

    def test_create_empty_trie(self):
        self.assertIsNone(src.trie.Trie.get_sentence(self.test_trie, 1, 1))

    def test_create_trie_with_nodes(self):
        sentence1 = ["testaaminen", "on", "kivaa"]
        sentence2 = ["on", "kivaa", "testaaminen"]
        src.trie.Trie.insert_sentence(self.test_trie, sentence1)
        src.trie.Trie.insert_sentence(self.test_trie, sentence2)
        self.assertIn(src.trie.Trie.get_sentence(self.test_trie, 3, 2), [sentence1, sentence2])

    def test_length_smaller_than_degree(self):
        sentence1 = ["testaaminen", "on", "kivaa"]
        src.trie.Trie.insert_sentence(self.test_trie, sentence1)
        self.assertEqual(src.trie.Trie.get_sentence(self.test_trie, 1, 2), ["testaaminen"])

    def test_length_longer_than_longest_sentence(self):
        sentence1 = ["testaaminen", "on", "kivaa"]
        src.trie.Trie.insert_sentence(self.test_trie, sentence1)
        self.assertIsNone(src.trie.Trie.get_sentence(self.test_trie, 10, 1))

    def test_text_splitting_works(self):
        text = "OiKeAstI,,,, oik33sti s11s joo &&&on tää AikaMoista, vai?? mitäh."
        correct_split = [["oikeasti"], ["joo", "tää", "aikamoista"], ["vai"], ["mitäh"]]
        self.assertEqual(src.trie.text_to_sentences(text), correct_split)

    def test_markov_chain(self):
        trained_trie = src.trie.train_markov_chain(1)
        first_child = src.trie.Node.get_children(trained_trie.root)[0][0]
        self.assertIn(first_child, "silloin")
