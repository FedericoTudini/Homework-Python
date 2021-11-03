import copy
import unittest
import testlib
import json
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Implementazione del test
            - ls:       lista di parole
            - testo:    testo in cui cercarle
            - expected_lista:   lista di parole risultato
            - expected_parola:  parola apparsa più volte nel testo
            - expected_ls:      parole non apparse (ls modificata)
        '''
        ls1_bis = copy.deepcopy(ls)
        res = program.es3(ls1_bis, testo)
        self.check(type(res), tuple,         None, 'non viene restituita una tupla')
        self.check(len(res),  2,             None, 'non viene restituita una tupla di 2 elementi')
        lista, parola = res
        self.check(lista,   expected_lista,  None, 'non viene restituita la lista corretta')
        self.check(parola,  expected_parola, None, 'non viene restituita la parola corretta')
        self.check(ls1_bis, expected_ls,     None, 'non viene modificata correttamente la lista in input')
        return 1

    @file_data('test_03.json')
    def test_letto_da_json(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

    @file_data('test_03.json')
    def test_letto_da_json_e_moltiplicato_per_1000(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        testo = testo*1000
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

    @file_data('test_03.json')
    def test_letto_da_json_e_moltiplicato_per_2000(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        testo = testo*2000
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

if __name__ == '__main__':
    Test.main()

