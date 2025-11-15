import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia lauseita! Mitä astetta haluat käyttää?")
    degree = input() #tarkista että validi
    print("Entä monenko sanan pituisia lauseita?")
    length = input() #tarkista että validi
    print("Luodaan siis " + length + "sanan pituisia lauseita asteella " + degree)
    text = "Istuin puun alla ja mietiskelin. Moi, ?? ##00sanoi fsf08098sas8 naapuri. Moi moi, sanoin minä."
    #slogan = trie.train_markov_chain(text, degree)
    #phrases = generate_phrases(length)
    #print(slogan)

def generate_phrases(length):
    slogan = trie.starts_with(length)
    return slogan
    
if __name__ == "__main__":
    main()
