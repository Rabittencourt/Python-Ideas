# Algoritmo de Localizador de String
#Desenvolvido por Rafael Almeida Bittencourt e Gustavo Amaral Matias Costa
import math
from pythonds.basic.stack import Stack
def divideBy2(decNumber):  #função para converter um número de notação decimal para binária
    remstack = Stack()
    if decNumber == 0:
        return str(decNumber)
    else:
        while decNumber > 0:
            rem = decNumber % 2
            remstack.push(rem)
            decNumber = decNumber // 2

        binString = ""
        while not remstack.isEmpty():
            binString = binString + str(remstack.pop())

        return binString
i=int(input('Digite qual o número da string que deseja buscar: '))
if i == 0:
    print(f'A cadeia escolhida é a vazia (epsilon)')
else:
    numcar = int((math.log(i+1,10))/(math.log(2,10))) # Determina o número de caracteres
    marco = 2**numcar-1 #Determina o marco inferior, ou seja, o número ao qual o novo número de caracter começa
    decnum = i - marco #Calcula a diferença entre o número escolhido e o marco inferior, em notação decimal
    binnum = divideBy2(decnum) # Função que converte o resultado da diferença acima em notação binária.
    difcar = numcar - len(binnum)
    contador = 0
    for n in range(0,difcar): # esse 'for' serve para adicionar 0's para que o numero binário tenha o mesmo número de caractres da posição
        contador = contador + 1
        binnum = str(0) + str(binnum)
    listabin = [] # Lista onde serão alocados os dígitos do binário
    listabin.extend(binnum) # Adicionamos os caracteres da cadeira binaria nesta lista
    for n in range(0,numcar): # A partir daqui mudaremos os símbolos {0,1} para {a,b}
        if listabin[n] == "0":
            listabin[n] = "a"
        else:
            listabin[n] = "b"
    listaalfa = listabin
    cadeia = ''.join(listaalfa) # Aqui colocamos os elementos da lista contendo símbolos a e b, para uma cadeia.
    print(f'A cadeia escolhida foi: {cadeia}')



