import copy
import unittest, pytest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

from program03 import Casata, Personaggio, leggi_catalogo_personaggi, faide, dynasty

@ddt
class Test(testlib.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Carico i file per avere pezzi di json a disposizione'''
        with open('tgot.json', encoding='utf8') as f:
            cls.tgot_data = json.load(f)
        cls.personaggi = None
        cls.casate = None

################################################################################

    @data(
        ['tgot.json',     381, 13],
    )
    @unpack
    @pytest.mark.t01
    @pytest.mark.t11
    @pytest.mark.t12
    def test_01_load_personaggi(self, filename, NP, NC):
        '''controlla che vengano caricati i Personaggi e le Casate'''
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            res = leggi_catalogo_personaggi(filename)
        self.assertEqual(type(res),       tuple,  "il risultato non è una tupla")
        self.assertEqual(len(res),        2,      "il risultato non ha due elementi")
        personaggi, casate = res
        self.assertEqual(type(personaggi), dict,   "Il catalogo_casata non è un dizionario")
        self.assertEqual(len(personaggi),  NP,     f"Il dizionario creato da {filename} deve contenere {NP} personaggi")
        self.assertEqual(type(casate),     dict,   "Il catalogo_registi non è un dizionario")
        self.assertEqual(len(casate),      NC,     f"Il catalogo_registi creato da {filename} deve contenere {NC} casate")
        for p in personaggi.values():
            self.assertEqual(type(p),      Personaggio, "Tutti i valori di catalogo_personaggi devono essere Personaggi")
        for c in casate.values():
            self.assertEqual(type(c),      Casata, "Tutti i valori di catalogo_casate devono essere Casate")
        Test.personaggi = personaggi
        Test.casate     = casate

        # TODO: controllo su almeno un paio di attori, casata e registi

################################################################################

    def do_test_Personaggio_dati_base(self, personaggio, c, nome, soprannome, casata):
        '''Verifica che il personaggio contenga i dati base'''
        self.assertEqual(type(personaggio),      Personaggio,     "Non è una istanza di Personaggio")
        self.assertEqual(personaggio.nome,       nome,       f"Il nome del personaggio non è {nome}")
        self.assertEqual(personaggio.soprannome, soprannome, f"Il soprannome del personaggio non è {soprannome}")
        self.assertEqual(type(personaggio.casata),     list, f"L'attributo casata del personaggio non è di tipo lista")
        if len(casata) >0:
            self.assertEqual(type(personaggio.casata[0]), Casata,f"Gli elementi dell'attributo casata del personaggio non sono istanze di Casata")
            self.assertEqual(personaggio.casata[0].name, casata[0],f"Gli elementi dell'attributo casata del personaggio non sono istanze di Casata")
            self.assertTrue(casata[0] in c, f"Casata non creata in gruppo casate")

    @data(
        # raw_data
        # nome                   soprannome                casata
        [{
         "characterName":"Jeor Mormont",
         "houseName":"Mormont",
         "characterImageThumb":"https://images-na.ssl-images-amazon.com/images/M/MV5BODAwODYyNzk0NV5BMl5BanBnXkFtZTcwNDI2NDk4OQ@@._V1._SX100_SY140_.jpg",
         "characterImageFull":"https://images-na.ssl-images-amazon.com/images/M/MV5BODAwODYyNzk0NV5BMl5BanBnXkFtZTcwNDI2NDk4OQ@@._V1_.jpg",
         "characterLink":"/character/ch0251492/",
         "actorName":"James Cosmo",
         "actorLink":"/name/nm0181920/",
         "killedBy":"Rast"
      }, 'Jeor Mormont',     None,    ['Mormont']                ],
        [{
         "characterName":"Tytos Lannister",
         "houseName":"Lannister",
         "parentOf":[
            "Tywin Lannister",
            "Kevan Lannister"
         ],
         "marriedEngaged":"Jeyne Lannister"
      },'Tytos Lannister',     None,    ['Lannister']                ],
        [{"characterName":"Sandor Clegane",
         "characterImageThumb":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwMjEwNDQ1MF5BMl5BanBnXkFtZTcwMzAxODg4OQ@@._V1._SX100_SY140_.jpg",
         "characterImageFull":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwMjEwNDQ1MF5BMl5BanBnXkFtZTcwMzAxODg4OQ@@._V1_.jpg",
         "characterLink":"/character/ch0162882/",
         "actorName":"Rory McCann",
         "actorLink":"/name/nm0564920/",
         "nickname":"The Hound",
         "killed":[
            "Mycah",
            "Kings Landing Rioter #1",
            "Kings Landing Rioter #2",
            "Kings Landing Rioter #3",
            "Beric Dondarrion",
            "Frey Soldier #2",
            "Lowell",
            "Dying Man",
            "Biter",
            "Steve",
            "Riddell",
            "Gatins",
            "Morgan",
            "Lem Lemoncloak"
         ]
      },'Sandor Clegane',     'The Hound',    []               ],
        [{"characterName":"Margaery Tyrell",
         "houseName":"Tyrell",
         "characterImageThumb":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzODQ1MDg3NV5BMl5BanBnXkFtZTcwODA4NDk4OQ@@._V1._SX100_SY140_.jpg",
         "characterImageFull":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzODQ1MDg3NV5BMl5BanBnXkFtZTcwODA4NDk4OQ@@._V1_.jpg",
         "characterLink":"/character/ch0251974/",
         "actorName":"Natalie Dormer",
         "actorLink":"/name/nm1754059/",
         "marriedEngaged":[
            "Renly Baratheon",
            "Joffrey Baratheon",
            "Tommen Baratheon"
         ],
         "killedBy":"Cersei Lannister"
      }, 'Margaery Tyrell',     None,    ['Tyrell']                ],
        [{"characterName":"Jaime Lannister",
         "houseName":"Lannister",
         "characterImageThumb":"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIzMzU1NjM1MF5BMl5BanBnXkFtZTcwMzIxODg4OQ@@._V1._SX100_SY140_.jpg",
         "characterImageFull":"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIzMzU1NjM1MF5BMl5BanBnXkFtZTcwMzIxODg4OQ@@._V1_.jpg",
         "characterLink":"/character/ch0158527/",
         "actorName":"Nikolaj Coster-Waldau",
         "actorLink":"/name/nm0182666/",
         "nickname":"The Kingslayer",
         "kingsguard":"True",
         "parents":[
             "Tywin Lannister",
             "Joanna Lannister"
         ],
         "parentOf":[
            "Joffrey Baratheon",
            "Myrcella Baratheon",
            "Tommen Baratheon"
         ],
         "guardianOf":[
            "Aerys II Targaryen",
            "Robert Baratheon",
            "Joffrey Baratheon"
         ],
         "killed":[
            "Aerys II Targaryen",
            "Jory Cassel",
            "Alton Lannister",
            "Torrhen Karstark",
            "Olenna Tyrell"
         ],
         "siblings":[
            "Cersei Lannister",
            "Tyrion Lannister"
         ]
      }, 'Jaime Lannister',     "The Kingslayer",    ['Lannister']                ],
    )
    @unpack
    @pytest.mark.t10
    def test_10_new_Personaggio(self, raw_data, nome, soprannome, casata):
        '''Controlla che il personaggio venga creato correttamente da un blocco di dati json'''
        c={}
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            personaggio = Personaggio(raw_data,c)
        self.do_test_Personaggio_dati_base(personaggio, c, nome, soprannome, casata)

################################################################################

    @data(
            # nome                   soprannome                casata
        ["Wyllis", "Wyllis", None, []],
        ["Brynden Tully","Brynden Tully","Blackfish",["Tully"]],
        ["Myrcella Baratheon","Myrcella Baratheon",None,["Baratheon"]],
        ["Cersei Lannister","Cersei Lannister",None,["Lannister", "Baratheon"] ],
        ["Brienne of Tarth","Brienne of Tarth",None,[]]

    )
    @unpack
    @pytest.mark.t11
    def test_11_Personaggio_from_catalogo_personaggi(self, nome, nome2, soprannome, casata):
        '''Controlla che il personaggio sia stato creato correttamente dal caricamento del file'''
        self.assertTrue(nome in self.personaggi, f"Il personaggio {nome} deve apparire nel catalogo_personaggi")
        personaggio = self.personaggi[nome]
        self.do_test_Personaggio_dati_base(personaggio, self.casate, nome, soprannome, casata)
        for c in personaggio.casata:
            self.assertTrue(type(personaggio.casata)==list, f"La casata deve essere inserita in una lista")
            self.assertEqual(type(c), Casata, f"La casata deve essere di tipo Casata")
            self.assertTrue(c.name in self.casate, f"La casata {c} del personaggio deve essere presente in catalogo_casate")
            self.assertTrue(c is self.casate[c.name], f"La casata {c} del personaggio deve essere presente in catalogo_casate")
            self.assertTrue(personaggio in c.membri, f"Il personaggio deve essere un membro della casata {c}")

    @data(
        # casata, membri
       ["Mormont",['Lyanna Mormont', 'Jeor Mormont', 'Jorah Mormont']],
       ["Targaryen",['Aerys II Targaryen', 'Rhaegal', 'Unknown Targaryen Queen', 'Rhaegar Targaryen', 'Drogon', 'Jon Snow', 'Viserys Targaryen', 'Rhaella Targaryen', 'Aegon Targaryen', 'Daenerys Targaryen', 'Rhaenys Targaryen', 'Viserion', 'Aegon V Targaryen', 'Maester Aemon']],
       ["Stark",['Ghost', 'Lyanna Stark', 'Lady', 'Sansa Stark', 'Arya Stark', 'Young Benjen Stark', 'Benjen Stark', 'Jon Snow', 'Young Lyanna Stark', 'Shaggydog', 'Young Ned', 'Grey Wind', 'Lyarra Stark', 'Young Ned Stark', 'Nymeria', 'Brandon Stark', 'Eddard Stark', 'Bran Stark', 'Rickard Stark', 'Rickon Stark', 'Robb Stark', 'Summer', 'Catelyn Stark']]
       )
    @unpack
    @pytest.mark.t12
    def test_12_Membri_casate(self, nome, membri):
        ''' Controlla che le casate abbiano tutti i membri previsti'''
        self.assertTrue(nome in self.casate, f"La casata {nome} deve apparire nel catalogo_casate")
        casata = self.casate[nome]
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            self.assertTrue(type(casata)==Casata, f"La casata deve essere di tipo Casata")
            self.assertTrue(all([type(c)==Personaggio for c in casata.membri]), f"Tutti i membri di una casata devono essere di tipo Personaggio")
            self.assertTrue(all([c.nome in membri for c in casata.membri ]), f"Tutti i Personaggi del catalogo_casate devono essere nella stessa Casata")
            self.assertTrue(all([m in [c.nome for c in casata.membri] for m in membri]),f"Tutti i membri di una casata devono essere nel catalogo_casate")

    @data(
        # nome, figli, genitori, fratelli, partner, uccisori, vittime
        ["Arya Stark",None,['Eddard Stark', 'Catelyn Stark'],['Robb Stark', 'Sansa Stark', 'Bran Stark', 'Rickon Stark'],None,None,['Red Keep Stableboy', 'Polliver', 'Rorge', 'Meryn Trant', 'The Waif', 'Black Walder Rivers', 'Lothar Frey', 'Walder Frey', 'Petyr Baelish']],
        ["Brandon Stark",None,['Rickard Stark', 'Lyarra Stark'],['Lyanna Stark', 'Benjen Stark', 'Eddard Stark'],['Catelyn Stark'],['Aerys II Targaryen'],None],
        ["Cassana Baratheon",['Renly Baratheon', 'Robert Baratheon', 'Stannis Baratheon'],None,None,['Steffon Baratheon'],None,None],
        ["Dorna Lannister",['Lancel Lannister', 'Martyn Lannister', 'Willem Lannister'],None,None,['Kevan Lannister'],None,None],
        ["Kevan Lannister",['Lancel Lannister', 'Martyn Lannister', 'Willem Lannister'],["Jeyne Lannister","Tytos Lannister"],['Tywin Lannister'],['Dorna Lannister'],['Cersei Lannister'],None],
        ["Nymeria",None,None,['Grey Wind', 'Lady', 'Summer', 'Shaggydog', 'Ghost'],None,None,None],
        ["Selyse Baratheon",['Shireen Baratheon'],None,None,['Stannis Baratheon'],['Selyse Baratheon'],['Selyse Baratheon']],
        ["Sansa Stark",None,['Eddard Stark', 'Catelyn Stark'],['Robb Stark', 'Arya Stark', 'Bran Stark', 'Rickon Stark'],['Joffrey Baratheon', 'Tyrion Lannister', 'Ramsay Snow'],None,None]
    )
    @unpack
    @pytest.mark.t12
    def test_13_Personaggio_attributi_lista(self, nome, figli, genitori, fratelli, partner, uccisori, vittime):
        '''Controlla che i personaggi abbiano tutti i link relazionali'''
        self.assertTrue(nome in self.personaggi, f"Il personaggio {nome} deve apparire nel catalogo_personaggi")
        personaggio = self.personaggi[nome]
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            if personaggio.figli:
                for f in personaggio.figli:
                    self.assertTrue(type(f)==Personaggio, f"Gli elementi associati devono essere di tipo Personaggio")
                    fp = self.personaggi[f.nome]
                    self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                    self.assertTrue(f.nome in figli,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.figli] for m in figli]),f"Tutti i figli del personaggio {nome} devono essere nell'attributo di quel Personaggio")
            if personaggio.genitori:
                for f in personaggio.genitori:
                    self.assertTrue(type(f)==Personaggio, f"Gli elementi associati devono essere di tipo Personaggio")
                    fp = self.personaggi[f.nome]
                    self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                    self.assertTrue(f.nome in genitori,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.genitori] for m in genitori]),f"Tutti i genitori  del personaggio {nome} devono essere nell'attributo di quel Personaggio")
            if personaggio.fratelli:
                for f in personaggio.fratelli:
                    self.assertTrue(type(f)==Personaggio, f"Gli elementi associati devono essere di tipo Personaggio")
                    fp = self.personaggi[f.nome]
                    self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                    self.assertTrue(f.nome in fratelli,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.fratelli] for m in fratelli]),f"Tutti i fratelli del personaggio {nome} devono essere nell'attributo di quel Personaggio")
            if personaggio.partner:
                for f in personaggio.partner:
                    self.assertTrue(type(f)==Personaggio, f"Gli elementi associati devono essere di tipo Personaggio")
                    fp = self.personaggi[f.nome]
                    self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                    self.assertTrue(f.nome in partner,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.partner] for m in partner]),f"Tutti i partner del personaggio {nome} devono essere nell'attributo di quel Personaggio")
            if personaggio.uccisori:
                for f in personaggio.uccisori:
                    self.assertTrue(type(f) in [Personaggio,str], f"Gli elementi associati devono essere di tipo Personaggio")
                    if type(f) == Personaggio:
                        fp = self.personaggi[f.nome]
                        self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                        self.assertTrue(f.nome in uccisori,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.uccisori if type(f)==Personaggio] for m in uccisori]),f"Tutti i uccisori del personaggio {nome} devono essere nell'attributo di quel Personaggio")
            if personaggio.vittime:
                for f in personaggio.vittime:
                    self.assertTrue(type(f) in [Personaggio,str], f"Gli elementi associati devono essere di tipo Personaggio")
                    if type(f) == Personaggio:
                        fp = self.personaggi[f.nome]
                        self.assertTrue(fp is f, f"I personaggi devono essere nel catalogo_personaggi")
                        self.assertTrue(f.nome in vittime,f"Tutti gli elementi associati ad un personaggio devono essere nelle liste di attributi del Personaggio")
                self.assertTrue(all([m in [f.nome for f in personaggio.vittime if type(f)==Personaggio] for m in vittime]),f"Tutti i vittime del personaggio {nome} devono essere nell'attributo di quel Personaggio")


    @data( #personaggio1, personaggio2, parentela, parentela inversa
            ['Jon Snow','Rhaella Targaryen','nonno','nipote figlio di figlio'],
            ['Rickard Stark','Arya Stark','nipote figlio di figlio','nonno'],
            ['Benjen Stark','Sansa Stark','nipote figlio di fratello','zio'],
            ['Aegon Targaryen','Daenerys Targaryen','zio','nipote figlio di fratello'],
            ['Rickon Stark','Robb Stark','fratello','fratello'],
            ['Joanna Lannister','Cersei Lannister','figlio','genitore'],
            ['Benjen Stark','Catelyn Stark','lontana','lontana'],
            ['Theon Greyjoy','Balon Greyjoy','genitore','figlio'],
            ['Aerys II Targaryen','Rhaegar Targaryen','figlio','genitore'],
            ['Arya Stark','Joffrey Baratheon','nessuna','nessuna']
    )
    @unpack
    @pytest.mark.t12
    def test_14_Personaggio_parentela(self, p1, p2, parentela, parentelainv):
        self.assertTrue(p1 in self.personaggi, f"Il personaggio {p1} deve apparire nel catalogo_personaggi")
        self.assertTrue(p2 in self.personaggi, f"Il personaggio {p2} deve apparire nel catalogo_personaggi")
        p1 = self.personaggi[p1]
        p2 = self.personaggi[p2]
        self.assertEqual(p1.parentela(p2), parentela, f"{p1.nome} e {p2.nome} devono avere la parentela {parentela}")
        self.assertEqual(p2.parentela(p1), parentelainv, f"{p2.nome} e {p1.nome} devono avere la parentela {parentelainv}")

    @data( #nome, famiglia_allargata
            ['Theon Greyjoy',['Euron Greyjoy', 'Alannys Greyjoy', 'Balon Greyjoy', 'Maron Greyjoy', 'Rodrik Greyjoy', 'Theon Greyjoy', 'Yara Greyjoy', 'Aeron Greyjoy']],
            ['Nymeria Sand',['Oberyn Martell', 'Obara Sand', 'Trystane Martell', 'Doran Martell', 'Ellaria Sand', 'Tyene Sand', 'Elia Martell', 'Nymeria Sand']],
            ['Euron Greyjoy',['Euron Greyjoy', 'Alannys Greyjoy', 'Balon Greyjoy', 'Maron Greyjoy', 'Rodrik Greyjoy', 'Theon Greyjoy', 'Yara Greyjoy', 'Aeron Greyjoy']],
            ['Alton Lannister',['Cersei Lannister', 'Tyrion Lannister', 'Martyn Lannister', 'Joanna Lannister', 'Tytos Lannister', 'Cynda Lannister', 'Tywin Lannister', 'Young Cersei Lannister', 'Alton Lannister', 'Jeyne Lannister', 'Kevan Lannister', 'Lancel Lannister', 'Jaime Lannister', 'Willem Lannister', 'Dorna Lannister']],
            ['Aegon V Targaryen',['Rhaegar Targaryen', 'Aegon Targaryen', 'Aegon V Targaryen', 'Jon Snow', 'Rhaella Targaryen', 'Maester Aemon', 'Drogon', 'Rhaegal', 'Viserion', 'Unknown Targaryen Queen', 'Viserys Targaryen', 'Daenerys Targaryen', 'Aerys II Targaryen', 'Rhaenys Targaryen']],
            ['Khal Drogo',['Aegon Targaryen', 'Aegon V Targaryen', 'Aerys II Targaryen', 'Daenerys Targaryen', 'Drogon', 'Jon Snow', 'Khal Drogo', 'Maester Aemon', 'Rhaegal', 'Rhaego', 'Rhaegar Targaryen', 'Rhaella Targaryen', 'Rhaenys Targaryen', 'Unknown Targaryen Queen', 'Viserion', 'Viserys Targaryen']],
            ['Rhaegar Targaryen',['Aegon Targaryen', 'Aegon V Targaryen', 'Aerys II Targaryen', 'Arya Stark', 'Benjen Stark', 'Bran Stark', 'Brandon Stark', 'Catelyn Stark', 'Daenerys Targaryen', 'Doran Martell', 'Drogon', 'Eddard Stark', 'Elia Martell', 'Ellaria Sand', 'Ghost', 'Grey Wind', 'Jon Snow', 'Lady', 'Lyanna Stark', 'Lyarra Stark', 'Maester Aemon', 'Nymeria', 'Nymeria Sand', 'Obara Sand', 'Oberyn Martell', 'Rhaegal', 'Rhaegar Targaryen', 'Rhaella Targaryen', 'Rhaenys Targaryen', 'Rickard Stark', 'Rickon Stark', 'Robb Stark', 'Sansa Stark', 'Shaggydog', 'Summer', 'Trystane Martell', 'Tyene Sand', 'Unknown Targaryen Queen', 'Viserion', 'Viserys Targaryen', 'Young Benjen Stark', 'Young Lyanna Stark', 'Young Ned', 'Young Ned Stark']],
            ['Petyr Baelish',['Brynden Tully', 'Catelyn Stark', 'Edmure Tully', 'Hoster Tully', 'Lysa Arryn', 'Petyr Baelish']],

           )
    @unpack
    @pytest.mark.t12
    def test_15_Personaggio_famiglia_allargata(self, nome, parenti):
        self.assertTrue(nome in self.personaggi, f"Il personaggio {nome} deve apparire nel catalogo_personaggi")
        p = self.personaggi[nome]
        out_parenti = {par.nome for par in p.famiglia_allargata()}
        self.assertEqual(set(out_parenti), set(parenti), "\nOutput:{}\nExpected:{}".format(set(out_parenti),set(parenti)))

    @data( # Casata1, Casata2, numero_ammazzati
      ['Targaryen','Lannister',1],
      ['Lannister','Baratheon',2],
      ['Stark','Targaryen',3],
      ['Frey','Stark',3],
      ['Tyrell','Lannister',4],
      ['Bolton','Targaryen',0],
      ['Greyjoy','Tarly',0],
      ['Tarly','Targaryen',2]
      )
    @unpack
    @pytest.mark.t12
    def test_16_Casata_ammazzatida(self, casata1, casata2, numero_ammazzati):
        self.assertTrue(casata1 in self.casate, f"La casata {casata1} deve apparire nel catalogo_casate")
        c1 = self.casate[casata1]
        self.assertTrue(casata2 in self.casate, f"La casata {casata1} deve apparire nel catalogo_casate")
        c2 = self.casate[casata2]
        self.assertEqual(c1.ammazzati_da(c2), numero_ammazzati, f"Per la casata {casata1} il numero di ammazzati dalla casata {casata2} deve essere {numero_ammazzati}")

    def test_20_Faide(self):
        res = faide(self.casate)
        self.assertTrue(type(res) == set, f"Faide deve tornare un set di tuple")
        resstr = set()
        for f in res:
            self.assertTrue(len(f)==4, f"Le tuple tornate da faide devono avere lunghezza 4")
            self.assertTrue(type(f[0])==type(f[2])==Casata, f"Le tuple devono contenere istanze di oggetti Casata")
            self.assertTrue(type(f[1])==type(f[3])==int, f"Le tuple devono contenere il numero di ammazzati per casata")
            t = (f[0].name, f[1], f[2].name, f[3])
            resstr.add(t)
        expected = {('Frey', 3, 'Stark', 1),('Tyrell', 3, 'Baratheon', 1)}
        self.assertEqual(resstr, expected,f"Il risultato di faide non è quello atteso")

    def test_21_Dynasty(self):
        res = dynasty(self.personaggi)
        self.assertTrue(type(res) == tuple, f"Dynasty deve tornare una tupla")
        self.assertTrue(len(res)==3, f"La tupla tornata da dynasty deve avere lunghezza 3")
        self.assertTrue(type(res[0])==Personaggio, f"Il primo elemento della tupla di dynasty deve essere un Personaggio")
        self.assertTrue(type(res[1])==int, f"Il secondo elemento della tupla di dynasty deve essere il numero di componenti della famiglia allargata")
        self.assertTrue(type(res[2])==set, f"Il terzo elemento della tupla di dynasty deve essere un insieme di istanze Personaggio")
        self.assertTrue(all([type(p)==Personaggio for p in res[2]]), f"Il terzo elemento della tupla di dynasty deve essere un insieme di istanze Personaggio")
        famiglia = {p.nome for p in res[2]}
        print(famiglia)
        expected = ('Sansa Stark',52,{'Robert Baratheon', 'Bran Stark', 'Renly Baratheon', 'Young Cersei Lannister', 'Brandon Stark', 'Ghost', 'Young Lyanna Stark', 'Jon Snow', 'Sansa Stark', 'Young Ned', 'Kevan Lannister', 'Catelyn Stark', 'Steffon Baratheon', 'Alton Lannister', 'Young Ned Stark', 'Baratheon Guard', 'Cersei Lannister', 'Joanna Lannister', 'Benjen Stark', 'Cassana Baratheon', 'Jaime Lannister', 'Shireen Baratheon', 'Stannis Baratheon', 'Rickon Stark', 'Jeyne Lannister', 'Arya Stark', 'Lancel Lannister', 'Joffrey Baratheon', 'Eddard Stark', 'Lyarra Stark', 'Dorna Lannister', 'Grey Wind', 'Summer', 'Tommen Baratheon', 'Nymeria', 'Ramsay Snow', 'Martyn Lannister', 'Willem Lannister', 'Lyanna Stark', 'Rickard Stark', 'Robb Stark', 'Tyrion Lannister', 'Roose Bolton', 'Lady', 'Selyse Baratheon', 'Tytos Lannister', 'Tywin Lannister', 'Walda Bolton', 'Young Benjen Stark', 'Shaggydog', 'Cynda Lannister', 'Myrcella Baratheon'})
        self.assertEqual(res[0].nome, expected[0],f"Il risultato di dynasty non è quello atteso")
        self.assertEqual(res[1], expected[1],f"Il risultato di dynasty non è quello atteso")
        self.assertEqual(famiglia, expected[2],f"Il risultato di dynasty non è quello atteso")

################################################################################
if __name__ == '__main__':
    Test.main()

