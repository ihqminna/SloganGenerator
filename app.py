import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    degree = input() #tarkista että validi
    print("Entä monenko sanan pituisia lauseita?")
    length = input() #tarkista että validi
    print("Luodaan siis " + length + " sanan pituisia lauseita asteella " + degree)
    slogan = trie.train_markov_chain(degree)
    #phrases = trie.generate_phrase(length)
    print(slogan)

def generate_phrase(length):
    slogan = trie.starts_with(length)
    return slogan
    
if __name__ == "__main__":
    main()
