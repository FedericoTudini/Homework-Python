import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    # TODO:
    #   casi estremi:
    #       tutti voti uguali
    #       tutti voti diversi
    #   casi di dimensione variabile
    #       numero di valori generati   (Kmila valori)
    #       numero di valori generabili (valori da X a Y)

    def do_test(self, voti, expected):
        '''Implementazione del test
            - voti:     lista di voti
            - expected: lista risultante attesa
        '''
        voti_bis = copy.deepcopy(voti)
        result   = program.es1(voti_bis)
        self.check(type(result), list,     None, "il risultato non e' una lista")
        self.check(result,       expected, None, "il risultato non e' corretto")
        self.check(voti_bis,     voti,     None, "la lista dei voti non va modificata")
        return 1

    @file_data('test_01.json')
    def test_prende_i_dati_dal_file_json(self, voti, expected):
        '''Versione che prende i dati dal file Json'''
        return self.do_test(voti, expected)

    # esempio di test che elenca i dati nel decoratore
    @data((1000,   10, # 1000 voti casuali tra 1 e 10
            [1000, 1000, 895, 775, 683, 589, 487, 389, 286, 179, 92]), # risultato
          (10000, 100, # 10000 voti casuali tra 1 e 100
            [10000, 10000, 9893, 9797, 9691, 9593, 9484, 9373, 9277, 9191, 9098, 9022, 8911, 8818, 8710, 8597, 8483, 8397, 8286, 8178, 8075, 7965, 7858, 7763, 7667, 7577, 7479, 7369, 7253, 7165, 7064, 6961, 6871, 6774, 6667, 6561, 6461, 6374, 6285, 6175, 6073, 5962, 5853, 5767, 5645, 5533, 5438, 5323, 5234, 5145, 5048, 4939, 4836, 4737, 4634, 4522, 4425, 4325, 4232, 4131, 4027, 3942, 3847, 3749, 3649, 3549, 3460, 3372, 3273, 3177, 3082, 2992, 2908, 2811, 2702, 2616, 2524, 2422, 2324, 2199, 2091, 1994, 1878, 1777, 1686, 1585, 1478, 1385, 1272, 1180, 1103, 998, 880, 781, 687, 588, 476, 388, 300, 202, 103]),
          (100000,  1, # 100000 volte 1
            [100000, 100000]),
         )
    @unpack
    def test_N_voti_casuali_tra_1_e_K(self, N, K, expected):
        '''Genera N voti casuali tra 1 e K'''
        random.seed(0)
        voti = [ random.randint(1,K) for _ in range(N) ]
        self.do_test(voti, expected)

    @data(1000,               # voti=range(1,1001)
          10000)             # voti=range(1,10001)
    def test_sequenza_di_N_valori_consecutivi(self, N):
        print(N)
        '''Genera N voti da 1 a N'''
        voti = list(range(1,N+1))
        expected = [N] + list(reversed(voti))
        self.do_test(voti, expected)

    @data((300,800),          # voti=[800, 300]
          (2000, 50000),      # voti=[50000, 2000]
         )
    @unpack
    def test_2_valori_soli_grandi(self, low, high):
        '''I voti sono una semplice coppia'''
        voti = [high, low]
        expected = [2]*(low+1)
        expected += [1]*(high-low)
        self.do_test(voti, expected)

if __name__ == '__main__':
    Test.main()

