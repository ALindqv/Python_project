""" os moduuli tiedostojen käsittelyä varten """
import os
import pydoc


def lista_luonti(nimi, mode):
    """ Funktio, joka luo listatiedostoja """
    ostoslista = open(f"listat/{nimi}.txt", mode, encoding="utf-8") # Kirjoittaa uuden tiedoston                  
    return ostoslista # Palauttaa tiedoston muuttuja-arvona

def uusi():
    """ Uuden tyhjän listan luonti """
    lista_nimi = input("Nimeä lista: ")
    lista_luonti(lista_nimi, "w")


def lisays(ostoslista):
    """ Funktio tuotteiden lisäämiseen listatiedostoihin """            
    tuotteet = [] # Tyhjä lista tuotteita varten
    while True: # Silmukka kysyy käyttäjältä listaan lisättäviä tuotteita
        tuote = input("Lisättävä tuote: ")

        # Ohjelman lopettaminen inputilla
        if tuote == "v":
            print("Lista valmis")
            break

        # Lisää käyttäjän syötteen listaan
        tuotteet.append(tuote)
        #print(tuotteet)
    if tuote == "":
        ostoslista.write("\n")
    else:
        for tuote in tuotteet: 
            ostoslista.write(f"{tuote}\n") # For loop kirjoittaa käyttäjän merkkijonot listatiedostoon

def listasta_poisto(lista):
    """ Funktio listan sisällön poistamiseen """
    while len(lista) > 0:
        poistettava_tuote = input("Mitkä tuotteet poistetaan? kirjoita 'v' kun valmista: ")
        poistettavat_tuotteet = [tuote.strip() for tuote in poistettava_tuote.split(",")]
                
        poistettavien_maara = 0
        
        if poistettava_tuote == "v":
            print("Lista valmis")
            break

        for tuote in poistettavat_tuotteet:
            if tuote in lista:
                lista.remove(tuote)
                print(f"{tuote} poistettu.")
                poistettavien_maara += 1
            else:
                print(f"{tuote} ei löytynyt listalta.")

            if poistettavien_maara > 0:
                print(f"Ostoslista on nyt: {lista}")
            else:
                print("Mitään tuotteita ei poistettu.")


def listan_poisto(ostoslista):
    """ Listatiedostojen poistaminen """
    os.remove(f"listat/{ostoslista}.txt") # Poistaa listan



def main():
    """ Pääohjelma """
    while True:
        polku = "./listat"

        if os.listdir(polku) == []:
            luodaanko = input("Ei tiedostoja, luodaanko uusi (y/n)? ") # Tiedostoja ei löytynyt hakemistosta

            if luodaanko == "y":
                uusi()

            elif luodaanko == "n":
                print("Lopetetaan")
                break

            else:
                print("Sopimaton arvo, kokeile y tai n")
                continue

        else:
            uusi_lista = input("Uusi vai vanha lista (u/v)? ") # Kysytään halutaanko tehdä uusi lista vai käyttää vanhaa, jos hakemisto ei ole tyhjä

            # Uuden listan luonti
            if uusi_lista == "u":
                lista_nimi = input("Nimeä lista: ")
            
                lista = lista_luonti(lista_nimi, "w") # Tallennetaan lista_kirjoitus-funktion paluuarvo muuttujaan 
                
                muokataanko = input("Haluatko muokata listaa (y/n)? ") 
                if muokataanko == "y":
                    lisays(lista) # Käytetään aikaisempaa muuttujaa parametrinä muokkaus-funktiolle
                elif muokataanko == "n":
                    print("Tyhjä lista tallennettu")
                lista.close() # Suljetaan tiedosto, että ohjelma voi tallentaa muokkaukset
            
            # Olemassaolevan listan käsittely
            elif uusi_lista == "v":

                # Listataan olemassaolevat listatiedostot 
                print("Tiedostot:")
                for tiedosto in os.listdir(polku):
                    print(f"- {tiedosto}")
                
                valitse_lista = input("Valitse lista: ")
                olemassa = input("Listan muokkaus vai poisto (m/p)? ")
                
                # Muokkaus
                if olemassa == "m":
                    
                    
                    lista = lista_luonti(valitse_lista, "a") # Tallennetaan lista_kirjoitus-funktion paluuarvo muuttujaan
                    
                    lisays_poisto = input("Lisätäänkö listaan vai poistetaanko listasta (l/p)? ")
                    
                    if lisays_poisto == "l":
                        lisays(lista) # Kutsutaan funktiota muokkaus
                        lista.close()
                    
                    elif lisays_poisto == "p":
                        with open(f"listat/{valitse_lista}.txt","r",encoding="utf-8") as lista:
                            rivit = lista.readlines()
                            listan_tuotteet = [rivi.strip() for rivi in rivit if rivi.strip()] # Ostoslistassa olevat tuotteet
                            print(listan_tuotteet)
                            
                            if listan_tuotteet == []:
                                print("Tyhjä lista, kokeile uudelleen")
                                return
                            else:
                                for tuote in rivit:
                                    print(tuote.rstrip())

                                #print(poistettavat_tuotteet)

                            listasta_poisto(listan_tuotteet) # Kutsutaan poistofunktiota, parametrinä listan tuotteet

                            print(listan_tuotteet)
                        with open(f"listat/{valitse_lista}.txt", "w", encoding = 'utf-8') as lista:
                            for rivi in listan_tuotteet: 
                                lista.write(f"{rivi}\n") # For loop kirjoittaa käyttäjän merkkijonot listatiedostoon
                                
                        

                # Listatiedostojen poisto            
                elif olemassa == "p":
                    poistettava_lista = input("Mikä lista poistetaan? ")
                    print(f"{poistettava_lista} poistettu")
                    listan_poisto(poistettava_lista)

                # Sopimaton arvo
                else:
                    print("Sopimaton arvo, kokeile m tai p")
                    continue
            
            jatko = input("Jatketaanko (y/n)? ")

            if jatko == "y":
                continue
            elif jatko == "n":
                print("Lopetetaan")
                break

# Tekee PyDoc-dokumentaation projektista
pydoc.writedoc('ostoslista')

main()