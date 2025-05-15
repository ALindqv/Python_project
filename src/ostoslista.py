import os
import pydoc

def main():
    print("Hei!")
    while True:
        uusi_lista = input("Uusi vai olemassaoleva lista (u/o)? ") #Kysytään haluaako tehdä uuden listan

        if uusi_lista == "u":
            lista_nimi = input("Anna listalle nimi")
            uusi_tiedosto = open(f"{lista_nimi}.txt","w") # Kirjoittaa uuden tiedoston
           
        elif uusi_lista == "o":
            jos_ei = input("Muokkaus vai poisto (m/p)? ")
            if jos_ei == "m":
                mita_muokataan = input("Mitä listaa muokataan? ")
                with open(f"{mita_muokataan}.txt", "a") as ostoslista: # Avaa olemassaolevan tiedoston ja lisää tekstiä
                    
                    # Silmukka kysyy käyttäjältä listaan lisättäviä tuotteita kunnes "v"
                    tuotteet = [] # Tyhjä lista tuotteita varten
                    while True:
                        tuote = input("Mitä lisätään? ")
                        if tuote == "v": 
                            print("Lista valmis")
                            break
                        tuotteet.append(tuote)
                        print(tuotteet)

                    for tuote in tuotteet:
                        ostoslista.write(f"- {tuote} \n")
                        
            elif jos_ei == "p":
                poistettava_lista = input("Mikä lista poistetaan? ")
                poisto(poistettava_lista)

def poisto(ostoslista):
    os.remove(f"{ostoslista}.txt") # Poistaa listan

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