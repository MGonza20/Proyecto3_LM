## Diagrama de máquina de estado finito

![AFD](https://user-images.githubusercontent.com/64711979/194376349-2d5c9b30-2566-420d-9db7-12a5c66058ed.png)

## Producciones


- 0 -> ~1 
- 0 -> ~ 
________
- 0 -> ^2
- 0 -> ^ 
________
- 0 -> =3
- 3 -> >4
- 3 -> >
________
- 0 -> o5
- 0 -> o
________
- 0 -> <6 
- 6 -> =7
- 7 -> >8
- 7 -> >
________
- 0 -> p9
- 0 -> q9
- 0 -> r9
- 0 -> s9
- 0 -> t9
- 0 -> u9
- 0 -> w9
- 0 -> x9
- 0 -> y9
- 0 -> z9
- 0 -> 19
- 0 -> 09
- 0 -> p
- 0 -> q
- 0 -> r
- 0 -> s
- 0 -> t
- 0 -> u
- 0 -> w
- 0 -> x
- 0 -> y
- 0 -> z 
- 0 -> 1
- 0 -> 0 

## Componentes de la Gramática

- N = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
- T = {~, ^, <, =, >, p, q, r, s, t, u, v, w, x, y, z, 1, 0}
- S = 0

## Representación de elementos en el código

- t_NOT = ~
- t_AND = ^
- t_OR = o
- t_IMP =>
- t_DIMP <=>
- t_LPAREN  = (
- t_RPAREN  = )

## Captura de pantalla de reconocimiento de expresión: ((p=>q)^q)
![reconocimiento-expresión](https://user-images.githubusercontent.com/64711979/194381994-efcbed8c-47e4-4b58-9e66-8041eb3b755e.png)
