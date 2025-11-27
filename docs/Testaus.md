# Testaus

## Yksikkötestauksen kattavuusraportti:

Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
src\__init__.py              0      0      0      0   100%
src\tests\__init__.py        0      0      0      0   100%
src\tests\app_test.py        3      0      0      0   100%
src\tests\trie_test.py      36      0      0      0   100%
src\trie.py                 95      0     36      0   100%
--------------------------------------------------------------------
TOTAL                      134      0     36      0   100%

![Coverage report](coverage_report.png)

Kurssimateriaalista:
- Mitä on testattu, miten tämä tehtiin?
- Minkälaisilla syötteillä testaus tehtiin?
- Miten testit voidaan toistaa?
- Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)
- Ei siis riitä todeta, että testaus on tehty käyttäen automaattisia yksikkötestejä, vaan tarvitaan konkreettista tietoa testeistä, kuten:
    - Testattu, että tekoäly osaa tehdä oikeat siirrot tilanteessa, jossa on varma 4 siirron voitto. Todettu, että siirroille palautuu voittoarvo 100000.
    - Testattu 10 kertaan satunnaisesti valituilla lähtö- ja maalipisteillä, että JPS löytää saman pituisen reitin kuin Dijkstran algoritmi.
    - Kummallakin algoritmilla on pakattu 8 MB tekstitiedosto, purettu se ja tarkastettu, että tuloksena on täsmälleen alkuperäinen tiedosto.