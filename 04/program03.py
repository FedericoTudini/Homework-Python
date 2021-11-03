r'''

In una immagine in formato PNG è disegnato un albero secondo le seguenti convenzioni:
- lo sfondo dell'immagine è nero (0, 0, 0)
- la radice viene rappresentata da un pixel verde (0, 255, 0)
- tutti gli altri nodi sono rappresentati da un pixel rosso (255, 0, 0)
- due nodi sono in relazione padre-figlio se esiste una sequenza di pixel bianchi
    affiancati in orizzontale e/o verticale che li collega
- se più nodi sono collegati dalla stesso percorso bianco che si dirama,
    vuol dire che uno è il padre e gli altri sono tutti suoi figli
- una volta individuato il nodo radice è possibile individuare quali siano i padri
    e quali siano i figli in tutto l'albero navigandolo a partire dalla radice
- potete assumere che i percorsi non si intersechino (ma possono diramarsi)
    e che siano sempre larghi 1 pixel
- potete assumere che non esistano cicli (altrimenti sarebbe un grafo e non un albero)

Esempio: (R=rosso, w=bianco, V=verde, ' '=nero)
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   wwwwwww                                        | 1
         w      RwwwwwwwwwwwwwwwR         R       | 2
         w            w                   w       | 3
         w            wwwRwwwwwwww        w       | 4
         w            w          w        w       | 5
         wwwwRwwwwwwwww          Vwwwwwwwww       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------

La radice (V) è il pixel alle coordinate        (33, 6)
mentre gli altri nodi (R) sono alle coordinate  ( 3, 0), (13, 6), (15, 10), (16, 2), (25, 4), (25, 10), (32, 2), (42, 2)
L'albero che ne risulta è

                (33, 6)
               /   |   \
             /     |    \
         (25,10) (42,2)  (25,4)
                        /  |   \
                       /   |    \
                   (16,2)(32,2) (13,6)
                                /    \
                            (3,0)  (15,10)

Implementate la funzione es3(filePNGinput, filePNGoutput) che:
    - legge l'immagine PNG contenuta nel file filePNGinput
    - individua e costruisce l'albero corrispondente
    - individua i due nodi più distanti nell'albero e
        - colora di blu (0, 0, 255) tutti i pixel bianchi del percorso che li collega
          passando di nodo in nodo (se necessario ripassando su alcuni pixel 2 volte)
            (lasciando invariato lo sfondo ed i nodi rossi/verdi)
    - salva nel file filePNGoutput l'immagine risultante
    - torna come risultato il numero di pixel che sono stati colorati di blu
        (che potrebbero essere di meno della lunghezza del percorso più lungo
        perchè i tratti su cui si passa due volte vanno contati una sola volta)

NOTA: La distanza tra due nodi è il numero minimo totale dei SOLI pixel BIANCHI che li collegano
passando per i nodi interni (alcuni tratti potrebbero essere percorsi 2 volte).
SUGGERIMENTO: ispiratevi al calcolo del diametro di un albero
NOTA: per calcolare il percorso più lungo i pixel su cui si passa più volte vanno contati più volte
    (ad esempio il numero di pixel per il percorso (16,2)->(25,4)->(32,2) è 10+14=24)
NOTA: potete assumere che il percorso più lungo sia unico

Nel caso dell'esempio i due nodi più distanti sono (42,2) e (3,0) per cui l'immagine da salvare è
(b)=blu
          1111111111222222222233333333334444444444
01234567890123456789012345678901234567890123456789
--------------------------------------------------
   R                                              | 0
   bbbbbbb                                        | 1
         b      RwwwwwwwwwwwwwwR         R       | 2
         b            w                   b       | 3
         b            bbbRbbbbbbbb        b       | 4
         b            b          b        b       | 5
         bbbbRbbbbbbbbb          Vbbbbbbbbb       | 6
         w                       w                | 7
         w               wwwwwwwww                | 8
         w               w                        | 9
         wwwwwwR         R                        |10
--------------------------------------------------
e la funzione torna 49 che è il numero di pixel bianchi che sono stati colorati di blu (b)

ATTENZIONE: Almeno una delle funzioni/metodi che risolvono l'esercizio DEVE essere ricorsiva.
ATTENZIONE: per fare in modo che il macchinario di test riconosca automaticamente la presenza della ricorsione
    questa funzione ricorsiva DEVE essere una funzione esterna oppure il metodo di una classe.
    Anche questa classe va definita esternamente alle funzioni.

ATTENZIONE: Non potete usare altre librerie a parte immagini.

ATTENZIONE: assicuratevi di salvare il programma con encoding utf8
(ad esempio usando come editor Notepad++ oppure Spyder)

In timeout per ciascuno dei test è di 1 secondo.

'''

