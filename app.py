import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    degree_str = input() #tarkista että validi
    degree = int(degree_str)
    print("Entä monenko sanan pituisia lauseita?")
    length_str = input() #tarkista että validi
    length = int(length_str)
    print("Luodaan siis " + length_str + " sanan pituisia lauseita asteella " + degree_str)
    trie.train_markov_chain(length, degree)
    #phrases = generate_phrases(length)

def generate_phrases(length):
    pass
    
if __name__ == "__main__":
    main()
