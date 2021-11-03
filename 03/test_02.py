import testlib
from ddt import file_data, ddt, data, unpack
import math

import program02 as program

@ddt
class Test(testlib.TestCase):


    # TODO: testare separatamente i vari metodi

    def do_test(self, nome, sfondo, origine, funzioni, punti, delfuncs, delpoints):
        '''Implementazione del test
            - nome         : parte del nome del file di output
            - sfondo       : colore di sfondo
            - origine      : dove posizionare l'origine degli assi
            - funzioni     : funzioni da disegnare
            - punti        : punti da disegnare
            - delfuncs     : funzioni da eliminare
            - delpoints    : punti da cancellare
        '''
        fileOutPNG  = f"es2_test_{nome}.png"   # file PNG che deve essere creato
        expectedPNG = f"es2_Ris_{nome}.png"    # file PNG della immagine attesa

        #fileOutPNG = expectedPNG # per creare i reference

        with self.ignored_function('builtins.print'), \
             self.ignored_function('pprint.pprint'), \
             self.timer(5):
            if sfondo:
                p = program.piano_cartesiano(c=sfondo)
            else:
                p = program.piano_cartesiano()
            for F in funzioni:
                p.disegna_funzione(F)
            for P in punti:
                p.disegna_punto(*P)
            if origine:
                p.cambia_origine(origine)
            for F in delfuncs:
                p.cancella_funzione(F)
            for P in delpoints:
                p.cancella_punto(P)
            p.salva_immagine(fileOutPNG)
            self.check_img_file(fileOutPNG, expectedPNG)

    @data(  ('solo-funzioni',
                    (0, 0, 0),                      # sfondo
                    None,                           # origine di default
                    (lambda x: x**2/100,            # funzioni
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    (),                             # punti
                    (),                             # funzioni da cancellare
                    ()                              # punti da cancellare
            ),
            ( 'funzioni-cambio-origine',  
                    None,                           # sfondo di default
                    (200, 240),
                    (lambda x: x**2/100, 
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    (),
                    (),
                    ()
            ),
            ( 'solo-punti',  
                    (0, 0, 255),                     # sfondo
                    None,                           # origine di default
                    (),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ()
            ),
            ( 'punti-cambio-origine',  
                    None,                           # sfondo di default
                    (100, 200),
                    (),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ()
            ),
            ('funzioni-e-punti', 
                    None,                           # sfondo di default
                    None,                           # origine di default
                    (lambda x: x**2/100, 
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ()
            ),
            ('funzioni-e-punti-cambio-origine', 
                    None,                           # sfondo di default
                    (520, 440),
                    (lambda x: x**2/100, 
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ()
            ),
            ('funzioni-e-punti-delfuncs', 
                    None,                           # sfondo di default
                    (520, 440),
                    (
                    lambda x: x**2/100, 
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (
                    lambda x: x , 
                    lambda x: x**2/100, 
                    ),
                    ()
            ),
            ( 'punti-delpoints',  
                    (0,0,0),                        # sfondo nero
                    (100, 200),
                    (),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ( (x, y)                                             for x in range(-400,400,120) for y in range(-400, 400, 120) ),
            ),
            ('funzioni-e-punti-delpoints', 
                    None,                           # sfondo di default
                    None,                           # origine di default
                    (lambda x: x**2/100, 
                    lambda x: x , 
                    lambda x: x**3/10000, 
                    lambda x: math.sin(x/50)*50,
                    ),
                    ( ((x, y), (abs(x%255), abs(y%255), abs((x+y)%255))) for x in range(-1000,1000,40) for y in range(-1000, 1000, 40) ),
                    (),
                    ( (x, y)                                             for x in range(-400,400,120) for y in range(-400, 400, 120) ),
            ),
        )
    @unpack
    def test(self, nome, sfondo, origine, funzioni, punti, delfuncs, delpoints):
        return self.do_test(nome, sfondo, origine, funzioni, punti, delfuncs, delpoints)

if __name__ == '__main__':
    Test.main()
