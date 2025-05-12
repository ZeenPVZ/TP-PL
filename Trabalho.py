# trabalho.py
import ply.lex as lex
import play.yacc as yacc
import csv
"""
Autores: Afonso Ferreira - 27981 ; Tomás Braga - 18447
Data: 12/05/2025
Descrição: Trabalho Prático 
UC: Processamento de Linguagens
"""
#Estrutura de Dados
tabelas={}

#Léxico
tokens=('IMPORT', 'EXPORT', 'DISCARD', 'TABLE', 'RENAME', 'PRINT', 'SELECT', 'FROM', 'WHERE', 'LETRANUM', 'STRING', 'NUMFLOAT')

t_ignora=' \t'

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

def t_novalinha(t):
    r'\n+'
    return t

def t_comentario(t):
    r'--.#'
    return t

def t_erro(t):
    print(f"Caracter Ilegal: {t.value[0]}")
    t.lexer.skip(1) 

lexer=lex.lex()






