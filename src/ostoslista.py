import os, pydoc

def main():
    print("Hei!")
    while True:
        uusi_lista = input("Uusi vai olemassaoleva lista (u/o)? ") # Kysytään halutaanko tehdä uuden listan

        # Uuden listan luonti
        if uusi_lista == "u":
            lista_nimi = input("Listan nimi: ")
            with open(f"listat/{lista_nimi}.txt","w", encoding="utf-8") as ostoslista: # Kirjoittaa uuden tiedoston
                
                
                muokkaus = input("Haluatko muokata listaa (y/n)? ")
                if muokkaus == "y":
                    lisays(ostoslista)
            ostoslista.close()
           
        # Olemassaolevan listan käsittely
        elif uusi_lista == "o":
            olemassa = input("Muokkaus vai poisto (m/p)? ")
            
            # Muokkaus
            if olemassa == "m":
                valitse_lista = input("Mitä listaa muokataan? ")
                with open(f"listat/{valitse_lista}.txt","a", encoding="utf-8") as ostoslista: # Avaa olemassaolevan tiedoston ja lisää tekstiä
                    lisays(ostoslista) # Kutsutaan funktiota lisays
                ostoslista.close()
            
            # Poisto            
            elif olemassa == "p":
                poistettava_lista = input("Mikä lista poistetaan? ")
                poisto(poistettava_lista)


# Funktio tuotteiden lisäämiseen listoihin
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
            print(tuotteet)
        for tuote in tuotteet:
            ostoslista.write(f"- {tuote} \n")

def poisto(ostoslista):
    os.remove(f"listat/{ostoslista}.txt") # Poistaa listan
         
main()