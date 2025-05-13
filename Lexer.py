# trabalho.py
import ply.lex as lex
import csv

#Estrutura de Dados
tabelas={}

class ArithLexer:
    def __initialize__(self):
        self.lexer=None

#Léxico
tokens=('IMPORT', 'EXPORT', 'DISCARD', 'TABLE', 'RENAME', 'PRINT', 'SELECT', 'FROM', 'WHERE', 'LETRANUM', 'STRING', 'NUMFLOAT')

t_ignore=' \t'

t_IMPORT=r'IMPORT'
t_EXPORT=r'EXPORT'
t_DISCARD=r'DISCARD'
t_TABLE=r'TABLE'
t_RENAME=r'RENAME'
t_PRINT=r'PRINT'
t_SELECT=r'SELECT'
t_FROM=r'FROM'
t_WHERE=r'WHERE'

def t_LETRANUM(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    return t    

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_NUMFLOAT(t):
    r'\d+(\.\d+)?'
    return t

def t_nova_linha(t):
    r'\n+'
    t.lexer.lineno+=t.value.count("\n")

def t_comentario(t):
    r'--.#'
    pass    #Ignora os Comentários

def t_multilinecomment(t):
    r'--\#.*'
    pass    #Ignora os Comentários Multilinha

def t_erro(t):
    print(f"Caracter Ilegal: {t.value[0]}")
    t.lexer.skip(1) 

lexer=lex.lex(_iniciate_)

    




