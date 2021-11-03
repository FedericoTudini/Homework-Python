'''
Abbiamo una immagine  .PNG . 
L'immagine presenta, su uno sfondo nero ( vale a dire di colore (0,0,0)), 
segmenti di colore bianco (vale a dire (255,255,255)) orizzontali e verticali di diversa lunghezza. 
Si veda ad esempio il file f1.png.
I segmenti, in alcuni casi, nell'incrociarsi creano rettangoli. 
Siamo interessati a trovare quei rettangoli di altezza e larghezza almeno 3 
(compreso il bordo, quindi con la parte nera alta e larga almeno 1 pixel)
e che, tranne il bordo completamente bianco, presentano tutti i pixel al loro interno di colore nero. 
A questo scopo vogliamo creare una nuova immagine identica alla prima se non per il 
fatto che questi rettangoli vengono evidenziati. 
Il bordo di questi rettangoli deve essere di colore verde (vale a dire (0,255,0)) e 
i pixel interni devono essere di colore rosso (vale a dire (255,0,0)).
Ad esempio l'immagine che vogliamo ricavare da quella nel file  f1.png e' 
nel file Risf1.png.

Scrivere una funzione es1(fimg,fimg1) che, presi in input gli indirizzi  di due file .PNG, 
legge dal primo l'immagine del tipo descritto sopra e salva nel secondo l'immagine 
con i rettangoli evidenziati. 
La funzione deve infine restituire  il numero di rettangoli che risultano evidenziati.

Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

ATTENZIONE: non sono permesse altre librerie.
'''

import immagini

def es1(fimg, fimg1):
    '''scova in fimg i rettangoli da evidenziare, crea una copia dell'immagine 
    in cui questi rettangoli risultano evidenziati (vale a dire hanno bordo  verde e
    interno  rosso) salva l'immagine in fimg1 e restituisce il numero di rettangoli
    evidenziati. '''
    img = immagini.load(fimg)
    h = len(img)
    w = len(img[0])
    bianco = (255,255,255)
    coord = []
    white = []
    upsx = []
    dwnsx = []
    updx = []
    dwndx = []
    rett = []
    rettangoli = []
               
    for x in range(0,h):
        for y in range(0,w):
            coord.append((x,y))
            
    coord = set(coord)
            
   
    for t in coord:
        if img[t[0]][t[1]] == bianco:
            white.append(t)
    
    white = set(white)
    
    for t in white:
        if (t[0],t[1] + 1) and (t[0] + 1,t[1]) and (t[0],t[1] + 2) and (t[0] + 2,t[1]) in white:
            upsx.append(t)
        if (t[0],t[1] + 1) and (t[0] - 1,t[1]) and (t[0],t[1] + 2) and (t[0] - 2,t[1])in white:
            dwnsx.append(t)
        if (t[0],t[1] - 1) and (t[0] + 1,t[1]) and (t[0],t[1] - 2) and (t[0] + 2,t[1]) in white:
            updx.append(t)
        if (t[0],t[1] - 1) and (t[0] - 1,t[1]) and (t[0],t[1] - 2) and (t[0] - 2,t[1]) in white:
            dwndx.append(t)
                                
    upsx = set(upsx)
    dwnsx = set(dwnsx)
    updx = set(updx)
    dwndx = set(dwndx)
            
    
    
    for t in upsx:
        w = 1
        x = 1
        y = 1
        z = 1
        a = tuple
        b = tuple
        c = tuple
        while (t[0],t[1]+x) in white:
            x+=1
            if (t[0],t[1]+x) in updx:
                a = (t[0],t[1]+x)
                while (a[0]+y,a[1]) in white:
                    y+=1
                    if (a[0]+y,a[1]) in dwndx:  
                        b = (a[0]+y,a[1])
                        while (b[0],b[1] - z) in white:
                            z+=1
                            if (b[0],b[1] - z) in dwnsx:
                                c = (b[0],b[1] - z)
                                while (c[0] - w,c[1]) in white:
                                    w+=1
                                    if (c[0] - w,c[1]) == t:
                                        rett.append([t,a,b,c])
    
    
    
                                        
    
    for lista in rett:
        for x in range(lista[0][0] + 1,lista[2][0]):
            for y in range(lista[0][1] + 1,lista[1][1]):
                if (x,y) in white:
                    rettangoli.append(lista)
                    break
                    
    for lista in rettangoli[::-1]:
        if lista in rett:
            rett.remove(lista)
            
    
    for ls in rett:
        for x in range(ls[0][1], ls[1][1] + 1):
            img[ls[0][0]][x] = (0,255,0)
            img[ls[2][0]][x] = (0,255,0)
            for y in range(ls[0][0], ls[2][0] + 1):
                img[y][ls[0][1]] = (0,255,0)
                img[y][ls[1][1]] = (0,255,0)
    
    for lista in rett:
        for x in range(lista[0][0] + 1,lista[2][0]):
            for y in range(lista[0][1] + 1,lista[1][1]):
                        img[x][y] = (255,0,0)
                        
    immagini.save(img, fimg1)

    return len(rett)
    
    

