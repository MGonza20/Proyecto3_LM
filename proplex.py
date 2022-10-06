from ply import lex
import ply.yacc as yacc
from uuid import uuid4
import networkx as nx
import matplotlib.pyplot as plt
import random

class Incrementer:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
class Node:
    def __init__(self, value,leftChild=None,rightChild=None, id=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.id = id
    def __str__(self):
        return self.value

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
labelsDict = {}

# def t_CONST( t ):
#     r'[0-1]'
#     t.value = int(t.value)
#     return t

incr = Incrementer()
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

G = nx.DiGraph()

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]



def p_expression_and(p):
    'expression : expression AND term'
    p[0] = Node(value="^", leftChild=p[1], rightChild=p[3], id=incr.value)
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    G.add_edge(p[0].id, p[0].leftChild.id)
    G.add_edge(p[0].id, p[0].rightChild.id)
    incr.increment()

def p_expression_or(p):
    'expression : expression OR term'
    p[0] = Node(value="o", leftChild=p[1], rightChild=p[3], id=incr.value)
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    G.add_edge(p[0].id, p[0].leftChild.id)
    G.add_edge(p[0].id, p[0].rightChild.id)
    incr.increment()


def p_not_expression(p):
    'expression : NOT expression'
    p[0] = Node(value="~", leftChild=p[2], id=incr.value)
    # Crear el nodo y dibujar un camino entre su leftChild
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    G.add_edge(p[0].id, p[0].leftChild.id)
    incr.increment()

def p_expression_implication(p):
    'expression : expression IMP expression'
    p[0] = Node(value="=>", leftChild=p[1], rightChild=p[3], id=incr.value)
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    G.add_edge(p[0].id, p[0].leftChild.id)
    G.add_edge(p[0].id, p[0].rightChild.id)
    incr.increment()

def p_expression_dimplication(p):
    'expression : expression DIMP expression'
    p[0] = Node(value="<=>", leftChild=p[1], rightChild=p[3], id=incr.value)
    # Crear el nodo y dibujar un camino entre su leftChild y rightChild
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    G.add_edge(p[0].id, p[0].leftChild.id)
    G.add_edge(p[0].id, p[0].rightChild.id)
    incr.increment()

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : VARIABLE'
    p[0] = Node(value=p[1], id=incr.value)
    G.add_node(incr.value)
    labelsDict[incr.value] = p[0].value
    incr.increment()


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

def createTree(input, G):

    # input = "p o ((p ^ q) o z)"
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
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], font_weight='bold', with_labels=True, labels=labelsDict)

    plt.show()


def menu():
    print('\nProyecto 3 - Lógica matemática\n\nOpciones:\n1. Crear árbol \
           \n2. Salir \n')

menu()
option = int(input('Elija una opción: '))
while option != 2:
    if option == 1:
        incr.value = 0
        labelsDict = {}
        G = nx.DiGraph()
        user_input = str(input('Ingrese expresión: ')) 
        createTree(user_input, G)
    else: print('\nOpcion invalida\n')

    menu()
    option = int(input('Elija una opción: '))
