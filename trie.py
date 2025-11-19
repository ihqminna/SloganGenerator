import re
import random

class Node:
    """Class for nodes in Trie."""

    def __init__(self):
        """Initializes new node."""
        self.children = {}
        self.frequency = 0

    def get_children(self):
        """Looks up for a word in Trie.
        Args:
            word = word to look for

        Returns:
            Children of a node.
        """
        current_node = self
        if not current_node.children:
            return None, None
        children_words = tuple()
        children_frequencies = tuple()
        for child in current_node.children:
            word = (child,)
            frequency = (current_node.children[child].frequency,)
            children_words += (word)
            children_frequencies += (frequency)
        return children_words, children_frequencies

class Trie:
    """Class for Trie structure."""

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
            current_node.frequency += 1

    def get_sentence(self, length, degree):
        sentence = ""
        current_node = self.root
        for i in range(length):
            children_words, children_frequencies = Node.get_children(current_node)
            word = random.choices(children_words, weights=children_frequencies, k=1)[0]
            sentence = sentence + " " + word
            current_node = current_node.children[word]
        return sentence
        
def create_trie(sentences, degree):
    """Creates a trie and saves sentences to it based on the degree as a parameter."""
    trained_trie = Trie()
    for s in sentences:
        i = 0
        while i < len(s) - degree:
            sentence_to_insert = []
            x = i
            while x <= degree + i:
                sentence_to_insert.append(s[x])
                x += 1
            Trie.insert_sentence(trained_trie, sentence_to_insert)
            i += 1
    return trained_trie
    """
    for child in trained_trie.root.children:
        children_words, children_frequencies = Node.get_children(trained_trie.root.children[child])
    for child in trained_trie.root.children:
        print(trained_trie.root.children[child])
        print(trained_trie.root.children[child].frequency)
        for grandchild in trained_trie.root.children[child].children:
            print(trained_trie.root.children[child].children[grandchild])
            print(trained_trie.root.children[grandchild].frequency)
    """

def train_markov_chain(length, degree):
    """Divide text into sentences and create a Markov chain based on them."""
    sentences = get_training_data()
    trie = create_trie(sentences, degree)
    for i in range(20):
        sentence = Trie.get_sentence(trie, length, degree)
        print(sentence)

def get_training_data():
    data = open("testidata.txt", "r", encoding="utf-8")
    raw_text = data.read()
    sentences = text_to_sentences(raw_text)
    data.close()
    return sentences

def text_to_sentences(text):
    """Split text into sentences and words."""
    text = text.lower()
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
