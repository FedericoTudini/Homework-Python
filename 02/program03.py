'''
Abbiamo un file contenente dei dati in forma tabellare:
- la prima riga contiene i nomi dei campi che individuano le informazioni, separati da tab
- la seconda riga contiene le indicazioni del tipo dei contenuti delle colonne (int/float/str) separati da tab
- le linee successive contengono i dati, sempre separate da tab, che devono essere intepretati come indicato nella seconda riga
    Nota: può succedere che una riga non contenga l'informazione in una o più colonne
Esempio: il file es3_esempio.txt che contiene dei dati presi da un gruppo di sensori ad intervalli di 1 minuto

Anno	Mese	Giorno	Ora	Minuto	Sensore1	Sensore2	Sensore3	Note
int	int	int	int	int	float	float	float	str
2018	12	25	0	0		3	45.3	manca il Sensore 1
2018	10	25	0	1	1	36		manca il Sensore 3
2017	11		0	2	14	5	82	manca il giorno
2016		23	11	17	13	4.5	32	manca il mese

Si vuol calcolare una "tabella pivot" per esaminare i dati e confrontarli tra loro.
(vedi https://en.wikipedia.org/wiki/Pivot_table)

Una tabella pivot è definita indicando:
    - quali campi devono essere mostrati in orizzontale come intestazioni di colonna nella prima riga
    - quali campi devono essere mostrati in verticale   come intestazioni di riga    nella prima colonna
    - quale campo deve   essere mostrato nella tabella in ciascuna delle altre caselle
    - come vanno aggregate le informazioni selezionate per una determinata casella (vedi sotto)
        - count     conta quanti valori diversi da '' sono presenti
        - min       trova il minimo
        - max       trova il massimo
        - sum       calcola la somma dei valori (solo per colonne numeriche)
        Nota: se non ci sono valori nelle righe selezionate, il risultato è '' (stringa vuota)

Nota: potete assumere che l'input di es3 sarà sempre corretto (p.es. si chiede 'sum' solo per campi con valori numerici)

La tabella viene costruita elencando come intestazioni delle colonne(righe) tutte le combinazioni di valori distinti che sono presenti nei campi selezionati.
Se come intestazione sono stati selezionati più campi, separatene i valori col carattere spazio ' '.
    Esempio, se nella tabella precedente si seleziona il campo 'Anno' le intestazioni delle colonne(righe) saranno, nell'ordine
        '2016'
        '2017'
        '2018'
    Se invece si selezionano i due campi ['Anno', 'Mese'] le intestazioni delle righe/colonne saranno, nell'ordine
        '2016 '         (qui il campo 'Mese' ha valore '')
        '2017 11'
        '2018 10'
        '2018 12'

Una volta individuate le combinazioni di valori da mostrare come intestazioni delle righe e delle colonne della tabella pivot, 
ciascuna casella della tabella individua una combinazione di valori unica dei valori dei campi di riga e di quelli di colonna. 
A ciascuna combinazione di valori corrispondono le 0 o più righe dei dati che hanno esattamente quei valori nei campi selezionati.
Nella corrispondente casella della tabella pivot va inserito il risultato che si ottiene 
applicando la funzione di aggregazione indicata al sottoinsieme di dati così selezionati che corrispondono a quella casella.

Esempio: vedi il file es3_Ris_esempio.txt che si ottiene dal file es3_esempio.txt selezionando:
    - per le colonne i campi ['Anno', 'Mese']
    - per le righe  il campo ['Giorno']
    - come dato da aggregare il campo 'Sensore1'
    - come funzione di aggregazione la funzione 'sum'
Ottenendo la tabella (in cui evidenzio le colonne con caratteri | )
-----------------------
|       |    |23  |25 |
|2016   |    |13.0|   |
|2017 11|14.0|    |   |
|2018 10|    |    |1.0|
|2018 12|    |    |   |
-----------------------
                    
in cui possiamo notare: 
    la seconda colonna che ha intestazione di colonna ''      perchè una riga dei dati non conteneva il Giorno
    la seconda riga    che ha intestazione di riga    '2016 ' perchè una riga dei dati non conteneva il Mese
    diverse caselle della tabella che contengono il valore '' perchè non esisteva il dato per il Sensore1 
            per quella combinazione di valori di Anno, Mese, Giorno

Si implementi la funzione es3(fin, fout, colonne, righe, dato, aggregatore) che:
    - legge dal file fin una tabella di dati separati da tab, in cui
        - la prima riga indica i nomi dei campi 
        - la seconda riga i tipi dei dati delle colonne
        - dalla terza in poi contiene i dati
    - costruisce la tabella pivot che ha:
        - come intestazioni delle colonne le combinazioni uniche di valori per i campi elencati nella lista 'colonne', in ordine alfabetico crescente
        - come intestazioni delle righe   le combinazioni uniche di valori per i campi elencati nella lista 'righe',   in ordine alfabetico crescente
        - come valori di tutte le altre caselle i valori ottenuti aggregando i valori della colonna 'dato' con la funzione indicata da 'aggregatore'
            Nota: se per una casella non esistono righe dei dati oppure i dati non contengono valori, il valore per la casella è ''
    - salva la tabella pivot nel file fout
    - torna come risultato la coppia (nrighe, ncolonne) che indica la dimensione della tabella ottenuta, intestazioni di riga e colonna comprese

NOTA: potete assumere che i nomi delle colonne/righe indicate siano sempre presenti nella prima riga del file dei dati, 
    che i tipi ci siano e che ci sia almeno una riga di dati

TIMEOUT: il timeout per ciascun test è di 5 secondi.

ATTENZIONE: è proibito l'uso di ogni libreria aggiuntiva (non potete fare import)

ATTENZIONE: assicuratevi che il file del programma sia in encoding UTF8 (ad esempio editandolo in Spyder o Notepad++)

'''

