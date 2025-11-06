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