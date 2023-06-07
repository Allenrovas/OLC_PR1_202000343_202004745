
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVleftPARIZQPARDERrightUMENOSAND CADENA CORDER CORIZQ DECIMAL DESIGUALDAD DIV DOSPUNTOS ENTERO ID IGUAL IGUALDAD LLAVEDER LLAVEIZQ MAS MAYORIGUAL MAYORQ MENORIGUAL MENORQ MENOS MOD NOT OR PARDER PARIZQ POR POT PTCOMA PUNTO RANY RBOOLEAN RBREAK RCONCAT RCONSOLE RCONTINUE RELSE RFALSE RFOR RFUNCTION RIF RINTERFACE RLET RLOG RNULL RNUMBER RRETURN RSPLIT RSTRING RTOEXPONENTIAL RTOFIXED RTOLOWERCASE RTOSTRING RTRUE RTUPPERCASE RWHILEinit : instruccionesinstrucciones    : instrucciones instruccioninstrucciones : instruccioninstruccion : imprimir PTCOMA\n                    | declaracion PTCOMA\n                    | condicional_if PTCOMA\n    imprimir : RCONSOLE PUNTO RLOG PARIZQ expresion PARDERdeclaracion : RLET ID DOSPUNTOS tipo IGUAL expresioncondicional_if : RIF PARIZQ expresion PARDER LLAVEIZQ LLAVEDERtipo : RSTRING\n            | RNUMBER\n            | RBOOLEANexpresion : expresion MAS expresion\n                | expresion MENOS expresion\n                | expresion POR expresion\n                | expresion DIV expresionexpresion : MENOS expresion %prec UMENOSexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : RTRUE\n                | RFALSE'
    
_lr_action_items = {'RCONSOLE':([0,2,3,10,11,12,13,],[7,7,-3,-2,-4,-5,-6,]),'RLET':([0,2,3,10,11,12,13,],[8,8,-3,-2,-4,-5,-6,]),'RIF':([0,2,3,10,11,12,13,],[9,9,-3,-2,-4,-5,-6,]),'$end':([1,2,3,10,11,12,13,],[0,-1,-3,-2,-4,-5,-6,]),'PTCOMA':([4,5,6,21,22,23,24,25,36,40,41,42,43,44,45,46,],[11,12,13,-18,-19,-20,-21,-22,-17,-13,-14,-15,-16,-7,-8,-9,]),'PUNTO':([7,],[14,]),'ID':([8,],[15,]),'PARIZQ':([9,17,],[16,26,]),'RLOG':([14,],[17,]),'DOSPUNTOS':([15,],[18,]),'MENOS':([16,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,40,41,42,43,45,],[20,33,20,-18,-19,-20,-21,-22,20,20,20,20,20,-17,33,20,-13,-14,-15,-16,33,]),'ENTERO':([16,20,26,32,33,34,35,38,],[21,21,21,21,21,21,21,21,]),'DECIMAL':([16,20,26,32,33,34,35,38,],[22,22,22,22,22,22,22,22,]),'CADENA':([16,20,26,32,33,34,35,38,],[23,23,23,23,23,23,23,23,]),'RTRUE':([16,20,26,32,33,34,35,38,],[24,24,24,24,24,24,24,24,]),'RFALSE':([16,20,26,32,33,34,35,38,],[25,25,25,25,25,25,25,25,]),'RSTRING':([18,],[28,]),'RNUMBER':([18,],[29,]),'RBOOLEAN':([18,],[30,]),'PARDER':([19,21,22,23,24,25,36,37,40,41,42,43,],[31,-18,-19,-20,-21,-22,-17,44,-13,-14,-15,-16,]),'MAS':([19,21,22,23,24,25,36,37,40,41,42,43,45,],[32,-18,-19,-20,-21,-22,-17,32,-13,-14,-15,-16,32,]),'POR':([19,21,22,23,24,25,36,37,40,41,42,43,45,],[34,-18,-19,-20,-21,-22,-17,34,34,34,-15,-16,34,]),'DIV':([19,21,22,23,24,25,36,37,40,41,42,43,45,],[35,-18,-19,-20,-21,-22,-17,35,35,35,-15,-16,35,]),'IGUAL':([27,28,29,30,],[38,-10,-11,-12,]),'LLAVEIZQ':([31,],[39,]),'LLAVEDER':([39,],[46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,10,]),'imprimir':([0,2,],[4,4,]),'declaracion':([0,2,],[5,5,]),'condicional_if':([0,2,],[6,6,]),'expresion':([16,20,26,32,33,34,35,38,],[19,36,37,40,41,42,43,45,]),'tipo':([18,],[27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','AnalizadorSintactico.py',18),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','AnalizadorSintactico.py',22),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_2','AnalizadorSintactico.py',28),
  ('instruccion -> imprimir PTCOMA','instruccion',2,'p_instrucciones_evaluar','AnalizadorSintactico.py',35),
  ('instruccion -> declaracion PTCOMA','instruccion',2,'p_instrucciones_evaluar','AnalizadorSintactico.py',36),
  ('instruccion -> condicional_if PTCOMA','instruccion',2,'p_instrucciones_evaluar','AnalizadorSintactico.py',37),
  ('imprimir -> RCONSOLE PUNTO RLOG PARIZQ expresion PARDER','imprimir',6,'p_imprimir','AnalizadorSintactico.py',42),
  ('declaracion -> RLET ID DOSPUNTOS tipo IGUAL expresion','declaracion',6,'p_declaracion','AnalizadorSintactico.py',46),
  ('condicional_if -> RIF PARIZQ expresion PARDER LLAVEIZQ LLAVEDER','condicional_if',6,'p_condicional_if','AnalizadorSintactico.py',51),
  ('tipo -> RSTRING','tipo',1,'p_tipo','AnalizadorSintactico.py',56),
  ('tipo -> RNUMBER','tipo',1,'p_tipo','AnalizadorSintactico.py',57),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','AnalizadorSintactico.py',58),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',64),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',65),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',66),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','AnalizadorSintactico.py',67),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','AnalizadorSintactico.py',78),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','AnalizadorSintactico.py',82),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','AnalizadorSintactico.py',86),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','AnalizadorSintactico.py',90),
  ('expresion -> RTRUE','expresion',1,'p_expresion_boolean','AnalizadorSintactico.py',95),
  ('expresion -> RFALSE','expresion',1,'p_expresion_boolean','AnalizadorSintactico.py',96),
]