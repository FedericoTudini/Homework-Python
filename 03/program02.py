# -*- coding: utf-8 -*-

"""
Bisogna progettare la classe piano_cartesiano che rappresenta un piano in cui
disegnare delle funzioni e dei punti.
Le specifiche della classe sono descritte nel seguito.

Il costruttore deve prendere tre argomenti con valore di default:
    -un intero che rappresenta la larghezza del piano (default 640)
    -un intero che rappresenta l'altezza del piano (default 480)
    -una tupla di colore (default bianco)
__init__ deve inizializzare un'immagine del colore e delle dimensioni ricevute
in input. L'immagine deve anche avere un asse verticale e un asse orizzontale,
di default nel centro dell'immagine (l'origine (0,0) sarà larghezza//2,
altezza//2), di colore (229,240,227) e che attraversa
l'intera immagine in entrambe le dimensioni.
Gli assi vengono disegnati sempre dietro a tutte le funzioni e punti del grafico.

Un metodo cambia_origine, che sposta l'origine del piano_cartesiano,
ridisegnando tutti gli oggetti già disegnati nel nuovo piano di riferimento. 
Il metodo cambia_origine prende come parametri una tupla di due interi,
corrispondenti alla posizione del nuovo punto di origine nella immagine. 
Se il punto passato non è compreso fra 0 e larghezza/altezza allora la funzione non fa nulla.

Un metodo disegna_funzione, che prende due argomenti, di cui uno con default:
    -una funzione
    -una tupla di colore (opzionale)
disegna_funzione deve disegnare la funzione sull'immagine di piano_cartesiano
utilizzando il colore passato in input oppure utilizzando il prossimo colore
preso da una tavolozza con 10 colori di default, che sono (0,0,0) (58,79,65)
(185,49,79) (213,161,142) (222,195,190) (225,222,227) (134,187,216)
(117,142,79) (246,174,45) (242,100,25). Se sono disegnate più di 10 funzioni,
il colore ricomincia dal primo. La funzione deve essere disegnata rispetto al
punto di origine, considerando i valori di x e y visibili nell'immagine.
Ad esempio, se l'immagine è 640x480 e l'origine è 320,240, le x visibili sono
da -320 a 319, mentre le y da -240 a 239.
NOTA: la funzione passata riceve un solo argomento, il valore intero x e torna il valore y, 
che può essere anche float. Per troncare il risultato y usate la funzione int()

Un metodo disegna_punto, che prende una tupla di due interi e una tupla di
colore per argomento e disegna un punto nelle coordinate corrispondenti alla
tupla, nel piano rappresentato dall'immagine.
I due interi della tupla sono, rispettivamente, la x e la y
relativi all'origine del piano (non sono relativi alla dimensione
dell'immagine). Se il punto è al di fuori dell'area visibile, non viene
disegnato, ma potrà apparire in seguito se si sposta l'origine del piano.

Un metodo cancella_funzione, che prende una funzione come paramentro e, se la
funzione è disegnata nel piano_cartesiano, la cancella.
Due funzioni sono uguali se disegnano esattamente lo stesso insieme di pixel
nel piano cartesiano nella zona visibile.

Un metodo cancella_punto, che prende una tupla di due interi come paramentro e,
se è disegnato un punto nelle coordinate indicate dalla tupla, anche se fuori 
dalla zona visibile, lo elimina dagli oggetti da disegnare e aggiorna il disegno.
Se quel punto è attraversato da una funzione, deve l'immagine deve mostrare
il colore della funzione.

Un metodo salva_immagine, che prende una stringa come parametro e salva
l'immagine del piano cartesiano con tutti gli oggetti disegnati in un file
con il nome preso dalla stringa in input.

L'ordine di sovrapposizione degli oggetti grafici nel piano è:
    - sfondo
    - assi
    - funzioni (nell'ordine in cui sono state aggiunte)
    - punti    (nell'ordine in cui sono state aggiunti)

ATTENZIONE: sono proibite tutte le librerie aggiuntive.

TIMEOUT: il timeout per ciascun test è di 5 secondi.

ATTENZIONE: assicuratevi che il file sia in encoding UTF8, ad esempio editandolo in Spyder o Notepad++.

"""

import immagini
import math


class piano_cartesiano():
    """ Scrivete qui il codice"""
    def __init__(self, l=640, a=480, c=(255,255,255)):
        """ Scrivete qui il codice"""

    def cambia_origine(self, newo):
        """ Scrivete qui il codice"""
        
    def disegna_funzione(self, f, c=None):
        """ Scrivete qui il codice"""

    def cancella_funzione(self, funz):
        """ Scrivete qui il codice"""

    def disegna_punto(self, p, c):
        """ Scrivete qui il codice"""

    def cancella_punto(self, punto):
        """ Scrivete qui il codice"""
    
    def salva_immagine(self, filename):
        """ Scrivete qui il codice"""






# le righe seguenti non vengono eseguite quando si importa il modulo
if __name__ == '__main__':
    """ Scrivete qui il codice"""
    pass
