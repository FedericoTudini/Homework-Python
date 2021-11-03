import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program03 as program

@ddt
class Test(testlib.TestCase):

    # TODO: aggiungere test di ricorsione

    def do_test(self, nome, expected):
        '''Implementazione del test
            - nome      : parte del nome dei file da leggere e da produrre
            - expected  : numero atteso di pixel colorati di blu
        '''
        fileInPNG   = f"es3_{nome}.png"
        fileOutPNG  = f"es3_test_{nome}.png"
        expectedPNG = f"es3_Ris_{nome}.png"

        # prima controlliamo che l'implementazione sia ricorsiva
        try:
            isrecursive.decorate_module(program)
            program.es3(fileInPNG, fileOutPNG)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        # poi controlliamo che faccia quello che deve fare
        with self.ignored_function('builtins.print'), \
             self.ignored_function('pprint.pprint'), \
             self.timer(1):
            result = program.es3(fileInPNG, fileOutPNG)
        self.assertEqual(type(result),  int,      "Il risultato non è un intero")
        self.assertEqual(result,        expected, f"Il risultato non è {expected} ma {result}")
        self.check_img_file(fileOutPNG, expectedPNG)

    @data(  
            ('esempio',  49),
            ('spirali', 458),
            ('tricky',   86),
            )
    @unpack
    def test(self, nome, expected):
        return self.do_test(nome, expected)

if __name__ == '__main__':
    Test.main()
