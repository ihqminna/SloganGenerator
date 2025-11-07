import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia sloganeita!")
    text = "Istuin puun alla ja mietiskelin. Moi, sanoi naapuri. Moi moi, sanoin minä."
    slogan = trie.train_markov_chain(text)
    #slogan = generate_slogan_with_word("moi")
    print(slogan)

def generate_random_slogan():
    pass

def generate_slogan_with_word(word):
    slogan = trie.starts_with(word)
    return slogan
    
if __name__ == "__main__":
    main()
