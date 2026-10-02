# Säähälytysjärjestelmä

## 1. Skriptin/ohjelman tarkoitus
Säähälytysjärjestelmä on Python-kielinen työkalu, joka tarkistaa reaaliaikaiset säätiedot (oletuksena Äänekoskelta) avoimen säärajapinnan kautta.

## 2. Järjestelmävaatimukset
* **Käyttöjärjestelmä:** Toimii yleisissä käyttöjärjestelmissä (Windows, macOS, Linux).
* **Python:** Edellyttää Python-tulkin asennusta (suositeltava versio 3.8 tai uudempi).
* **Ulkoinen kirjasto:** Ohjelma käyttää `requests`-kirjastoa HTTP-pyyntöjen tekemiseen. asenna etukäteen komentorivillä komennolla:
  ```bash
  pip install requests

  Käytetty tekoälyä apuna koodissa