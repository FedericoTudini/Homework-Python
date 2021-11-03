import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, ftesto1, expected1, expected2):
        '''Implementazione del test
            - ftesto:    nome  del file delle sequenze da decodificare
            - ftesto1:   nome  del file delle sequenze da produrre
            - expected1: file decodificato atteso
            - expected2: il numero di sequenze atteso
        '''
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(6):
            result   = program.es1(ftesto,ftesto1)
        self.assertEqual(type(result), int,       "il risultato non e' unintero")
        self.assertEqual(result,       expected2, "il numero di sequenze trovate non e' corretto")
        self.check_text_file(ftesto1, expected1)

    def test_fseq1_sequenze_di_esempio(self):
        return self.do_test('es1_fseq1.txt', 'es1_fseq1b.txt', 'es1_RisSeq1.txt', 3)

    def test_fseq2_10righe_da_4(self):
        return self.do_test('es1_fseq2.txt', 'es1_fseq2b.txt', 'es1_RisSeq2.txt', 8)

    def test_fseq3_100righe_da_20(self):
        return self.do_test('es1_fseq3.txt', 'es1_fseq3b.txt', 'es1_RisSeq3.txt', 48)
        
    def test_fseq6_100righe_da_20_e_spazi(self):
        return self.do_test('es1_fseq6.txt', 'es1_fseq6b.txt', 'es1_RisSeq6.txt', 45)

    def test_fseq7_5000righe_da_6_e_spazi(self):
        return self.do_test('es1_fseq7.txt', 'es1_fseq7b.txt', 'es1_RisSeq7.txt', 2461)

    def test_fseq4_10000righe_da_3(self):
        return self.do_test('es1_fseq4.txt', 'es1_fseq4b.txt', 'es1_RisSeq4.txt', 4790)
        
    def test_fseq5_3000righe_da_100(self):
        return self.do_test('es1_fseq5.txt', 'es1_fseq5b.txt', 'es1_RisSeq5.txt', 1413)

if __name__ == '__main__':
    Test.main()

