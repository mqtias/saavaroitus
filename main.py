from weather_module import hae_saatiedot
from notification_module import laheta_ilmoitus
from error_handler import kasittele_virhe

def main():
    syotetty_kaupunki = input("Minkä paikkakunnan sään haluat? (Paina Enter käyttääksesi oletusta): ").strip()
    
    if not syotetty_kaupunki:
        kaupunki = "Äänekoski"
        print(f"Ei paikkakuntaa annettu. Haetaan oletuksena säätietoja kohteelle: {kaupunki}...")
    else:
        kaupunki = syotetty_kaupunki
        print(f"Haetaan säätietoja kohteelle: {kaupunki}...")
    
    try:
        saatiedot = hae_saatiedot(kaupunki)
        
        if not saatiedot and kaupunki != "Äänekoski":
            print(f"Paikkakunnalta '{kaupunki}' ei löytynyt säätietoja. Haetaan sen sijaan oletus...")
            kaupunki = "Äänekoski"
            saatiedot = hae_saatiedot(kaupunki)
        
        if saatiedot:
            lampotila = saatiedot.get("lampotila")
            sade_prosentti = saatiedot.get("sade_prosentti", 0)
            kuvaus = saatiedot.get("kuvaus", "")

            viesti = ""
            if "lumi" in kuvaus or (sade_prosentti > 70 and lampotila < 0):
                viesti = f"ON kylmä! Lämpötila kohteessa {kaupunki} on {lampotila}°C ja luvassa on lunta."
            elif sade_prosentti >= 50:
                viesti = f"Tulet todennäköisesti kastumaan ({kaupunki}); sääennuste: {kuvaus}, lämpötila {lampotila}°C."
            else:
                viesti = f"Sää vaikuttaa hyvälle kohteessa {kaupunki} ({kuvaus})! Lämpötila on {lampotila}°C."
                
            laheta_ilmoitus(viesti)
        else:
            print("Säätietoja ei voitu hakea mistään.")
            
    except Exception as e:
        kasittele_virhe(e, "Virhe pääohjelman suorituksessa.")

if __name__ == "__main__":
    main()