def es3(fin, fout, colonne, righe, dato, aggregatore):
    
    with open(fin) as f:
        txt = f.readlines()
    
    for x in range(2):
        txt[x] = txt[x].replace("\n", "").split("\t")
        
    combinazioni_righe = set()
    ls_righe = {x : txt[0].index(x) for x in righe}
    ls_colonne = {x : txt[0].index(x) for x in colonne}
    d = {}
    nDato = txt[0].index(dato)
    t = eval(txt[1][nDato])
    
    if t == str:
        default = ""
    else:
        default = 0
        
        
    if aggregatore == "sum":
        func = somma
    elif aggregatore == "count":
        func = conta
    elif aggregatore == "min":
        func = minimo
    elif aggregatore == "max":
        func = massimo    
        
        
        
    if len(colonne) == 2 and len(righe) == 2:
        for x in range(2,len(txt)):
            txt[x] = txt[x].replace("\n", "").split("\t")
            k = " ".join((txt[x][ls_colonne[colonne[0]]],txt[x][ls_colonne[colonne[1]]]))
            if d.get(k, None) == None:
                d[k] = {}
            combinazioni_righe.add(" ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]])))
            k2 = " ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]]))
            
            print(txt[x][nDato])
            if txt[x][nDato] == "":
                pre = default
            else:
                pre = txt[x][nDato]

                intersezione = func(t(d[k].get(k2, default)),t(pre))
            d[k][k2] = str(intersezione)
    elif len(colonne) == 2 and len(righe) == 1:
        for x in range(2,len(txt)):
            txt[x] = txt[x].replace("\n", "").split("\t")
            k = " ".join((txt[x][ls_colonne[colonne[0]]],txt[x][ls_colonne[colonne[1]]]))
            print(k)
            if d.get(k, None) == None:
                d[k] = {}
            combinazioni_righe.add(txt[x][ls_righe[righe[0]]])
            k2 = txt[x][ls_righe[righe[0]]]
            
            if txt[x][nDato] == "" and aggregatore != "count":
                intersezione = ""
            else:
                pre = txt[x][nDato]
                intersezione = func(t(d[k].get(k2, default)),t(pre))
            d[k][k2] = str(intersezione)
    elif len(colonne) == 1 and len(righe) == 2:
        for x in range(2,len(txt)):
            txt[x] = txt[x].replace("\n", "").split("\t")
            k = txt[x][ls_colonne[colonne[0]]]
            if d.get(k, None) == None:
                d[k] = {}
            combinazioni_righe.add(" ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]])))
            k2 = " ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]]))
            if txt[x][nDato] == "":
                pre = default
            else:
                pre = txt[x][nDato]

            intersezione = func(t(d[k].get(k2, default)),t(pre))
            d[k][k2] = str(intersezione)
    elif len(colonne) == 1 and len(righe) == 1:
        for x in range(2,len(txt)):
            txt[x] = txt[x].replace("\n", "").split("\t")
            k = txt[x][ls_colonne[colonne[0]]]
            if d.get(k, None) == None:
                d[k] = {}
            combinazioni_righe.add(txt[x][ls_righe[righe[0]]])
            k2 = txt[x][ls_righe[righe[0]]]
            
            if txt[x][nDato] == "":
                pre = default
            else:
                pre = txt[x][nDato]

            intersezione = func(t(d[k].get(k2, default)),t(pre))
            d[k][k2] = str(intersezione)
        
        
    s = "\t".join(sorted(combinazioni_righe))+"\n"
    
    file = open(fout,"w")
    file.write(s)
    
    combinazioni_righe = sorted(combinazioni_righe)
    
    for x in sorted(d.keys()):
        stringa = x +"\t"+ "\t".join([d[x].get(k, "") for k in combinazioni_righe]) + "\n"
        file.write(stringa)
    
    file.close()
    
    
    
    return d

#funzioni di aggregazione
def somma(a,b):
    return a+b
def massimo(a,b):
    return max(a,b)
def minimo(a,b):
    return min(a,b)
def conta(a,b):
    if b != "":
        a+=1
    return a

#    for x in range(2,len(txt)):
#        txt[x] = txt[x].replace("\n", "").split("\t")
#        if len(colonne) == 2:
#            k = " ".join((txt[x][ls_colonne[colonne[0]]],txt[x][ls_colonne[colonne[1]]]))
#        else:
#            k = txt[x][ls_colonne[colonne[0]]]
#        d[k] = {}
#        if len(righe) == 2:
#            combinazioni_righe.add(" ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]])))
#            k2 = " ".join((txt[x][ls_righe[righe[0]]],txt[x][ls_righe[righe[1]]]))
#        else:
#            combinazioni_righe.add(txt[x][ls_righe[righe[0]]])
#            k2 = txt[x][ls_righe[righe[0]]]
#        if txt[x][nDato] == "":
#            pre = default
#        else:
#            pre = txt[x][nDato]

#    with open(fin) as f:
#        txt = f.readlines()
#        
#    lista_dizionari = []
#    
#    ls_righe = {x:txt[0].index(x) for x in righe}
#    ls_colonne = {txt[0].index(x) for x in colonne}
#    nDato = txt[0].index(dato)
#    
#    combinazioni_righe = []
#    combinazioni_colonne = []
#        
#    if aggregatore == "count":
#        f = "count"
#    else:
#        f = eval(aggregatore)
#   
#    for x in range(2,len(txt)):
#        txt[x] = txt[x].replace("\n", "").split("\t")
#        d = {txt[0][i] : txt[x][i] for i in ls_righe}
#        d.update({txt[0][j] : txt[x][j] for j in ls_colonne})
#        d[txt[0][nDato]] = txt[x][nDato]
#        lista_dizionari.append(d)
#        
##        sorted(items, key = lambda x : (x[0] == colonne[0],x[0] == colonne[1]), reverse = True)
#        
#        
##        
##    
##    for x in txt[2:]:
##        d = {txt[0][i] : x[i] for i in ls_righe}
##        d.update({txt[0][j] : x[j] for j in ls_colonne})
##        d[txt[0][nDato]] = x[nDato]
##        lista_dizionari.append(d)
##        if len(colonne) == 2:
##            combinazioni_colonne.append((d.get(colonne[0]),d.get(colonne[1])))
##        if len(righe) == 2:
##            combinazioni_righe.append((d.get(righe[0]),d.get(righe[1])))
##            
##    if len(combinazioni_righe) == 0:
##        combinazioni_righe = set(diz[righe[0]] for diz in lista_dizionari )
##    else:
##        combinazioni_righe.sort(key = lambda x : (x[0],x[1]))
##    if len(combinazioni_colonne) == 0:
##        combinazioni_colonne = set(diz[colonne[0]] for diz in lista_dizionari )
##    else:
##        combinazioni_colonne.sort(key = lambda x : (x[0],x[1]))
#        
##    combinazioni = []
##        
##    for c in combinazioni_righe:
##        for r in combinazioni_colonne:
##            if type(c) == tuple and type(r) == tuple:
##                combinazioni.append(c+r)
##            elif type(c) == tuple and type(r) != tuple:
##                combinazioni.append(c+(r,))
##            elif type(c) != tuple and type(r) == tuple:
##                combinazioni.append((c,)+r)
##            elif type(c) != tuple and type(r) != tuple:
##                combinazioni.append((c+r))
#            
#            
#    t = eval(txt[1][nDato])
#
#    lista = []
#    
#    if type(combinazioni_righe[0]) != tuple and type(combinazioni_colonne[0]) != tuple:
#        lista = unoeuno(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t)
#        s = "\t".join(combinazioni_righe)+"\n" + lista
#    elif type(combinazioni_righe[0]) != tuple and type(combinazioni_colonne[0]) == tuple:
#        lista = dueCeunoR(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t)
#        s = "\t".join(combinazioni_righe)+"\n" + lista
#    elif type(combinazioni_righe[0]) == tuple and type(combinazioni_colonne[0]) != tuple:
#        lista = dueReunoC(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t)
#        s = "\t".join([x[0] for x in combinazioni_colonne]) + "\n" +"\t".join([x[1] for x in combinazioni_colonne]) + lista
#    elif type(combinazioni_righe[0]) == tuple and type(combinazioni_colonne[0]) == tuple:
#        lista = dueRedueC(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t)
#        s = "\t".join([x[0] for x in combinazioni_colonne]) + "\n" +"\t".join([x[1] for x in combinazioni_colonne]) + lista
#    file1 = open(fout,"w")
#    
#    file1.write(s)
#    
#    file1.close
#        
#    
##    return prima_riga         
#    return len(combinazioni_righe), len(combinazioni_colonne)

#def conta(ls):
#    return ls.count("")
#
#def unoeuno(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t):
#    ris = ""
#    for c in combinazioni_colonne:
#        interno_tabella = []
#        for r in combinazioni_righe:
#            
#            ls = [t(x.get(dato)) for x in list(filter(lambda x : x[txt[0][ls_righe[0]]] == r and x[txt[0][ls_colonne[0]]] == c, lista_dizionari )) if x.get(dato) != ""]
#            #controllo sul tipo di dato
#            
#            if f == "count":
#                k = ls.count("")
#            else:
#                if len(ls) == 0:
#                    k = ""
#                else:
#                    k = str(f(ls))
#            
#            interno_tabella.append(k)
#        ris += c+"\t"  + "\t".join(interno_tabella) + "\n"
#        
#    return ris
#
#def dueCeunoR(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t):
#    ris = ""
#    for c in combinazioni_colonne:
#        interno_tabella = []
#        for r in combinazioni_righe:
#            
#            ls = [t(x.get(dato)) for x in list(filter(lambda x : x[txt[0][ls_righe[0]]] == r and x[txt[0][ls_colonne[0]]] == c[0] and x[txt[0][ls_colonne[1]]] == c[1], lista_dizionari )) if x.get(dato) != ""]
#            if f == "count":
#                k = ls.count("")
#            else:
#                if len(ls) == 0:
#                    k = ""
#                else:
#                    k = str(f(ls))
#            interno_tabella.append(k)
#        ris += " ".join(c)+"\t"  + "\t".join(interno_tabella) + "\n"
#        
#    return ris
#
#def dueReunoC(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t):
#    ris = ""
#    for c in combinazioni_colonne:
#        interno_tabella = []
#        for r in combinazioni_righe:
#            
#            ls = [t(x.get(dato)) for x in list(filter(lambda x : x[txt[0][ls_colonne[0]]] == c[0] and x[txt[0][ls_colonne[1]]] == c[1] and x[txt[0][ls_righe[0]]] == r[0] and x[txt[0][ls_righe[1]]] == r[1], lista_dizionari )) if x.get(dato) != ""]
#            if f == "count":
#                k = ls.count("")
#            else:
#                if len(ls) == 0:
#                    k = ""
#                else:
#                    k = str(f(ls))
#            interno_tabella.append(k)
#        ris += c+"\t"  + "\t".join(interno_tabella) + "\n"
#        
#    return ris
#
#def dueRedueC(combinazioni_colonne, combinazioni_righe, f, txt, lista_dizionari, ls_righe, ls_colonne, dato, t):
#    ris = ""
#    for c in combinazioni_colonne:
#        interno_tabella = []
#        for r in combinazioni_righe:
#            
#            ls = [t(x.get(dato)) for x in list(filter(lambda x : x[txt[0][ls_colonne[0]]] == c and x[txt[0][ls_righe[0]]] == r[0] and x[txt[0][ls_righe[1]]] == r[1], lista_dizionari )) if x.get(dato) != ""]
#            if f == "count":
#                k = ls.count("")
#            else:
#                if len(ls) == 0:
#                    k = ""
#                else:
#                    k = str(f(ls))
#            interno_tabella.append(k)
#        ris += " ".join(c)+"\t"  + "\t".join(interno_tabella) + "\n"
#        
#    return ris
#
#def creaDizionari(txt):
#    return
    





