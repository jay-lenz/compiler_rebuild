import sys
from lexer import Lexer

tokens = [
    'ID',
    'INTEGER','REAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'LEQUAL',
    'GEQUAL',
    'NEQUAL',
    'LTHEN',
    'GTHEN',
    'LPAREN',
    'RPAREN',
    
    'COLON'
    
    ,'ASSIGN'
   ]

reserved = {

  'if'   : 'IF',
  'then' : 'THEN',
  'begin': 'BEGIN',
  'end'  : 'ENbD',
  'else' : 'ELSE',
  'while': 'WHILE',
  'do'   : 'DO',
  'done' : 'DONE',
  'print': 'PRINT',

}

tokens = tokens + list(reserved.values())

input = open(sys.argv[1], 'r').read()

print('\n')

compileLexer = Lexer(tokens,reserved)
compileLexer.build()
compileLexer.tokenizer(input)
compileLexer.printTokens(True)

