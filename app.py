import trie

"""Explanation + Args + Returns + Attributes"""

def main():
    print("Luodaanpas uusia sloganeita!")
    text = "Istuin puun alla ja mietiskelin. Moi, sanoi naapuri. Moi moi, sanoin minä."
    slogan = train_markov_chain(text)
    #slogan = generate_slogan_with_word("moi")
    print(slogan)

def train_markov_chain(text):
    """Divide text into sentences and create a Markov chain based on them."""
    sentence = []
    sentences = []
    word = ""
    for c in text:
        if c == ".":
            if word.strip():
                sentence.append(word)
            word = ""
            #trie.insert(sentence)
            sentences.append(sentence)
            sentence = []
        elif c == " ":
            if word.strip():
                sentence.append(word)
            word = ""
        elif c.isalpha() or c == "ä" or c =="ö":
            word = word + c
    return sentences

def generate_random_slogan():
    pass

def generate_slogan_with_word(word):
    slogan = trie.starts_with(word)
    return slogan
    
if __name__ == "__main__":
    main()
