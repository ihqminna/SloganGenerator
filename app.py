import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    length, degree = ask_for_parameters()
    print("Luodaan siis " + str(length) + " sanan pituisia lauseita asteella " + str(degree))
    trained_trie = trie.train_markov_chain(degree)
    for i in range(20):
        sentence = trie.Trie.get_sentence(trained_trie, length, degree)
        print(sentence)
    #phrases = generate_phrases(length)

def ask_for_parameters():
    degree = ask_for_value("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    length = ask_for_value("Entä monenko sanan pituisia lauseita?")
    return degree, length

def ask_for_value(question):
    valid = False
    print(question)
    value = input()
    valid = value.isnumeric()
    while not valid:
        print("Syötäthän arvon kokonaislukuna")
        print(question)
        value = input()
        valid = value.isnumeric()
    return int(value)

def generate_phrases(length):
    pass
    
if __name__ == "__main__":
    main()
