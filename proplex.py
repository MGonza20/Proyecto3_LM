from ply import lex
import ply.yacc as yacc
from uuid import uuid4
class Node:
    def __init__(self, value,id=uuid4(),leftChild=None,rightChild=None, parent=None):
        self.value = value
        self.id = id
        self.leftChild = leftChild
        self.rightChild = rightChild

tokens = [
    'NOT',
    'AND',
    'OR',
    'IMP',
    'DIMP',
    'VARIABLE',
    # 'CONST',
    'LPAREN',
    'RPAREN'
]

t_NOT = r'\~'
t_AND = r'\^'
t_OR = r'o'
t_IMP = r'\=>'
t_DIMP = r'<\=>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore = ' \t'

# def t_CONST( t ):
#     r'[0-1]'
#     t.value = int(t.value)
#     return t

def t_VARIABLE( t ) :
    r'[p|q|r|s|t|u|v|w|x|y|z|1|0]'
    t.value = t.value
    return t

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )


def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()





tree_nodes = []

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_expression_and(p):
    'expression : expression AND term'
    p[0] = Node(value="^", leftChild=p[1], rightChild=p[3])
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    print(p[0].rightChild.value)

def p_expression_or(p):
    'expression : expression OR term'
    p[0] = Node(value="o", leftChild=p[1], rightChild=p[3])
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    print(p[0].rightChild.value)

def p_not_expression(p):
    'expression : NOT expression'
    # Crear el nodo y dibujar un camino entre su leftChild
    p[0] = Node(value="~", leftChild=p[2])


def p_expression_implication(p):
    'expression : expression IMP expression'
    p[0] = Node(value="=>", leftChild=p[1], rightChild=p[3])
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild

def p_expression_dimplication(p):
    'expression : expression DIMP expression'
    p[0] = Node(value="=>", leftChild=p[1], rightChild=p[3])
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : VARIABLE'
    p[0] = Node(value=p[1])
    # Crear un nuevo nodo
#
# def p_factor_num(p):
#     'factor : CONST'
#     p[0] = Node(value=p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!", p)

precedence = (
    ( 'left', 'IMP', 'DIMP' ),
    ( 'left', 'AND', 'OR' )
)

input = "~~p"

# Give the lexer some input
lexer.input(input)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
print("-- Creando Arbol-- ")
parser = yacc.yacc()
result = parser.parse(input)