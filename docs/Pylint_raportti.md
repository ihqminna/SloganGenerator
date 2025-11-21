# Pylint-raportti

## Tiedosto app.py

### Raportti

Module app
app.py:51:8: W0612: Unused variable 'i' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.74/10 (previous run: 9.44/10, +0.29)

### Kommentit

Muuttuja i on käytössä for-loopissa, jossa varmistetaan ettei ohjelma jää etsimään lauseita loputtomassa loopissa.

## Tiedosto trie.py

### Raportti

Module trie
trie.py:32:8: C0206: Consider iterating with .items() (consider-using-dict-items)
trie.py:6:0: R0903: Too few public methods (1/2) (too-few-public-methods)
trie.py:76:12: W0612: Unused variable 'i' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.68/10 (previous run: 9.46/10, +0.22)

### Kommentit

Node-luokka ei tarvitse enempää kuin yhden metodin, jotta saadaan solmun lapset haettua. I on käytössä for-loopissa.
