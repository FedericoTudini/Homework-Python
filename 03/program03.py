# -*- coding: utf-8 -*-
"""
Si deve realizzare una raccolta dei personaggi della saga de il Trono di Spade, 
che sono salvati in formato json.
Si devono realizzare la classe Personaggio e la classe Casata, 
secondo i parametri come descritto di seguito.
Infine, si devono realizzare la funzioni leggi_catalogo_personaggi per leggere 
i dati dai file json, e che torna i due dizionari catalogo_personaggi e catalogo_casate, 
e due funzioni per ricavare le Casate che hanno prodotto faide 
e la famiglia allargata di un personaggio (vedi più sotto).

Gli attributi della classe Personaggio sono:
    -nome
    -soprannome
    -casata
    -attore_interprete*
    -vittime*
    -genitori*
    -fratelli*
    -partner*
    -uccisori*

Il costruttore della classe Personaggio deve inizializzare tutti gli attributi possibili, 
prendendoli come dizionario letto dal file json.
Se la voce del dizionario di un personaggio non ha qualche attributo di
quelli previsti nella classe, tale attributo viene inizializzato a None.
L'attributo casata è una lista di oggetti di tipo Casata.
Gli attributi con un asterisco sono liste di riferimenti ad altre
istanze di classe Personaggio, corrispondenti ai personaggi cui la voce
del dizionario fa riferimento.

NOTA: deve esistere una sola istanza di ciascun personaggio e di ciascuna casata,
ovvero quella che avete inserito nei due dizionari catalogo_personaggi e catalogo_casate
nella funzione leggi_catalogo_personaggi.

Inoltre, la classe Personaggio deve avere i seguenti metodi:
    -parentela, che prende in input un secondo Personaggio e ritorna il tipo
       di parentela che intercorre fra i due personaggi come stringa, ovvero:
       'figlio', 'genitore', 'fratello', 'nonno', 'zio', 'nipote figlio di fratello',
       'nipote figlio di figlio' oppure 'lontana'.
       Se i personaggi sono di una diversa casata ritorna la stringa "nessuna".
    -famiglia_allargata, che calcola e ritorna l'insieme dei personaggi che fanno
     parte della sua famiglia allargata ovvero hanno una parentela con lui o con
     il/la suo/a compagno/a

La classe Casata, deve avere l'attributo name di tipo stringa, e l'attributo
membri che deve contenere un set con i riferimenti a tutti i personaggi che le
appartengono. Inoltre deve avere il seguente metodp:
    -ammazzati_da(self, casata) che torna il numero di membri della casata self
     che sono stati uccisi da qualche membro dell'altra casata passata come argomento

Sulla base degli oggetti così definiti implementate infine le funzioni
- faide(catalogo_casate) che trova l'insieme di casate tra le quali sono avvenuti
  il maggior numero di morti totali (di cui almeno 1 per parte).
  La funzione torna la tupla (Casata1, numero di morti dalla Casata2, Casata2, numero di morti dalla Casata1), con
        Casata1 = il nome della casata che ha ucciso più  personaggi dell'altra casata (almeno 1)
        Casata2 = il nome della casata che ha ucciso meno personaggi dell'altra casata (almeno 1)
- dynasty(personaggi) che trova il personaggio con la più grande famiglia allargata
    La funzione torna la tripla (personaggio, numero di componenti, famiglia allargata)

ATTENZIONE: sono proibite altre librerie oltre quelle già incluse.

TIMEOUT: il timeout per ciascun test è di 0.5 secondi.

ATTENZIONE: assicuratevi di salvare questo programma in encoding UTF8 
(ad esempio editandolo in Spyder o Notepad++)

"""
""" json tipo di un personaggio:
      {
         "characterName":"Aerys II Targaryen",
         "houseName":"Targaryen",
         "characterImageThumb":"https://images-na.ssl-images-amazon.com/images/M/MV5BMWQzOWViN2ItNDZhOS00MmZlLTkxZTYtZDg5NGUwMGRmYWZjL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1._SX100_SY140_.jpg",
         "characterImageFull":"https://images-na.ssl-images-amazon.com/images/M/MV5BMWQzOWViN2ItNDZhOS00MmZlLTkxZTYtZDg5NGUwMGRmYWZjL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_.jpg",
         "characterLink":"/character/ch0541362/",
         "actorName":"David Rintoul",
         "actorLink":"/name/nm0727778/",
         "nickname":"The Mad King",
         "royal":true,
         "killed":[
            "Brandon Stark",
            "Rickard Stark"
         ],
         "servedBy":[
            "Arthur Dayne",
            "Jaime Lannister"
         ],
         "parentOf":[
            "Daenerys Targaryen",
            "Rhaegar Targaryen",
            "Viserys Targaryen"
         ],
         "siblings":[
            "Rhaella Targaryen"
         ],
         "marriedEngaged":"Rhaella Targaryen",
         "killedBy":"Jaime Lannister"
      }
"""

import json

class Casata():
    def __init__(self, name):
        self.name = name
        self.membri = set()
        

    def ammazzati_da(self, casata):
        n = 0
        for pers in self.membri:
            if pers.uccisori != None:
                for killer in pers.uccisori:
                    if killer in casata.membri:
                        n+=1
        return n
        
