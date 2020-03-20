"""
    Klasse Telefonbuch
        addNummer(nummer)^^
        getNummer(vorname, name)^^
        deleteNummer(nummer)
        getKontaktliste()
"""
import sqlite3 #'modul zum Ansprechen der SQLite-Datenbank'


class Telefonbuch:
    
    """Constructor zur Vorbereitung des Datenzugriffs"""
    def __init__(self): #übernimmt keine Argumente, leerer Konstruktor, der intern alles bereitstellt
        self.conn = sqlite3.connect('contacts.db')    #handle zur Datenbank "contacts"
        self.c = self.conn.cursor()         #cursor c übergibt die anfrage an die db


    """Destructor zum schließen(freigeben) der Datenbankverbindung"""
    def __exit__(self, *args):
        print('__exit__')
        self.connection.close()


    """ Fuegt der DB einen neuen Eintrag hinzu. """
    def addNummer(self,vorname,name,nummer):
        #Vorbedingung_setzen
        assert(isinstance(nummer,str))      #prüft ob einträge vom typ string sind,
        assert(isinstance(vorname,str))     #wenn nicht bricht das programm ab um fehler zu vermeiden
        assert(isinstance(name,str))        #Python typisiert Datentypen schwach bis gar nicht
        params = (vorname, name, nummer)    #Tupel, einfacher zum einbinden in die SQL-Anfrage
        sql = "INSERT INTO contacts VALUES (NULL,?,?,?)" #erster Eintrag is die ID und wird von der DB erstellt
        self.c.execute(sql,params)          #cursor c wird Tupel params übergeben
        self.conn.commit()         #damit Aenderungen in der DB ausgeführt werden, wird der Handler genutzt(commit)


    """Liefert Telefonnummen zu gegebenen Vorname und name"""
    def getNummer(self,vorname,name):   #gibt Liste der Telefonnummern aus
        #Vorbedingung_setzen
        assert(isinstance(name,str))      #prüft ob einträge vom typ string sind
        assert(isinstance(vorname,str))
        liste = []                          #benötigt um Tupels in Liste von Strings umzuwandeln
        params = (vorname,name)
        sql = "SELECT telefon FROM contacts WHERE vorname = ? AND name = ?"
        self.c.execute(sql,params)
        for row in self.c.fetchall():       #der einzelne Datensatz von self.c (Liste von tTupel) wird in Liste geschrieben
            liste.append(str(row[0]))


    """Löscht Datensatz zur angegebenen Telefonnummer"""
    def deleteNummer(self,nummer):
        #Vorbedingung_setzen
        assert(isinstance(nummer,str))
        params = (nummer,)                  #Tupel mit nur einem Eintrag muss mit komma geschrieben werden
        sql = "DELETE FROM contacts WHERE telefon = ?"
        self.c.execute(sql,params)
        self.conn.commit()          #wichtig damit die änderung in der DB datei geschrieben wird

