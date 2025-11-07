import re

class Node:
    """Class for nodes in Trie."""

    def __init__(self):
        """Initializes new node."""
        self.children = dict()
        self.is_end_of_word = False

class Trie:
    """Class for Trie structure and it's functions."""

    def __init__(self):
        """Initializes new root node."""
        self.root = Node()

    def insert(self, sentence):
        """"""
        current_node = self.root
        for word in sentence:
            if word in current_node.children:
                current_node.children[word] = Node()
            current_node = current_node.children[word]
        current_node.is_end_of_sentence = True

    def search(self, word):
        """Looks up for a word in Trie.
        Args:
            word = word to look for

        Returns:
            True if word was found, else False.
        """
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c] 
        return current_node.is_end_of_word

    def starts_with(self, word):
        pass

def train_markov_chain(text):
    """Divide text into sentences and create a Markov chain based on them."""
    sentences = text_to_sentences(text)
    print(sentences)

def text_to_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s]
    sentences2 = []
    word = ""
    for s in sentences:
        words = re.split(r'[, ]', s)
        words = [word for word in words if word]
        checked_words = []
        for word in words:
            checked_word = ""
            for c in word:
                if c.isalpha() or c == "ä" or c =="ö":
                    checked_word = checked_word + c
                else:
                    checked_word = ""
                    break
            if checked_word: checked_words.append(checked_word)
        sentences2.append(checked_words)
    return sentences2
