
'''
Created on 27.02.2020

@author: corat
'''
print("AdressbuchPY")
print("************")
personen=[]



def hauptmenu():
    print("""H A U P T M E N U
        1. Eintrag hinzufuegen
        2. Eintrag aendern
        3. Eintrag loeschen
        4. Eintraege anzeigen
        0. Beenden""")
    

    
def hinzu():
    print("Sie legen einen neuen Kontakt an!\n-----------------------------------\n")
    anrede = input("Anrede: ")
    name = input("Name: ")
    vorname = input("Vorname: ")
    straße = input("Straße: ")
    hausnummer = input("Hausnummer: ")
    plz = input("Postleitzahl: ")
    stadt = input("Stadt: ")
    telefon = input("Telefon: ")
    mobil = input("Mobil: ")
    email_priv = input("E-Mail privat: ")
    email_gesch = input("E-Mail geschäftlich: ")

    personen = {"Anrede": anrede,
             "Name" : name,
             "Vorname": vorname,
             "Strasse": straße,
             "Hausnummer": hausnummer,
             "PLZ": plz,
             "Stadt": stadt,
             "Telefonnummer": telefon,
             "Mobil" : mobil,           
             "Privat-E-Mail": email_priv,
             "Geschäftlich-E-Mail": email_gesch,
}
    print(len(personen))
    #with open("personen.txt","a") as datei:
    #    for person in personen:
    #        anrede = person[0]
    #        name = person[1]
    #        vorname = person[2]
    #        straße = person[3]
    #        hausnummer = person[4]
    #        plz = person[5]
    #        stadt = person[6]
    #        telefon = person[7]
    #        mobil = person[8]
    #        email_priv = person[9]
    #        email_gesch = person[10]
    # 
    datei=open("personen.csv","w")       
    datei.write(str(anrede)+";"+str(name)+";"+str(vorname)+";"+str(straße)+";"+str(hausnummer)+";"+str(plz)+";"+str(stadt)+";"+str(telefon)+";"+str(mobil)+";"+str(email_priv)+";"+str(email_gesch)+"\n")
    datei.close()

    print("---------------------------------------------")
    print("Erfolgreich hinzugefügt!")
    print("---------------------------------------------")


def aendern():
    print("Eintrag aendern")

def loeschen():
    return print("Eintrag loeschen")

def anzeigen():
    return print("Eintrag anzeigen")

def beenden():
    return print("Programm beenden")

hauptmenu()
auswahl=int(input("\nTreffen sie eine Auswahl:   "))
print(" ")

if auswahl==1:
    hinzu()
elif auswahl==2:
    aendern()
elif auswahl==3:
    loeschen()
elif auswahl==4:
    anzeigen()
elif auswahl==0:
    beenden()
else:
    print("\n Ungueltige Eingabe. Nochmal")