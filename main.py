from weather_module import hae_saatiedot
from notification_module import laheta_ilmoitus
from error_handler import kasittele_virhe

def main():
    kaupunki = "Äänekoski"
    print(f"Haetaan reaaliaikaisia säätietoja kohteelle: {kaupunki}...")
    
    try:
        saatiedot = hae_saatiedot(kaupunki)
        
        if saatiedot:
            lampotila = saatiedot.get("lampotila")
            sade_prosentti = saatiedot.get("sade_prosentti", 0)
            kuvaus = saatiedot.get("kuvaus", "")

            viesti = ""
            if "lumi" in kuvaus or (sade_prosentti > 70 and lampotila < 0):
                viesti = f"Pue tänään lämpimästi päälle! Lämpötila on {lampotila}°C ja luvassa on lunta."
            elif sade_prosentti >= 50:
                viesti = f"Ota tänään sateenvarjo mukaan; sääennuste: {kuvaus}, lämpötila {lampotila}°C."
            else:
                viesti = f"Sää näyttää hyvältä ({kuvaus})! Lämpötila on {lampotila}°C."
                
            laheta_ilmoitus(viesti)
        else:
            print("Säätietoja ei voitu noutaa.")
            
    except Exception as e:
        kasittele_virhe(e, "Virhe pääohjelman suorituksessa.")

if __name__ == "__main__":
    main()