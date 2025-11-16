import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    degree = input() #tarkista että validi
    print("Entä monenko sanan pituisia lauseita?")
    length = input() #tarkista että validi
    print("Luodaan siis " + length + " sanan pituisia lauseita asteella " + degree)
    trie.train_markov_chain(degree)
    #phrases = generate_phrases(length)

def generate_phrases(length):
    pass
    
if __name__ == "__main__":
    main()