class Personaggio():
    def __init__(self, data, casata):
        
        self.data = data
        
        if type(data.get("houseName")) == list:
            ls = []
            for name in data.get("houseName"):
                    if name not in casata.keys():
                        casata[name] = Casata(name)
                    ls.append(casata[name])
            self.casata = ls
            for cas in self.casata:
                cas.membri.add(self)
                
        elif type(data.get("houseName")) == str:
            ls = []
            if data.get("houseName") not in casata:
                casata[data.get("houseName")] = Casata(data.get("houseName"))
            ls.append(casata[data.get("houseName")])
            self.casata = ls
            ls[0].membri.add(self)
        else:
            ls = []
            self.casata = []
        
        self.nome = data.get("characterName")
        self.soprannome = data.get("nickname")
        self.attore_interprete = data.get("actorName")
        self.genitori = data.get("parents")
        self.vittime = data.get("killed")
        self.fratelli = data.get("siblings")
        self.uccisori = data.get("killedBy")
        self.partner = data.get("marriedEngaged")
        self.figli = data.get("parentOf")

    def parentela(self, p):
        for c in self.casata:
            if p in c.membri:
                if p.fratelli != None :
                    if self in p.fratelli:
                        return "fratello"
                if p.genitori != None :
                    if self in p.genitori:
                        return "figlio"
                    for genitore in p.genitori:
                        if self.fratelli != None and genitore in self.fratelli:
                            return "nipote figlio di fratello"
                        if genitore.genitori != None and self in genitore.genitori:
                            return "nipote figlio di figlio"
                if self.genitori != None :
                    if p in self.genitori:
                        return "genitore"
                    for genitore in self.genitori:
                        if genitore.genitori != None and p in genitore.genitori:
                         return "nonno"
                        if genitore.fratelli != None and p in genitore.fratelli:
                            return "zio"
                return "lontana"
        
        return "nessuna"

    def famiglia_allargata(self):
        '''torna l'insieme di personaggi imparentati con self oppure con un* su* compagn*, compreso self'''
        
        ins = set()
        ins.add(self)
        for c in self.casata:
            for p in c.membri:
                if self.parentela(p) != "nessuna":
                    ins.add(p)
        if self.partner != None:
            for partner in self.partner:
                for c in partner.casata:
                    for p in c.membri:
                        if partner.parentela(p) != "nessuna":
                            ins.add(p)
        if self.figli != None:
            for x in self.figli:
                ins.add(x)
                
        return ins
    
#    Nella famiglia allargata vanno aggiunti figli fratelli e genitori del personaggio e dei partner
#        -famiglia_allargata, che calcola e ritorna l'insieme dei personaggi che fanno
#     parte della sua famiglia allargata ovvero hanno una parentela con lui o con
#     il/la suo/a compagno/a

def leggi_catalogo_personaggi(personaggi_file_json):
    '''Carica il file personaggi e torna un dizionario di oggetti: nome -> Personaggio '''
    with open("tgot.json") as personaggi_file_json:
        actors = json.load(personaggi_file_json)
    catalogo_personaggi = {}
    catalogo_casate = {}
            
    
    for x in actors.values():
        for diz in x:
            catalogo_personaggi[diz.get("characterName")] = Personaggio(diz, catalogo_casate)
    
    attr = {"actorName","killed","parents","killedBy","marriedEngaged","siblings","parentOf"}
    attr2 = ["killed", "killedBy", "marriedEngaged"]
    
    
    for obj in catalogo_personaggi.values():
        for x in attr:    

            if type(obj.data.get(x)) == list:
                for num in range(len(obj.data.get(x))):
                    if obj.data[x][num] in catalogo_personaggi.keys():
                        obj.data[x][num] = catalogo_personaggi[obj.data[x][num]]
                        
        for x in range(len(attr2)):
            if type(obj.data.get(attr2[x])) == str and obj.data.get(attr2[x]) in catalogo_personaggi.keys():
                ls = []
                if x == 0 and obj.data.get(attr2[x]) != None:
                    ls.append(catalogo_personaggi[obj.data.get(attr2[x])])
                    obj.vittime = ls
                elif x == 1 and obj.data.get(attr2[x]) != None:
                    ls.append(catalogo_personaggi[obj.data.get(attr2[x])])
                    obj.uccisori = ls
                elif x == 2 and obj.data.get(attr2[x]) != None:
                    ls.append(catalogo_personaggi[obj.data.get(attr2[x])])
                    obj.partner = ls

    return catalogo_personaggi, catalogo_casate
    

def faide(casate):
    '''trova tutte le coppie di casate che si sono ammazzate l'un l'altra il maggior numero di membri totali (con almeno 1 per parte)'''
    ins = set()
    
    for a in casate.keys():
        for b in casate.keys():
            if a != b:
                killedA = 0
                killedB = 0
                for p in casate[a].membri:
                    if p.vittime != None:
                        for x in p.vittime:
                            if x in casate[b].membri:
                                killedA+=1
                for p in casate[b].membri:
                    if p.vittime != None:
                        for x in p.vittime:
                            if x in casate[a].membri:
                                killedB+=1
                                
                if killedA >= 1 and killedB >= 1:
                    if killedA > killedB:
                        ins.add((casate[b],killedA,casate[a],killedB))
    return ins

#- faide(catalogo_casate) che trova l'insieme di casate tra le quali sono avvenuti
#  il maggior numero di morti totali (di cui almeno 1 per parte).
#  La funzione torna la tupla (Casata1, numero di morti dalla Casata2, Casata2, numero di morti dalla Casata1), con
#        Casata1 = il nome della casata che ha ucciso più  personaggi dell'altra casata (almeno 1)
#        Casata2 = il nome della casata che ha ucciso meno personaggi dell'altra casata (almeno 1)

def dynasty(personaggi):
    '''torna il personaggio con la massima famiglia allargata, la dimensione e la famiglia'''
    ins = set()
    k = (None,0)
    for x in personaggi.values():
        ins.add((x,len(x.famiglia_allargata())))
    for x in ins:
        if x[1] > k[1]:
            k = x
            
    
    
    return k + (k[0].famiglia_allargata(),)
        
        
