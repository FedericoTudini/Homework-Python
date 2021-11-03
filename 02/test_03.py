import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, nome, colonne, righe, dato, aggregatore):
        '''Implementazione del test
            - nome   : nome del dataset
            - colonne: lista dei nomi delle intestazioni di colonna
            - righe  : lista dei nomi delle intestazioni di riga
            - dato   : nome della colonna da aggregare nella tabella pivot
            - aggregatore: funzione di aggregazione (min/max/sum/count)
        '''
        ftesto     = f"es3_{nome}.txt"         # file dati da leggere
        ftesto1    = f"es3_test_{nome}.txt"    # file in cui salvare la tabella
        fexpected  = f"es3_Ris_{nome}.txt"     # file con la tabella attesa
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.timer(5):
            result   = program.es3(ftesto, ftesto1, colonne, righe, dato, aggregatore)
        self.check_text_file(ftesto1, fexpected)

    @data( 
            #Anno	Mese	Giorno	Ora	Minuto	Sensore1	Sensore2	Sensore3	Note
            #int	int	int	int	int	float	float	float	str
            ('esempio',     ['Anno',   'Mese'   ], ['Giorno'             ], 'Sensore1', 'sum'),

            #ID	speed	period	warning	pair
            #int	int	str	str	str
            ('amis',        ['period', 'warning'], ['pair'               ], 'speed',    'max'),

            #ID	state	year	month	day	date	wday	births
            #int	str	int	int	int	str	str	int
            ('Birthdays',   ['state'            ], ['wday'               ], 'births',   'sum'),

            #mpg	cylinders	displacement	horsepower	weight	acceleration	year	origin	name
            #float	int	float	float	int	float	int	str	str
            ('mpg',         ['year', 'cylinders'], ['origin',            ], 'mpg',      'max'),

            # survived	pclass	name	sex	age	sibsp	parch	ticket	fare	cabin	embarked
            # int	int	str	str	int	int	int	str	float	str	str
            ('titanic',     ['pclass', 'sex'    ], ['embarked','survived'], 'survived', 'count'),

            # ID	year	sex	education	vocabulary
            # str	int	str	int	int
            ('Vocab',       ['year', 'sex'      ], ['education'          ], 'vocabulary', 'max'),

            #carat	cut	color	clarity	depth	table	price	x	y	z
            #float	str	str	str	float	int	int	float	float	float
            ('diamonds',   ['cut', 'color'      ], ['clarity'          ], 'price',    'sum'),

            #ID	caseid	state	age	airbag	injury	restraint	sex	inimpact	modelyr	airbagAvail	airbagDeploy	Restraint	D_injury	D_airbagAvail	D_airbagDeploy	D_Restraint	year
            #str	str	int	int	int	int	int	int	int	int	str	str	str	int	str	str	str	int
            ('FARS',   ['sex', 'restraint'], ['airbagAvail', 'airbagDeploy'], 'injury',    'sum'),
            )
    @unpack
    def test_trova_sequenze(self, name, colonne, righe, dato, aggregatore):
        return self.do_test(      name, colonne, righe, dato, aggregatore)


if __name__ == '__main__':
    Test.main()

