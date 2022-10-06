from ply import lex

tokens = [
    'NOT',
    'AND',
    'OR',
    'IMP',
    'DIMP',
    'VARIABLE',
    'CONST',
    'LPAREN',
    'RPAREN'
]

t_NOT = r'~'
t_AND = r'\^'
t_OR = r'o'
t_IMP = r'\=>'
t_DIMP = r'<\=>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore = ' \t'

def t_CONST( t ):
    r'[0-1]'
    t.value = int(t.value)
    return t

def t_VARIABLE( t ) :
    r'[p|q|r|s|t|u|v|w|x|y|z]'
    t.value = t.value
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )


def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

# Give the lexer some input
lexer.input("qop")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)


