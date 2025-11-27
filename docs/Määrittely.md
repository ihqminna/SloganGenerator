# Määrittelydokumentti

## Työn kuvaus

Työn tarkoituksena on toteuttaa tekstiä generoiva algoritmi. Sille syötetään tietyntyyppisiä tekstejä, joiden perusteella se pystyy luomaan uusia lauseita aiheeseen liittyen.

Tekstit ovat ympäristöaiheisiin liittyen ja algoritmi tuottaa niiden pohjalta ympäristöaiheisia lauseita. Todennäköisesti koulutusmateriaalia muuttamalla sloganeita voisi koostaa hyvinkin erilaisista lähteistä.

## Algoritmi

Tekstit luodaan Markovin ketju-algoritmin perusteella. Markovin ketju voi olla ensimmäisen tai useamman asteen malli, jossa kukin seuraava kirjain, sana tai muu sisältö määräytyy sitä välittömästi edeltävien sisältöjen perusteella.

Käyttäjä valitsee asteen, jolla ketju koulutetaan tietyn syvyiseksi Trie-puuksi. Ensimmäisen asteen Markovin ketjussa tallennetaan puu kahden sanan syvyisenä (yksittäisen juurisolmun lisäksi): kutakin sanaa seuraavat sanat ovat sen lapsisolmuja, joissa on ilmoitettu myös niiden esiintymistiheys harjoitusdatassa edeltävän sanan jälkeen. Kaikissa ketjuissa, eli n. asteen rakenteissa Trie-puun syvyys on yksittäisen juurisolmun lisäksi aina n+1. Näin voidaan tarkistaa sanoja generoidessa mitkä sanat voivat seurata tiettyä n-pituista sanajonoa.

Mallissa huomioidaan sanojen esiintymistiheydet, eli jos sana esiintyy usein tietyn sanan (1. aste) tai tiettyjen sanojen (2. tai enemmän asteita) jälkeen, se myös generoidaan useammin kyseisen sanan tai kyseisten sanojen jälkeen. Esiintymistiheydet tallennetaan Trie-puun solmuihin. Sanojen generoinnissa niitä hyödynnetään painotuksina satunnaisia sanoja valitessa.

## Taustani

Tekoälyn eettinen puoli kiinnostaa. Vaikka henkilökohtaisesti pyrin välttämään generatiivisen tekoälyn käyttöä sen resurssi-intensiivisyyden vuoksi, haluaisin oppia enemmän koneoppimisesta.

Koodaan ohjelman Pythonilla, pystyn vertaisarvioimaan Pythonin lisäksi Java-projekteja.

Opiskelen tietojenkäsittelytieteen kandidaatin tutkintoa n:ttä vuotta.
