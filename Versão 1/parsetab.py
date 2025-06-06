
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*concat entrada escrever num string varidZ : LstV ';'LstV : VLstV : LstV ';' VV : varid '=' EV : escrever EE : E '+' E\n               | E '-' E\n               | E '*' EE : '(' E ')'E : numE : varidE : stringE : E concat EE : entrada '(' ')'"
    
_lr_action_items = {'varid':([0,5,6,7,9,16,17,18,19,],[4,11,4,11,11,11,11,11,11,]),'escrever':([0,6,],[5,5,]),'$end':([1,6,],[0,-1,]),';':([2,3,8,10,11,12,14,15,22,23,24,25,26,27,],[6,-2,-5,-10,-11,-12,-3,-4,-6,-7,-8,-13,-9,-14,]),'=':([4,],[7,]),'(':([5,7,9,13,16,17,18,19,],[9,9,9,21,9,9,9,9,]),'num':([5,7,9,16,17,18,19,],[10,10,10,10,10,10,10,]),'string':([5,7,9,16,17,18,19,],[12,12,12,12,12,12,12,]),'entrada':([5,7,9,16,17,18,19,],[13,13,13,13,13,13,13,]),'+':([8,10,11,12,15,20,22,23,24,25,26,27,],[16,-10,-11,-12,16,16,-6,-7,-8,16,-9,-14,]),'-':([8,10,11,12,15,20,22,23,24,25,26,27,],[17,-10,-11,-12,17,17,-6,-7,-8,17,-9,-14,]),'*':([8,10,11,12,15,20,22,23,24,25,26,27,],[18,-10,-11,-12,18,18,18,18,-8,18,-9,-14,]),'concat':([8,10,11,12,15,20,22,23,24,25,26,27,],[19,-10,-11,-12,19,19,-6,-7,-8,19,-9,-14,]),')':([10,11,12,20,21,22,23,24,25,26,27,],[-10,-11,-12,26,27,-6,-7,-8,-13,-9,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Z':([0,],[1,]),'LstV':([0,],[2,]),'V':([0,6,],[3,14,]),'E':([5,7,9,16,17,18,19,],[8,15,20,22,23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Z","S'",1,None,None,None),
  ('Z -> LstV ;','Z',2,'p_z','fca_grammar.py',26),
  ('LstV -> V','LstV',1,'p_lstv_head','fca_grammar.py',30),
  ('LstV -> LstV ; V','LstV',3,'p_lstv_tail','fca_grammar.py',34),
  ('V -> varid = E','V',3,'p_atrib','fca_grammar.py',40),
  ('V -> escrever E','V',2,'p_esc','fca_grammar.py',44),
  ('E -> E + E','E',3,'p_expr_op','fca_grammar.py',48),
  ('E -> E - E','E',3,'p_expr_op','fca_grammar.py',49),
  ('E -> E * E','E',3,'p_expr_op','fca_grammar.py',50),
  ('E -> ( E )','E',3,'p_expr_pare','fca_grammar.py',54),
  ('E -> num','E',1,'p_expr_num','fca_grammar.py',58),
  ('E -> varid','E',1,'p_expr_var','fca_grammar.py',62),
  ('E -> string','E',1,'p_expr_string','fca_grammar.py',66),
  ('E -> E concat E','E',3,'p_expr_concat','fca_grammar.py',70),
  ('E -> entrada ( )','E',3,'p_expr_entrada','fca_grammar.py',74),
]
