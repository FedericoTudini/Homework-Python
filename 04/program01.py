

''' 
    Alice e Bob si affrontano nel seguente gioco: 
    hanno  una sequenza iniziale di  N interi, 
    una mossa del gioco consiste nel selezionare dalla sequenza  due numeri  consecutivi 
    a e b, con a>b, i due numeri vengono eliminati dalla sequenza e 
    sostituiti dalla loro  differenza (a-b). Alice e Bob si alternano nelle mosse 
    con Alice che effettua la prima mossa, il gioco e' vinto se all'avversario viene 
    lasciata una sequenza per cui non e' possibile muovere (vale a dire: nella sequenza 
    non sono presenti due numeri consecutivi a e b con a>b).
    Data la sequenza  iniziale siamo interessati a trovare il numero 
    di possibili partite che portano alla vittoria di  Alice ed il numero di 
    possibili partite che portano alla vittoria di Bob. 
    
    Si consideri ad esempio l'albero di gioco che si ottiene a partire dalla 
    sequenza-configurazione '19 -3 2 -10 -20'  e che e' riportato  nel file 
    albero_di_gioco1.pdf:
    le possibili partite vittoriose per Alice sono tre (tutte portano alla 
    sequenza-configurazione '22 32') mentre le possibili partite vittoriose  per Bob sono 
    sei (tre partite con configurazione finale '10', due partite con configurazione 
    finale '30' e una partita con configurazione finale '50'). 
    
    Definire una funzione es(s) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che, data una  stringa  che codifica  una  configurazione iniziale 
    del gioco (i numeri della sequenza son separati da uno spazio), restituisce  
    una tupla di 6 elementi.
    - la prima   componente della tupla e' il numero di possibili vittorie di Alice
    - la seconda componente della tupla e' il numero di possibili vittorie di Bob
    - la terza   componente della tupla e' il numero di nodi-configurazioni presenti 
      nell'albero di gioco.
    - la quarta  componente della tupla e' il nome del vincitore della partita più corta
    - la quinta  componente della tupla e' il nome del vincitore della partita più lunga
    - la sesta   componente e' una lista con tutte le DIVERSE configurazioni di gioco presenti
    nell'albero di gioco. Ciascuna configurazione deve apparire nella lista
    come tupla di interi e le tuple devono comparire nella lista ordinate per lunghezza 
    crescente e, a parita' di lunghezza, in ordine crescente.
    
    Ad esempio es('19, -3, 2, -10, -20') deve restituire la sestupla 
    (3, 6, 25, 'Bob', 'Alice', 
        [(10,), (30,), (50,), 
        (10, -20), (20, 10), (22, 32), (30, -20), 
        (19, -3, 32), (20, -10, -20), (22, 2, 10), (22, 12, -20), 
        (19, -3, 2, 10), (19, -3, 12, -20), (22, 2, -10, -20), 
        (19, -3, 2, -10, -20)])

ATTENZIONE: non sono permesse altre librerie altre a quelle già importate.

TIMEOUT: il timeout per ciascun test è di 1 secondo.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

'''


#def es1(s):
#    s = s.split()
#    lista = []
#    for x in s:
#        lista.append(int(x))
#    conf = func(lista,[])
#    ins = set(conf)
#    v = vittorie(conf)
#    
#    return (v[0], v[1], len(conf), v[2], v[3], sorted(ins, key = lambda x : (len(x), x[0:] )))
#
#def func(s,configurazioni=[]):
#    
#    #aggiungo la configurazione alla lista (deve poi essere ordinata, nel return)
#    configurazioni.append(tuple(s))
#
#    #caso base: se la condizione non è valida esco dal ciclo
#    
#    if not check(s):
#        return 
#        
#    #passo ricorsivo: se la condizione è valida...
#    else:    
#        for k in range(len(s)-1):
#            if s[k] > s[k+1]:
#                #modifico la lista sostituendo i due elementi con la loro differenza 
#                j = s[:]
#                j.pop(k)
#                j.pop(k)
#                j.insert(k,s[k]-s[k+1])
#                func(j,configurazioni)
#                
#    return configurazioni
#
#def check(s):
#    flag = False
#    for k in range(len(s)-1):
#        if s[k] > s[k+1]:
#            flag = True
#        break
#    return flag
#
#def vittorie(l):
#    alice = 0
#    bob = 0
#    diz = {}
#    if len(l) % 2 == 0:
#        for x in l:
#            if not check(x):
#                if len(x) % 2 == 0:
#                    bob += 1
#                    diz[len(l[-1])-len(x)] = "Bob"
#                else:
#                    alice += 1
#                    diz[len(l[-1])-len(x)] = "Alice"
#    else:
#        for x in l:
#            if not check(x):
#                if len(x) % 2 == 0:
#                    alice += 1
#                    diz[len(l[-1])-len(x)] = "Alice"
#                else:
#                    bob += 1
#                    diz[len(l[-1])-len(x)] = "Bob"
#                
#    return alice,bob,diz[max(diz)],diz[min(diz)]

def check(s):
    flag = False
    for k in range(len(s)-1):
        if s[k] > s[k+1]:
            flag = True
            break
    return flag

class Albero:
    def __init__(self, radice):
        self.radice = radice
        self.figli = []
        self.padre = None
    
    def func(self):
        s = self.radice
        if not check(s):
            return self
        for k in range(len(s)-1):
                if s[k] > s[k+1]:
                    #modifico la lista sostituendo i due elementi con la loro differenza 
                    j = s[:]
                    j.pop(k)
                    j.pop(k)
                    j.insert(k,s[k]-s[k+1])
                    jr = Albero(j)
                    jr.padre = self 
                    self.figli.append(jr)
                    jr.func()
        return self
                    
                    
def es1(s):
    corta = ""
    lunga = ""
    s = s.split()
    lista = []
    for x in s:
        lista.append(int(x))
    tree = Albero(lista).func()
    e = esplora(tree, [])
    e.append(tuple(lista))
    vA = vittorie(e)[0]
    vB = vittorie(e)[1]
    ins = set(e)
    if len(lista) % 2 == 0:
        vA, vB = vB, vA
    m = list(filter( lambda x :  not check(x), e))
    mosse = set()
    for x in m:
        mosse.add(len(lista)-len(x))
    if max(mosse) % 2 != 0: 
        lunga = "Alice"
    else: 
        lunga = "Bob" 
    if min(mosse) % 2 != 0: 
        corta= "Alice"
    else: 
        corta = "Bob" 
        
        
    
    return (vA, vB, len(e), lunga, corta, sorted(ins, key = lambda x : (len(x), x[0:]) )) 

def esplora(albero, ls = []):
    
    for t in albero.figli:
        ls.append(tuple(t.radice))
        esplora(t, ls)
    return ls


def vittorie(e):
    pari = 0
    dispari = 0
    for x in e:
        if not check(x):
            if len(x) % 2 == 0:
                pari += 1
            else: dispari += 1
    return pari, dispari
#    if len(albero.figli) == 0:
#        return albero
#    for x in albero.figli:
#        k = esplora(x)
#    return k
    

#m = list(filter( lambda x :  not check(x), e))
    

            
            
        
        


