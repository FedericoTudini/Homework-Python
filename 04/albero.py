class Albero:
    def __init__(self,V):
        self.id=V
        self.f=[]

################### DA QUI IN GIÙ SONO SOLO FUNZIONI NECESSARIE PER I TEST #####################
################### CHE È PROIBITO USARE NEL VOSTRO CODICE                 #####################

def fromLista1(lista):
    '''Crea l'albero da una lista [valore, listafigli]
           In cui lista figli contiene alberi o e' la lista vuota. '''
    r=Albero(lista[0])
    r.f=[fromLista1(x) for x in lista[1]]
    return r
    
################################################################################################
