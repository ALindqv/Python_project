import os
import pydoc

def main():
    print("Hei!")
    while True:
        uusi_lista = input("Tehdäänkö uusi lista (y/n)? ") #Kysytään haluaako tehdä uuden listan

        if uusi_lista == "y":
            lista_nimi = input("Anna listalle nimi")
            uusi_tiedosto = open(f"{lista_nimi}.txt","w") # Kirjoittaa uuden tiedoston
           
        elif uusi_lista == "n":
            jos_ei = input("Muokkaus vai poisto (m/p)? ")
            if jos_ei == "m":
                mita_muokataan = input("Mitä listaa muokataan? ")
                with open(f"{mita_muokataan}.txt", "a") as ostoslista: # Avaa olemassaolevan tiedoston ja lisää tekstiä
                    
                    # Silmukka kysyy käyttäjältä listaan lisättäviä tuotteita kunnes "v"
                    while True:
                        mita_lisataan = input("Mitä lisätään? ")
                        lisays = ostoslista.write(f"- {mita_lisataan} \n")
                        if mita_lisataan == "v": 
                            print("Lista valmis")
                            break
            elif jos_ei == "p":
                poisto = input("Mikä lista poistetaan? ")
                os.remove(f"{poisto}.txt") # Poistaa listan
def lisays():
    while True:
        lisataan = input("Lisää ostokset: ")
        ostoslista.write(f"- {lisataan}\n")
        if lisataan == "valmis":
            print("Lista tallennettu")
            break 


def lisataan_listaan():        
    uuteen_lisays = input("Lisätäänkö vai Poistetaanko listasta (L/P)? ")
    poisto = input("Mitkä tuotteet poistetaan? ")
        

        
            
                
    
main()