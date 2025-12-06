"""Module for trie functions."""

import re
import random

class Node:
    """Class for nodes in Trie.

    Attributes:
        childen: children of the node
        frequency: how often does the node occur
    """

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
    """Class for Trie structure.

    Attributes:
        root: root-node of the structure
    """

    def __init__(self, sentences):
        """Initializes new Trie structure."""
        self.root = Node()
        self.sentences = sentences

    def insert_sentence(self, sentence):
        """Insert a sentence to trie.

        Args:
            sentence: sentence to be inserted
        """
        current_node = self.root
        for word in sentence:
            if word not in current_node.children:
                current_node.children[word] = Node()
            current_node = current_node.children[word]
            current_node.frequency += 1

    def get_sentence(self, length, degree):
        """Create a sentence from the trie.

        Args:
            length: length of the sentence
            degree: degree of the markov chain

        Returns:
            words: sentence created as a list        
        """
        current_node = self.root
        words = []
        nodes = []
        for i in range(degree+1):
            if len(words) == length:
                return words
            children_words, children_frequencies = Node.get_children(current_node)
            if not children_words:
                return None
            word = random.choices(children_words, weights=children_frequencies, k=1)[0]
            words.append(word)
            current_node = current_node.children[word]
            nodes.append(current_node)
        while len(words) < length:
            current_node = self.root
            context_words = words[-degree:]
            for w in context_words:
                if w not in current_node.children:
                    return None
                current_node = current_node.children[w]
            children_words, children_frequencies = Node.get_children(current_node)
            word = random.choices(children_words, weights=children_frequencies, k=1)[0]
            words.append(word)
        return words

    def sentences_in_training_data(self, sentences):
        """Method checks how many of the provided sentences occur as is in the training data.
        
        Args:
        takes the sentences as argument

        Returns:
        count of how many of the sentences occur as is in the training data
        """
        not_unique = 0
        for s in sentences:
            if Trie.in_training_data(self, s):
                not_unique += 1
        return not_unique

    def in_training_data(self, sentence):
        """Checks if a sentence occurs as is in the training data.
        
        Args:
        self: the trie structure
        sentence: sentence to be checked
        """
        p = len(sentence)
        for sent in self.sentences:
            if any(
                sent[i:i+p] == sentence
                for i in range(len(sent) - p + 1)
            ):
                return True
        return False

def create_trie(sentences, degree):
    """Creates a trie and saves sentences to it based on the degree as a parameter.
    
    Args:
        sentences: the training data for trie
        degree: the degree of the Markov chain

    Returns:
        trained_trie: the trie that was created from the sentences
    """
    trained_trie = Trie(sentences)
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

def train_markov_chain(degree):
    """Divide text into sentences and create a Markov chain based on them.
    
    Return:
        trie: return the trie structure created
    """
    sentences = get_training_data()
    trie = create_trie(sentences, degree)
    return trie

def get_training_data():
    """Read training data.
    
    Returns:
        sentences: the text split into words and sentences
    """
    with open("data/luontotekstit.txt", "r", encoding="utf-8") as data:
        raw_text = data.read()
    data.close()
    sentences = text_to_sentences(raw_text)
    return sentences

def text_to_sentences(text):
    """Split text into sentences and words.
    
    Args:
        text: the text to be split

    Returns:
        checked_sentences: text split into words and sentences
    """
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
            if checked_word:
                checked_words.append(checked_word)
        checked_sentences.append(checked_words)
    checked_sentences = [s for s in checked_sentences if s]
    return checked_sentences
