import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program02 as program
import albero
@ddt
class Test(testlib.TestCase):

    def do_test(self, rad, expected):
        '''Implementazione del test
            - rad:      radice dell'albero da trasformare in stringa di testo 
            - expected: stringa di testo attesa
        '''
        with self.ignored_function('builtins.print'), self.timer(0.5):
            result   = program.es2(rad)
        self.assertEqual(type(result), str,      "il risultato non e' una stringa ")
        self.assertEqual(result,       expected, "il risultato non e' corretto"    )

    def test_albero_5_nodi(self):
        '''...'''
        lista0=['04',[['05',[['01',[['06',[['03',[]]]]]]]]]]
        r0=albero.fromLista1(lista0)
        stringa0='''04
| 
05
| 
01
| 
06
| 
03'''
        return self.do_test(r0, stringa0)



    def test_albero_12_nodi(self):
        '''...'''
        lista1= ['05', [['02', [['01', []]]], ['04', [['01', []], ['02', [['03', []], ['06', []]]], ['09', []], ['08', []],['02', []]]],['06', []]]]
        r1=albero.fromLista1(lista1)
        stringa1='''              05              
 _____________|_____________  
|             |             | 
02            04            06
|    _________|_________      
01  |     |     |   |   |     
    01    02    09  08  02    
         _|_                  
        |   |                 
        03  06                '''
        return self.do_test(r1, stringa1)

    def test_albero_17_nodi(self):
        '''...'''
        lista2=['36', [['05', [['63', [['91', [['03', []], ['51', []]]], ['10', [['63', []], ['16', [['58', []]]], 
        ['38', [['62', []], ['32', []], ['30', []]]]]]]]]], ['67', [['34', [['61', []], ['77', [['72', []], ['24', [['84', []]]]]]]]]]]]
        r2=albero.fromLista1(lista2)
        stringa2='''                   36                 
         __________|___________       
        |                      |      
        05                     67     
        |                      |      
        63                     34     
   _____|_____               __|__    
  |           |             |     |   
  91          10            61    77  
 _|_     _____|_____             _|_  
|   |   |   |       |           |   | 
03  51  63  16      38          72  24
            |    ___|___            | 
            58  |   |   |           84
                62  32  30            '''
        return self.do_test(r2, stringa2)


    def test_albero_41_nodi(self):
        '''...'''
        lista3=['60', [['66', [['56', [['36', [['70', []], ['99', []], ['05', []]]], ['33', [['28', []], ['52', []], ['80', []], ['84', []]]], 
        ['55', [['79', []], ['66', []]]]]], ['58', [['67', [['48', []], ['80', []], ['16', []]]], ['66', [['57', []]]], ['05', []]]], 
        ['19', [['54', [['28', []], ['86', []]]], ['50', [['84', []]]]]]]], ['25', [['96', []], ['77', [['52', [['03', []]]], 
        ['42', [['89', []]]], ['72', [['94', []], ['87', []], ['85', []], ['26', []]]]]]]]]]
        r3=albero.fromLista1(lista3)
        stringa3='''                                                        60                                    
                                        ________________|________________                     
                                       |                                 |                    
                                       66                                25                   
                  _____________________|_____________________        ____|_____               
                 |                            |              |      |          |              
                 56                           58             19     96         77             
     ____________|____________           _____|_____       __|__         ______|______        
    |             |           |         |       |   |     |     |       |   |         |       
    36            33          55        67      66  05    54    50      52  42        72      
 ___|___     _____|_____     _|_     ___|___    |        _|_    |       |   |    _____|_____  
|   |   |   |   |   |   |   |   |   |   |   |   57      |   |   84      03  89  |   |   |   | 
70  99  05  28  52  80  84  79  66  48  80  16          28  86                  94  87  85  26'''
        return self.do_test(r3, stringa3)
        
if __name__ == '__main__':
    Test.main()

