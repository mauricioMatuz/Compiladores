import ply.lex as lex
import re
import codecs
import os
import sys


tokens = ['ID','PLUS','MINUS','TIMES','DIVIDE','ASSIGN','EQUAL','NE','LT','LTE','GT',
         'GTE','LPARENT','RPARENT','COMA','SEMMICOLOM','LLLAVE','RLLAVE','NUMBER'
]

reservadas = ['IF','ELSE','WHILE','DO','INT','FLOAT','STRING','INCLUDE','HASH']
# reservadas = {
#       'if':'IF',
#       'else':'ELSE',
#       'while':'WHILE',
#       'do':'DO',
#       'int':'INT',
#       'float':'FLOAT',
#       'string':'STRING',
#       'include':'INCLUDE',
#       'hash':'HASH',
# }

tokens = tokens + reservadas

t_ignore = '\t'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NE = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMA = r','
t_SEMMICOLOM = r';'
# t_LLAVE = r'\{'
# t_RLLAVE = r'\}'

def t_ID(t):
      r'[a-zA-Z_][a-zA-Z0-9_]*'#!el ciclo pe de 0 a mucho
      if t.value.upper() in reservadas:
            t.value = t.value.upper()
            t.type = t.value
      return t

def t_COMMENT(t):
      r'//.*'
      pass

def t_NUMBER(t):
      r'\d+'
      t.value = t.value
      return t

def t_NEWLINE(t):
      r'\n+'
      t.lexer.lineno += len(t.value)



def t_error(t):
      print("caracter ilegal llamen a la migra '%s'"%t.value[0])
      t.lexer.skip(1)
      
def buscarFicheros(directorio):
      fichero = []
      numArchivo = ''
      respuesta = False
      cont = 1
      for base, dirs, files in os.walk(directorio):
            fichero.append(files)
      for file in files:
            print(str(cont) + ". "+file)
            cont = cont + 1
            
      while respuesta == False:
            numArchivo = input("\nNumero del Test: ")
            for file in files:
                  if file == files[int(numArchivo)-1]:
                        respuesta = True
                        break

      print("Has escogido \"%s\"\n" %files[int(numArchivo)-1])
      return files[int(numArchivo)-1]
                        
      
directorio = 'C:/Users/matam/Desktop/IA/com/C1/test/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
      tok = analizador.token()
      if not tok :
            break
      print(tok)