""" os moduuli tiedostojen käsittelyä varten """
import os

"""  
- Parametreinä nimi (käsiteltävän listan nimi) ja käsittelyn mode
- Palauttaa arvon lista, jota käytetään 
"""
def lista_kasittely(nimi, mode):
    lista = open(f"listat/{nimi}.txt", mode, encoding="utf-8") # Kirjoittaa uuden tiedoston                  
    return lista # Palauttaa tiedoston muuttuja-arvona

def lista_luku(nimi):
    """ Lukee listan nimellä, joka on annettu parametrinä
        - Palauttaa tiedostosta luetut rivit sekä listatiedoston sisällön
    """
    lista = lista_kasittely(nimi, "r")
    rivit = lista.readlines()
    sisalto = [rivi.strip() for rivi in rivit if rivi.strip()] # Ostoslistassa olevat tuotteet
    return rivit, sisalto

""" Uuden tyhjän listan luonti 
- Saatuaan käyttäjältä listan nimen, ohjelma kutsuu annetulla nimellä
funktiota lista_kasittely
- Palauttaa funktiosta saamansa arvon
"""
def uusi_tyhja():
    nimi = input("Nimeä lista: ")
    lista = lista_kasittely(nimi, "w")
    print("Uusi lista luotu")
    return lista

""" 
Funktio tuotteiden lisäämiseen listatiedostoihin 
Ottaa vastaan listan nimen parametrinä ja käyttää sitä kirjoittamaan listan sisällön oikeaan listaan
"""
def lisays(ostoslista):
                
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

""" 
Funktio listan sisällön poistamiseen 
Ottaa vastaan listan nimen parametrinä ja suorittaa poiston
"""
def listasta_poisto(lista):
    
    while len(lista) > 0:
        poistettava_tuote = input("Mitkä tuotteet poistetaan? Kirjoita 'v' kun valmista: ")
        poistettavat_tuotteet = [tuote.strip() for tuote in poistettava_tuote.split(",")] # Muodostetaan lista poistettavista tuotteista ja poistetaan tulostuksesta välit
                
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

""" 
Listatiedostojen poistaminen 
- Ottaa vastaan listan nimen paramatrinä ja tiedosto poistetaan os-moduulilla
"""
def listan_poisto(ostoslista):
    os.remove(f"listat/{ostoslista}.txt") # Poistaa listan


"""
- Pääfunktio kutsuu tätä funktiota parametreillä tiedoston nimi ja hakemiston polku
- Tämä funktio suorittaa listojen muokkausoperaatiot
"""
def listan_muokkaus(nimi, polku):
    
    while nimi in os.listdir(polku):
        
        alaviiva = "\033[4m" # Tiedostojen nimet alaviivataan listauksessa
        normaali_teksti = "\033[0m" # Muuttaa tekstin takaisin normaaliksi alaviivattujen sanojen jälkeen
        olemassa = input("Listan muokkaus vai poisto (m/p)? ")

        # Muokkaus
        if olemassa == "m":
            
            
            nimi = nimi[:-4] # Tiedostotyyppi poistetaan nimestä käsittelyfunktiota varten

            lista = lista_kasittely(nimi, "a") # Tallennetaan lista_kirjoitus-funktion paluuarvo muuttujaan
            
            lisays_poisto = input("Lisätäänkö listaan vai poistetaanko listasta (l/p)? ")
            
            if lisays_poisto == "l":
                lisays(lista) # Kutsutaan funktiota lisays lista_kasittely-funktion paluuarvolla
                lista.close()
            
            elif lisays_poisto == "p":
                rivit, listan_sisalto = lista_luku(nimi) # Saadaan halutun listan sisältö ja rivit kutsumalla funktiota
                if len(listan_sisalto) == 0:
                    print("Tyhjä lista, kokeile uudelleen")
                    continue
                else:
                    for tuote in rivit:
                        print(f'{alaviiva}{tuote.strip()}{normaali_teksti}')
                print()

                listasta_poisto(listan_sisalto) # Kutsutaan poistofunktiota, parametrinä listan tuotteet

                print(listan_sisalto)
                with open(f"listat/{nimi}.txt", "w", encoding = 'utf-8') as lista:
                    for rivi in listan_sisalto: 
                        lista.write(f"{rivi}\n") # For loop kirjoittaa käyttäjän merkkijonot listatiedostoon

            else:
                print("Sopimaton arvo, kokeile l tai p")
                continue     
            
        # Listatiedostojen poisto            
        elif olemassa == "p":
            nimi = nimi[:-4]
            print(f"Lista {alaviiva}{nimi}{normaali_teksti} poistettu")
            listan_poisto(nimi)

        # Sopimaton arvo
        else:
            print("Sopimaton arvo, kokeile m tai p")
            continue

def main():
    polku = "./listat" # Listatiedostojen hakemisto

    if not os.path.exists(polku): # Luo hakemiston, jos sitä ei ole
        os.makedirs(polku) 

    # Ohjelma käynnistyy tähän haaraan, jos hakemisto on tyhjä
    while True:
        while len(os.listdir(polku)) == 0:
            luodaanko = input("Ei tiedostoja, luodaanko uusi (y/n)? ") # Tiedostoja ei löytynyt hakemistosta
                
            if luodaanko == "y":
                uusi_tyhja()

            elif luodaanko == "n":
                break

            else:
                print("Sopimaton arvo, kokeile y tai n")
                continue

        # Ohjelma käyttää tätä haaraa, jos tiedostoja on jo olemassa
        while len(os.listdir(polku)) > 0:
            uusi_tai_vanha = input("Uusi lista vai käytetäänkö vanhaa lista (u/v)? ") # Kysytään halutaanko tehdä uusi lista vai käyttää vanhaa, jos hakemisto ei ole tyhjä

            # Uuden listan luonti
            if uusi_tai_vanha == "u":
                lista = uusi_tyhja()
                
                muokataanko = input("Haluatko muokata listaa (y/n)? ") 
                if muokataanko == "y":
                    lisays(lista) # Käytetään aikaisempaa muuttujaa parametrinä muokkaus-funktiolle
                elif muokataanko == "n":
                    print("Tyhjä lista tallennettu")
                lista.close() # Suljetaan tiedosto, että ohjelma voi tallentaa muokkaukset
            
            # Olemassaolevan listan käsittely
            elif uusi_tai_vanha == "v":

                # Listataan olemassaolevat listatiedostot
                alaviiva = "\033[4m" # Tiedostojen nimet alaviivataan listauksessa
                normaali_teksti = "\033[0m" # Muuttaa tekstin takaisin normaaliksi alaviivattujen sanojen jälkeen
                print("Tiedostot:")
                for tiedosto in os.listdir(polku):
                    print('- '+f'{alaviiva}{tiedosto}{normaali_teksti}')
                print()
                
                valitse_lista = input("Valitse lista: ")
                valitse_lista += '.txt' # Tiedoston nimen loppuun lisätään tiedoston .txt, että ohjelma osaa etsiä sitä

                listan_muokkaus(valitse_lista, polku)
                
            
        jatko = input("Jatketaanko (y/n)? ")

        if jatko == "y":
            continue
        elif jatko == "n":
            print("Lopetetaan")
            break
main()