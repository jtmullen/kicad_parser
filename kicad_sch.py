'''
``kicad_pcb`` parser using `sexp_parser.SexpParser`

The parser `KicadPCB` demonstrates the usage of a more general S-expression
parser of class `sexp_parser.SexpParser`. Check out the source to see how easy
it is to implement a parser in an almost declarative way.

A usage demonstration is available in `test.py`
'''

from .sexp_parser import *

__author__ = "Zheng, Lei"
__copyright__ = "Copyright 2016, Zheng, Lei"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "realthunder.dev@gmail.com"
__status__ = "Prototype"
	

class KicadSCH(SexpParser):

    # To make sure the following key exists, and is of type SexpList
    _symbol = ['in_bom',
               'on_board',
               'uuid']
			   
    _sheet = ['stroke',
              'fill',
              'uuid']

    _defaults =('junction',
				'no_connect',
				'bus_entry',
				'wire',
				'bus',
				'image',
				'polyline',
				'text',
				'label',
				'global_label',
				'hierarchical_label',
				'sheet',
				'sheet_instances',
				'symbol_instances',
				'pin',
				'path',
                ['symbol'] + _symbol,
                ['sheet'] + _sheet)

    def export(self, out, indent='  '):
        exportSexp(self,out,'',indent)

    def getError(self):
        return getSexpError(self)

    @staticmethod
    def load(filename):
        with open(filename,'r') as f:
            return KicadSCH(parseSexp(f.read()))

