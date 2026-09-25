import requests
from error_handler import kasittele_virhe

def hae_saatiedot(kaupunki):
    url = f"https://wttr.in/{kaupunki}?format=j1"
    
    try:
        headers = {"User-Agent": "Saahaytysjarjestelma/1.0"}
        vastaus = requests.get(url, headers=headers, timeout=10)
        vastaus.raise_for_status()
        data = vastaus.json()

        nykyinen = data["current_condition"][0] 
        lampotila = float(nykyinen["temp_C"])
        kuvaus = nykyinen["weatherDesc"][0]["value"].lower()

        sade_prosentti = 10
        if "rain" in kuvaus or "sade" in kuvaus or "shower" in kuvaus:
            sade_prosentti = 80
        elif "cloud" in kuvaus or "pilvinen" in kuvaus:
            sade_prosentti = 30

        tulos = {
            "lampotila": lampotila,
            "sade_prosentti": sade_prosentti,
            "kuvaus": kuvaus
        }
        return tulos
        
    except requests.exceptions.RequestException as e:
        kasittele_virhe(e, "Verkkovirhe säätietoja haettaessa. Tarkista verkkoyhteys.")
        return None