import re

text = "Istuin puun alla ja mietiskelin. Moi, ?? ##00sanoi fsf08098sas8 naapuri. Moi moi, sanoin minä."

class Node:
    """Class for nodes in Trie."""

    def __init__(self):
        """Initializes new node."""
        self.children = {}
        self.frequency = 0

class Trie:
    """Class for Trie structure and it's functions."""

    def __init__(self):
        """Initializes new Trie structure."""
        self.root = Node()

    def insert_sentence(self, sentence):
        """"""
        current_node = self.root
        for word in sentence:
            if word not in current_node.children:
                current_node.children[word] = Node()
            current_node = current_node.children[word]
            self.frequency += 1

    def get_children(self, words):
        """Looks up for a word in Trie.
        Args:
            word = word to look for

        Returns:
            Children of a node.
        """
        current_node = self.root
        for w in words:
            if w not in current_node.children:
                return False
            current_node = current_node.children[w] 
        return current_node
    
    def create_trie(self, sentences, degree):
        """"""
        for s in sentences:
            Trie.insert_sentence(s)

    def train_markov_chain(degree):
        """Divide text into sentences and create a Markov chain based on them."""
        sentences = text_to_sentences()
        trie.create_trie(self, sentences, degree)

def text_to_sentences():
    """Split text into sentences and words."""
    sentences = re.split(r'[.!?,-]', text)
    checked_sentences = []
    for s in sentences:
        words = s.split()
        checked_words = []
        for word in (w for w in words if w):
            checked_word = ""
            for c in word:
                if c.isalpha() or c == "ä" or c =="ö":
                    checked_word = checked_word + c
                else:
                    checked_word = ""
                    break
            if checked_word: checked_words.append(checked_word)
        checked_sentences.append(checked_words)
    checked_sentences = [s for s in checked_sentences if s]
    return checked_sentences
