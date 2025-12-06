# Pylint-raportti

## Tiedosto app.py

### Raportti

Module src.app
src\app.py:4:0: E0401: Unable to import 'trie' (import-error)
src\app.py:106:8: W0612: Unused variable 'i' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.12/10 (previous run: 9.12/10, +0.00)


### Kommentit

Muuttuja i on käytössä for-loopissa, jossa varmistetaan ettei ohjelma jää etsimään lauseita loputtomassa loopissa. En tiedä miksi pylint herjaa trie.py-tiedoston importista, tuonti kuitenkin toimii. 

## Tiedosto trie.py

### Raportti

Module src.trie
src\trie.py:32:8: C0206: Consider iterating with .items() (consider-using-dict-items)
src\trie.py:6:0: R0903: Too few public methods (1/2) (too-few-public-methods)
src\trie.py:77:12: W0612: Unused variable 'i' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 9.72/10 (previous run: 9.63/10, +0.09)

### Kommentit

Node-luokka ei tarvitse enempää kuin yhden metodin, jotta saadaan solmun lapset haettua. I on käytössä for-loopissa.
