
'''Una o piu' sequenze numeriche sono codificate all'interno di un file di testo. 
Ciascuna sequenza e' distribuita su una o piu' linee del file.  
Gli elementi sulla stessa linea sono almeno due e sono separati da spazi; 
l'ultimo elemento della linea e' l'ultimo della sequenza  se nessuna delle linee 
che seguono  comincia con quell'elemento, in caso contrario la sequenza continua 
nella prima  linea che segue che contiene quell'elemento.
Le linee di una stessa sequenza possono essere inframmezzate da linee vuote e/o 
linee di altre sequenze.
Nota che una stessa linea puo' essere in comune a piu' sequenze.
Ogni volta che una linea non è il seguito di un'altra sequenza, si inizia una nuova sequenza.
Se veda come  esempio il file fseq1.txt che codifica  le seguenti tre sequenze:
1 2 3 4 5 6 7 8
20 30 40 50 5 6 7 8
4 50 6
Dato un file di testo che codifica sequenze nel modo appena descritto vogliamo 
produrre un file di testo in cui le sequenze appaiono decodificate. Vale a dire:
- le sequenze compaiono una dopo l'altra nel file e nello stesso ordine con 
  cui iniziano nel file originale
- ciascuna sequenza e' separata della precedente da una linea vuota.
- ciascuna sequenza si trova distribuita in linee consecutive, cinque elementi 
  per linea tranne al piu' l'ultima linea (che puo' contenerne meno) e con 
  gli elementi di una linea separati tra loro da un unico spazio.

Scrivere una funzione es1(ftesto,ftesto1) che prende in input  il
nome ftesto del file di testo  contenente sequenze numeriche codificate
e produce il file ftesto1  in cui le sequenze compaiono decodificate.
La funzione deve tornare il numero di sequenze individuate.

Ad esempio es1 per il file fseq1.txt deve produrre un file di testo RisSeq1.txt 
che contiene il seguente testo:

"1 2 3 4 5\n6 7 8\n\n20 30 40 50 5\n6 7 8\n\n4 50 6"

NOTA: il timeout previsto per questo esercizio è di 6 secondi per ciascun test

ATTENZIONE: sono vietate tutte le librerie aggiuntive.

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)
''' 
        
def es1(ftesto,ftesto1):
    with open(ftesto) as f:
        txt = f.readlines()
    f.close()
    
    ls = []
    
    for x in txt:
        if x[0] != "\n":
            ls.append(" ".join(x.split()))
            
    lista = riordina(ls)
    
    s = "\n\n".join(lista)
    
    s2 = five(s)
    
    file1 = open(ftesto1,"w")
    
    file1.write(s2)
    
    file1.close

    return len(lista)


def riordina(lista):
    tup = tuple()
    ris = []
    for x in range(len(lista)):
        k=x+1
        if x in tup:
            continue
        
        while k < len(lista):
            if lista[x][-1] == lista[k][0]:
                lista[x] += lista[k][1:]
                if k not in tup:
                    tup += (k,)
            if lista[x][-2:] == lista[k][0:2]:
                lista[x] += lista[k][2:]
                if k not in tup:
                    tup += (k,)
            k+=1
        ris.append(lista[x])
        
    tup = sorted(tup)
        
    for x in tup[::-1]:
        lista.pop(x)
            
    return lista

def five(s):
    k=0
    for x in range(len(s)):
        if s[x] == " ":
            k += 1
            if k == 5:
                s = s[0:x] + "\n" + s[x+1:]
        if s[x] == "\n":
            k = 0
            
    return s
            
            
    

                        



