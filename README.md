# dojo-numeros-romanos
Conversor de n�meros inteiros para romanos e vice-versa.

Dojo retirado de: http://dojopuzzles.com/problemas/exibe/numeros-romanos/

### O Problema

O sistema de numera��o romana (ou n�meros romanos) desenvolveu-se na Roma Antiga e utilizou-se em todo o seu Imp�rio.
Neste sistema as cifras escrevem-se com determinadas letras, que representam os n�meros. As letras s�o sempre
mai�sculas, j� que no alfabeto romano n�o existem as min�sculas, as letras s�o I, V, X, L, C, D e M.
Sua tarefa � desenvolver um programa que converta n�meros indo-ar�bicos para o formato romano e vice-versa.

As regras para a forma��o dos n�meros romanos s�o apresentadas a seguir.
Cada letra corresponde a um determinado valor:
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Agrupando as letras acima, podemos representar os n�meros de acordo com um conjunto de regras:
Com exce��o de V, L e D, os outros numerais podem se repetir no m�ximo tr�s vezes:
III = 3
XXX = 30
CCC = 300
MMM = 3000

Quando escritos � direita de numerais maiores, I, X e C somam-se aos valores dos primeiros:
VIII = 5 + 1 + 1 + 1 = 8
LXII = 50 + 10 + 1 + 1 = 62
CLVIII = 158
MCXX = 1000 + 100 + 10 + 10 = 1120

Mas se os numerais I, X e C estiverem � esquerda dos maiores, seus valores s�o subtra�dos como, por exemplo, em:
IV = 5 - 1 = 4
IX = 10 - 1 = 9
XC = 100 - 10 = 90
