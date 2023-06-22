
import ply.lex as lex

class Lexer:
    t_INTEGER = r'\d+'
    t_REAL    = r'\d+\.\d+'
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_COLON   = r';'

    t_EQUAL   = r'=='
    t_LEQUAL  = r'<='
    t_GEQUAL  = r'>='
    t_NEQUAL  = r'!='
    t_LTHEN   = r'<'
    t_GTHEN   = r'>'

    t_ASSIGN  = r'<-' 

    t_ignore  = ' \t'    

  
    def __init__(self, tokens, reserved):
        self.tokens = tokens
        self.reserved = reserved
    
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-z0-9]*'
        t.type = self.reserved.get(t.value, "ID")
        return t

    def t_error(self, t):
        print("Invalid character: %s" % t.value[0])
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def tokenizer(self, data):
        self.lexer.input(data)
    
    def printTokens(self, printTokens=False):
        if printTokens:
            while True:
                token = self.lexer.token()
                if not token:
                    break
                print(token)