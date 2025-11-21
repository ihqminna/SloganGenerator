import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    length, degree = ask_for_parameters()
    print("Luodaan siis " + str(length) + " sanan pituisia lauseita asteella " + str(degree))
    trained_trie = trie.train_markov_chain(degree)
    phrases = generate_phrases(trained_trie, length, degree)

def ask_for_parameters():
    degree = ask_for_value("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    length = ask_for_value("Entä monenko sanan pituisia lauseita?")
    return length, degree

def ask_for_value(question):
    print(question)
    value = input()
    valid = value.isnumeric()
    while not valid:
        print("Syötäthän arvon kokonaislukuna")
        print(question)
        value = input()
        valid = value.isnumeric()
    return int(value)

def generate_phrases(trained_trie, length, degree):
    """Generates 10 or less phrases with 200 tries.
    
    Args:
        Trie structure, length for the phrases and degree of the trie.

    Returns:
        Sentences created with the Trie.
    """
    sentences = []
    for i in range(200):
        if len(sentences) == 10:
            return sentences
        phrase = ""
        sentence = trie.Trie.get_sentence(trained_trie, length, degree)
        if sentence:
            for w in sentence:
                phrase += " " + w
            sentences.append(phrase)
            print(phrase)
    return sentences
    
if __name__ == "__main__":
    main()
