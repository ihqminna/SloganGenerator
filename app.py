"""Main program."""

import src.trie
import sys

def main():
    """ Start the program: creates trie and then generates phrases."""
    print("Luodaanpas uusia lauseita!")
    length, degree = ask_for_parameters()
    print("Luodaan siis " + str(length) + " sanan pituisia lauseita asteella " + str(degree))
    trained_trie = trie.train_markov_chain(degree)
    generate_phrases(trained_trie, length, degree)

def ask_for_parameters():
    """Gets parameters from the user.

    Returns:
        length: length for the new phrases
        degree: degree for the Markov chain
    """
    degree = ask_for_value("Mitä astetta haluat käyttää?")
    length = ask_for_value("Entä monenko sanan pituisia lauseita?")
    return length, degree

def ask_for_value(question):
    """Asks user for a value.

    Args:
        question: question to be asked from the user before they input the value.

    returns:
        Value as an int.
    """
    print(question + " Jos haluat keskeyttää ohjelman, syötä x.")
    value = input()
    if value == "x":
        sys.exit()
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
        trained_trie: Trie structure
        length: length for the phrases to be generated
        degree: degree of the Markov chain
    """
    sentences = []
    for i in range(200):
        if len(sentences) == 10:
            main()
        phrase = ""
        sentence = trie.Trie.get_sentence(trained_trie, length, degree)
        if sentence:
            for w in sentence:
                phrase += " " + w
            sentences.append(phrase)
            print(phrase)
    text1 = "Antamillasi parametreille saatiin luotua "
    text2 = " lausetta. Kokeile pienempää astetta tai lauseen pituutta."
    print(text1 + str(len(sentences)) + text2)
    main()

if __name__ == "__main__":
    main()
