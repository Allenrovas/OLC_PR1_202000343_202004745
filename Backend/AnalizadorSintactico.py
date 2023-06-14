 #Precedencia para las operaciones
from src.Expresiones.identificador import Identificador
from src.TablaSimbolos.Arbol import Arbol
from src.TablaSimbolos.Excepcion import Excepcion
import ply.yacc as yacc
from AnalizadorLexico import *
from src.Expresiones.aritmetica import Aritmetica
from src.Expresiones.primitivos import Primitivos
from src.Instrucciones.imprimir import Imprimir
from src.Instrucciones.declaraciones import Declaracion_Variables
from src.TablaSimbolos.TablaSimbolos import TablaSimbolos
from src.Instrucciones.condicional_if import If
from src.Expresiones.relacional_logica import Relacional_Logica
from src.Instrucciones.ciclo_for import For
from src.Instrucciones._return import Return
from src.Instrucciones.llamada_funcion import Llamada_Funcion
from src.Instrucciones.funcion import Funcion
from src.Instrucciones.Asignacion import Asignacion
from src.Instrucciones.ciclo_while import While
import sys
sys.setrecursionlimit(10000000)


precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','IGUALDAD','DESIGUALDAD'),
    ('left','MAYORQ','MENORQ','MAYORIGUAL','MENORIGUAL'),
    ('left','MAS','MENOS','COMA'),
    ('left','POR','DIV','MOD'),
    ('left','POT'),
    ('left','PARIZQ', 'PARDER'),
    ('right','UMENOS'),
)

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_evaluar(t):
    '''instruccion : imprimir PTCOMA
                    | declaracion_normal PTCOMA
                    | condicional_ifs PTCOMA
                    | ciclo_for PTCOMA
                    | funcion PTCOMA
                    | llamada_funcion PTCOMA
                    | r_return PTCOMA
                    | asignacion PTCOMA
                    | ciclo_while PTCOMA
                    '''
    t[0] = t[1]

def p_instrucciones_evaluar_1(t):
    '''instruccion : imprimir
                    | declaracion_normal
                    | condicional_ifs
                    | ciclo_for
                    | funcion
                    | llamada_funcion
                    | r_return
                    | asignacion
                    | ciclo_while
                    '''
    t[0] = t[1]

def p_imprimir(t):
    'imprimir : RCONSOLE PUNTO RLOG PARIZQ expresion PARDER'
    t[0] = Imprimir(t[5], t.lineno(1), find_column(input, t.slice[1]))
