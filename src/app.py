"""Main program."""

import sys
import trie

def main():
    """ Start the program: creates trie and then generates phrases."""
    print("Luodaanpas uusia lauseita!")
    length, degree = ask_for_parameters()
    print("Luodaan Markovin ketju asteella " + str(degree) + ".")
    trained_trie = trie.train_markov_chain(degree)
    use_trie(trained_trie, length, degree)

def use_trie(trained_trie, length, degree):
    """Generates sentences based on a ready trie structure.
    
    Args:
    trained trie: the ready trie structure
    length: length of the sentences to be creates
    degree: degree of the markov chain
    """
    generate = True
    while generate:
        print("Luodaan " + str(length) + " sanan pituisia lauseita Markovin ketjulla.")
        sentences = generate_phrases(trained_trie, length, degree)
        print_sentences(sentences)
        print("Haluatko luoda uuden mallin tai tarkistaa moniko lause on uniikki?")
        print("Syötä m jos haluat luoda uuden mallin.")
        print("Syötä t jos haluat tarkistaa lauseiden esiintymisen sellaisenaan harjoitusdatassa.")
        print("Syötä x keskeyttääksesi ohjelman.")
        print("Syötä mitä tahansa muuta luodaksesi lisää lauseita mallilla.")
        value = input()
        if value == "t":
            check_uniques(trained_trie, sentences)
        elif value == "m":
            generate = False
        elif value == "x":
            sys.exit()
    main()

def check_uniques(trained_trie, sentences):
    """Checks if the created sentences are unique, or if they occur as is in the training set.

    Args:
    trained trie: the trie structure
    sentences: created sentences
    """
    not_unique = trie.Trie.sentences_in_training_data(trained_trie, sentences)
    total = len(sentences)
    txt = " lauseesta harjoitusdatassa esiintyy täysin samana "
    print("Yhteensä " + str(total) + txt + str(not_unique) + " lausetta.")

def ask_for_parameters():
    """Gets parameters from the user.

    Returns:
        length: length for the new phrases
        degree: degree for the Markov chain
    """
    degree = ask_for_value("Mitä astetta haluat käyttää?")
    length = ask_for_value("Entä monenko sanan pituisia lauseita?")
    return length, degree

def print_sentences(sentences):
    """Prints out a list of sentences.
    
    Args:
    sentences: sentences to be printed
    """
    for s in sentences:
        sentence = ""
        for w in s:
            sentence += w + " "
        print(sentence)

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
        valid = value.isnumeric() and value > 0
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
            return sentences
        sentence = trie.Trie.get_sentence(trained_trie, length, degree)
        if sentence:
            sentences.append(sentence)
    text1 = "Antamillasi parametreille saatiin luotua vain "
    text2 = " lausetta 200 yrityksellä. Kokeile pienempää astetta tai lauseen pituutta."
    print(text1 + str(len(sentences)) + text2)
    return sentences

if __name__ == "__main__":
    main()
