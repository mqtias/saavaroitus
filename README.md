# Säähälytysjärjestelmä

## 1. Skriptin/ohjelman tarkoitus
Säähälytysjärjestelmä on Python-kielinen työkalu, joka tarkistaa reaaliaikaiset säätiedot (oletuksena Äänekoskelta) avoimen säärajapinnan kautta. Ohjelma analysoi lämpötilan ja sateen todennäköisyyden sekä lähettää käyttäjälle ilmoituksen (esimerkiksi kehotuksen ottaa sateenvarjo mukaan tai pukeutua lämpimämmin), jotta ulos lähtiessä osaa varautua oikeilla vaatteilla ja varusteilla.

## 2. Järjestelmävaatimukset
* **Käyttöjärjestelmä:** Toimii kaikissa yleisissä käyttöjärjestelmissä (Windows, macOS, Linux).
* **Python:** Edellyttää Python-tulkin asennusta (suositeltava versio 3.8 tai uudempi).
* **Ulkoinen kirjasto:** Ohjelma käyttää `requests`-kirjastoa HTTP-pyyntöjen tekemiseen. Se on asennettava etukäteen komentoriviltä komennolla:
  ```bash
  pip install requests