#console.log()
def p_asignacion(t):
    'asignacion : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_normal(t):
    '''declaracion_normal : RLET ID DOSPUNTOS tipo IGUAL expresion
                            | RLET ID
                            | RLET ID DOSPUNTOS tipo
                            | RLET ID IGUAL expresion
                            '''
    if len(t) == 7:
        t[0] = Declaracion_Variables(t[2], t[4], t[6], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 3:
        t[0] = Declaracion_Variables(t[2], 'any', None, t.lineno(1), find_column(input, t.slice[1]))
    else:
        if t[3] == ":":
            t[0] = Declaracion_Variables(t[2], t[4], None, t.lineno(1), find_column(input, t.slice[1]))
        else:
            t[0] = Declaracion_Variables(t[2], 'any' , t[4], t.lineno(1), find_column(input, t.slice[1]))
        
def p_funcion(t):
    '''funcion : RFUNCTION ID PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER
               | RFUNCTION ID PARIZQ parametros PARDER LLAVEIZQ instrucciones LLAVEDER'''
    if len(t) == 8:
        t[0] = Funcion(t[2],None,t[6], t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada_funcion(t):
    '''llamada_funcion : ID PARIZQ PARDER
                       | ID PARIZQ parametros_llamada PARDER'''
    if len(t) == 4:
        t[0] = Llamada_Funcion(t[1],None,t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Llamada_Funcion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_parametros(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_2(t):
    'parametros : parametro'
    t[0] = [t[1]]

def p_parametro(t):
    '''parametro : RLET ID DOSPUNTOS tipo  
                | ID DOSPUNTOS tipo
                | ID'''
    if len(t) == 2:
        t[0] = {'tipo': 'any', 'id': t[1]}
    elif len(t) == 4:
        t[0] = {'tipo': t[3], 'id': t[1]}
    else:
        t[0] = {'tipo': t[4], 'id': t[2]}

def p_parametros_llamada(t):
    'parametros_llamada : parametros_llamada COMA parametro_ll'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_ll_2(t):
    'parametros_llamada : parametro_ll'
    t[0] = [t[1]]

def p_parametro_ll(t):
    '''parametro_ll : expresion'''
    t[0] = t[1]

def p_expresion_funcion(t):
    'expresion : llamada_funcion'
    t[0] = t[1]

def p_return(t):
    'r_return : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))


def p_condicional_ifs(t):
    'condicional_ifs : RIF condicional_if'
    t[0] = t[2]

def p_condicional_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = If(t[2], t[5], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_else(t):
    'condicional_if : PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER RELSE LLAVEIZQ instrucciones LLAVEDER'
    t[0] = If(t[2], t[5], t[9], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_else_if(t):
    'condicional_if : PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER RELSE RIF condicional_if'
    t[0] = If(t[2], t[5], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

def p_ciclo_for(t):
    'ciclo_for : RFOR PARIZQ declaracion_normal PTCOMA expresion PTCOMA expresion PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), find_column(input, t.slice[1]))
    
def p_ciclo_while(t):
    'ciclo_while : RWHILE PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = While( t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))    


def p_tipo(t):
    '''tipo : RSTRING
            | RNUMBER
            | RBOOLEAN'''
    t[0] = t[1]



def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion IGUALDAD expresion
                | expresion DESIGUALDAD expresion
                | expresion MAYORQ expresion
                | expresion MENORQ expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion AND expresion
                | expresion OR expresion
                | expresion POT expresion
                | expresion MOD expresion
                '''
    if t[2] == '+'  : 
        t[0] = Aritmetica(t[1], t[3], '+', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], '-', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmetica(t[1], t[3], '*', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '===':
        t[0] = Relacional_Logica(t[1], t[3], '===', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!==':
        t[0] = Relacional_Logica(t[1], t[3], '!==', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional_Logica(t[1], t[3], '>', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional_Logica(t[1], t[3], '<', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional_Logica(t[1], t[3], '>=', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional_Logica(t[1], t[3], '<=', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Relacional_Logica(t[1], t[3], '&&', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Relacional_Logica(t[1], t[3], '||', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^':
        t[0] = Aritmetica(t[1], t[3], '^', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], t[3], '%', t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    if t[1] == '-':
        t[0] = Aritmetica(0, t[2], '-', t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Relacional_Logica(t[2], None, '!', t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_incrementable(t):
    '''expresion : expresion MAS MAS
                | expresion MENOS MENOS'''
    if t[2] == '+':
        incrementable = Primitivos('number', 1, t.lineno(2), find_column(input, t.slice[2]))
        t[0] = Aritmetica(t[1],incrementable, '+', t.lineno(2), find_column(input, t.slice[2]))
    else:
        incrementable = Primitivos('number', 1, t.lineno(2), find_column(input, t.slice[2]))
        t[0] = Aritmetica(t[1],incrementable, '-', t.lineno(2), find_column(input, t.slice[2]))
        
    
def p_identificador(t):
    'expresion : ID'
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]), None)

def p_nulo(t):
    'expresion : RNULL'
    t[0] = Primitivos('null',None, t.lineno(1), find_column(input, t.slice[1]))

def p_any(t):
    'expresion : RANY'
    t[0] = Primitivos('any',None, t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos('number',int(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos('number',float(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos('string',str(t[1]), t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_boolean(t):
    '''expresion : RTRUE
                | RFALSE'''
    if t[1] == 'true':
        t[0] = Primitivos('boolean', True, t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Primitivos('boolean', False, t.lineno(1), find_column(input, t.slice[1]))

def p_error(t):
    print(" Error sintáctico en '%s'" % t.value)


def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

entrada = '''




let a:number;
console.log(a);

while(a<10){
    a = a + 1;
    console.log(a);
}

  
'''


def test_lexer(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


#lexer.input(entrada)
#test_lexer(lexer)
instrucciones = parse(entrada)
ast = Arbol(instrucciones)
tsg = TablaSimbolos()
ast.setTsglobal(tsg)

for instruccion in ast.getInstr():
    if isinstance(instruccion, Funcion):
        ast.setFunciones(instruccion)

for instruccion in ast.getInstr():
    if not(isinstance(instruccion, Funcion)):
        value = instruccion.interpretar(ast,tsg)
        if isinstance(value, Excepcion):
            ast.setExcepciones(value)
print(ast.getConsola())
