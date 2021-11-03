import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program02 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, ftesto1, fexpected):
        '''Implementazione del test
            - ftesto:    nome  del file delle sequenze da decodificare
            - expected:  la sequenza cercata
        '''
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(6):
            result   = program.es2(ftesto, ftesto1)
        self.check_text_file(ftesto1, fexpected)

    @data( 
            ('es2_seq1.txt',   'es2_test_seq1.txt',   'es2_RisSeq1.txt'),
            ('es2_seq10.txt',  'es2_test_seq10.txt',  'es2_RisSeq10.txt'),
            ('es2_seq20.txt',  'es2_test_seq20.txt',  'es2_RisSeq20.txt'),
            ('es2_seq30.txt',  'es2_test_seq30.txt',  'es2_RisSeq30.txt'),
            ('es2_seq40.txt',  'es2_test_seq40.txt',  'es2_RisSeq40.txt'),
            ('es2_seq50.txt',  'es2_test_seq50.txt',  'es2_RisSeq50.txt'),
            ('es2_seq60.txt',  'es2_test_seq60.txt',  'es2_RisSeq60.txt'),
            ('es2_seq70.txt',  'es2_test_seq70.txt',  'es2_RisSeq70.txt'),
            ('es2_seq80.txt',  'es2_test_seq80.txt',  'es2_RisSeq80.txt'),
            ('es2_seq90.txt',  'es2_test_seq90.txt',  'es2_RisSeq90.txt'),
            ('es2_seq100.txt', 'es2_test_seq100.txt', 'es2_RisSeq100.txt'),
            )
    @unpack
    def test_trova_sequenze(self, fname, fname1, expected):
        return self.do_test(fname, fname1, expected)


if __name__ == '__main__':
    Test.main()