import immagini

class Nodo:
    def __init__(self, v, percorso=[]):
        self.v = v
        self.figli = []        
        self.percorso = percorso
                
    def __repr__(self):
        return "Nodo " + str(self.v)


def es3(filePNGInput, filePNGOutput):
    # inserite qui il vosto codice
    img, h, w = dimensions(filePNGInput)
    y, x = start(img)
    alb = explore(y, x, img, h, w, None, set(), list())
    _, pixels = diametro(alb)
    return draw(img, pixels[1], filePNGOutput)


def diametro(nodo):
    maxProf1 = [-1, list()]
    maxProf2 = [-1, list()]
    maxDiam = [-1, list()]
    if not nodo.figli:
        return [0, list()], [0, list()]
    for figlio in nodo.figli:
        prof, diam = diametro(figlio)
        if diam[0] > maxDiam[0]:
            maxDiam = diam
        tempDist = prof[0]+len(figlio.percorso)-2
        if tempDist > maxProf1[0]:
            maxProf2 = maxProf1
            maxProf1 = [tempDist, figlio.percorso + prof[1]]
        elif tempDist > maxProf2[0]:
            maxProf2 = [tempDist, figlio.percorso + prof[1]]
    diamRadice = maxProf1[0]
    if len(nodo.figli) > 1:
        diamRadice += maxProf2[0]
    if diamRadice > maxDiam[0]:
        pixel = maxProf1[1].copy()
        if len(nodo.figli) > 1:
            pixel += maxProf2[1]
        diam = [diamRadice, pixel]
    else:
        diam = maxDiam
    prof = maxProf1
    return prof, diam


def draw(img, c, nome):
    count=0
    for y, x in c:
        if img[y][x]==(255, 255, 255):
            img[y][x]=(0, 0, 255)
            count+=1
    immagini.save(img, nome)
    return count


def explore(y, x, img, h, w, alb=None, esplorati = set(), percorso=list()):
    if not check (y, x, h, w) and (y, x) not in esplorati:
        if img[y][x] == (0, 0, 0):
            return
        else:
            esplorati.add((y,x))
            percorso.append((y, x))
            if not alb:
                alb = Nodo((y, x), percorso.copy())
            elif img[y][x] == (255, 0, 0) or img[y][x]==(0, 255, 0):

                # prendi solo il percorso dal figlio al padre
                ramo = []
                i = len(percorso)-1
                while percorso[i] != alb.v:
                    ramo.append(percorso[i])
                    i -= 1
                ramo.append(percorso[i])
                
                figlio = Nodo((y, x), ramo)
                alb.figli.append(figlio)
                alb = figlio
                
            explore(y+1, x, img, h, w, alb, esplorati, percorso)
            explore(y-1, x, img, h, w, alb, esplorati, percorso)
            explore(y, x+1, img, h, w, alb, esplorati, percorso)
            explore(y, x-1, img, h, w, alb, esplorati, percorso)
            percorso.pop()
    return alb


def start(img):
    for y, row in enumerate(img):
        for x, el in enumerate(row):
            if el == (0, 255, 0):
                return y, x
    

def dimensions(filePNGInput):
    '''ritorna l'immagine e la dimensione dell'immagine'''
    img = immagini.load(filePNGInput)
    return img, len(img), len(img[0])


def check(y, x, h, w):
    '''controlla se sono dentro l'immagine'''
    return y<0 or x<0 or h<=y or w<=x
    


    



