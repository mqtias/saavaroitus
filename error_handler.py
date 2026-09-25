"""
Keskitetty virheenkäsittelyohjelma.
"""

import datetime

def kasittele_virhe(virhe, lisatieto=""):
    """Tallentaa virheen lokitiedostoon ja tulostaa sen käyttäjälle."""
    aikaleima = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    virhe_viesti = f"[{aikaleima}] VIRHE: {lisatieto} -> {str(virhe)}\n"
    
    print(virhe_viesti)
    
    try:
        with open("virheloki.txt", "a", encoding="utf-8") as loki:
            loki.write(virhe_viesti)
    except Exception as e:
        print(f"Virhelokiin kirjoittaminen epäonnistui: {e}")