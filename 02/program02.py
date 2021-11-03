"""
Bisogna indovinare una  sequenza  numerica segreta X composta da
una permutazione dei primi N interi.
Vengono fornite   M sequenze numeriche  con 5<=M<=N.
Delle M sequenze sappiamo che ciascuna  e' ottenuta a partire X
applicando il seguente procedimento:
a) viene selezionato un elemento della stringa X.
b) l'elemento selezionato viene cancellato da X ricompattando la sequenza
c) l'elemento cancellato viene reinserito in X in una qualunque delle
possibili posizioni diversa da quella originale.
Sappiamo inoltre che gli elementi selezionati per creare le M sequenze
son tutti diversi tra loro. 
Date le M sequenze vogliamo scoprire la sequenza numerica X

Ad esempio si cosiderino le seguenti 6 sequenze:

1) 2 3 4 7 1 5 6 8
2) 7 2 1 3 4 5 6 8
3) 7 2 3 4 1 6 5 8
4) 7 2 3 4 1 6 5 8
5) 7 4 2 3 1 5 6 8
6) 8 7 2 3 4 1 5 6 

la sequenza segreta X e' 7 2 3 4 1 5 6 8
infatti gli spostamenti di  X che hanno prodotto le 6 sequenze sono:
1) il 7 selezionato e poi reinserito in posizione 4
2) l' 1 selezionato e poi reinserito in posizione 3
3) il 6 selezionato e poi reinserito in posizione 1
4) il 5 selezionato e poi reinserito in posizione 6
5) il 4 selezionato e poi reinserito in posizione 2
6) l' 8 selezionato e poi reinserito in posizione 1

Scrivere una funzione es2(ftesto,ftesto1) che prende in input  il
nome del file di testo ftesto contenente le  M sequenze  e
e produce il file di testo di nome  ftesto1 con la sequenza segreta X

Gli elementi delle  sequenze in ftesto sono in linee consecutive e
ciascun elemento e'
separato dal successivo da uno o piu' spazi bianchi o dal return.
Ciascuna sequenza e' separata dalla precedente da almeno una linea vuota.

Gli elementi della sequenza in ftesto1 sono in linee consecutive, ogni linea
contiene esattamente tre elementi della sequenza tranne l'ultima che puo'
contenerne di meno. Ogni elemento elemento della sequenza e'
separato dal successivo da uno spazio o un return.

'''2 3 4 7 1 5 6 8\n\n
7 2 1 3 4 5 6 8\n\n
7 2 3 4 1 6 5 8\n\n
6 7 2 3 4 1 5 8\n\n
7 4 2 3 1 5 6 8\n\n
8 7 2 3 4 1 5 6'''

allora ftesto1 conterra' il testo
''7 2 3\n4 1 5\n6 8''

NOTA: il timeout previsto per questo esercizio è di 6 secondi per ciascun test

ATTENZIONE: sono proibite tutte le librerie aggiuntive

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder)
"""

def es2(fin, fout):
    with open(fin) as f:
        txt = f.read()
    f.close()
    
    
    
    txt = txt.replace("\n\n\n", "\n\n").split("\n\n")
    
    txt = list(map(lambda x : x.replace("\n", " "), txt))
    
    txt = list(filter(lambda x : x != "", txt))
    
    txt = list(map(lambda x : x.split(" "), txt))
    
    diz = {}
    
    ls = [0]*len(txt[0])
    
    ins = set(range(1,len(txt[0])+1))
    
    for x in range(len(txt[0])):
        diz = {}
        for y in range(len(txt)):
            diz[txt[y][x]] = diz.get(txt[y][x],0) + 1
        lt = list((filter(lambda x : diz.get(x) > len(txt)//2, diz)))
        if len(lt) == 1:
            ls[x] = lt[0]
            ins.remove(int(lt[0]))
    
    diz = {}
            
    for x in txt:
        for n in ins:
            k = x.index(str(n))
            if k != len(txt[0])-1:
                diz[(str(n),x[k+1])] = diz.get((str(n),x[k+1]),0) + 1
                diz[(x[k-1],str(n))] = diz.get((x[k-1],str(n)),0) + 1
            
    d = set(diz.items())
            
    while 0 in ls:
        k = ls.index(0)-1
        j = list(filter(lambda x : x[0][0] == ls[k],d))
        j = sorted(j,key = lambda x : -x[1])
        
        ls[k+1] = j[0][0][1]
        
    s = " ".join(ls)
    
    s = three(s)
    
        
    file1 = open(fout,"w")
    
    file1.write(s)
    
    file1.close

    return 

def three(s):
        k=0
        for x in range(len(s)):
            if s[x] == " ":
                k += 1
                if k == 3:
                    s = s[0:x] + "\n" + s[x+1:]
            if s[x] == "\n":
                k = 0
        return s


        
    


