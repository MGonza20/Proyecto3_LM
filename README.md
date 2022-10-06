## Componentes de la Gramatica
- T = {p,q,r,s,t,u,v,w,x,y,z,1,0}
- NT = {LPAREN,RPAREN,NOT,IM,OR,AND,DIMP, factor, VARIABLE, expression, term}
- S = expression
- P:
  - expression => term
  - term => factor
  - factor => VARIABLE
  - factor => LPAREN expression RPAREN
  - VARIABLE => p|q|r|s|t|u|v|w|x|y|z|1|0
  - expression => expression DIMP expression
  - expression => expression IMP expression
  - expression => NOT expression
  - expression => expression OR term
  - expression => expression AND term

 
