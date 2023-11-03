import numpy as np
import random as rd
import copy as cp

#Gerar as matriz
def Gerar_Problema (_Elementos,valorMnimoM1,valorMaximoM1):
    matriz1 = np.zeros((_Elementos,_Elementos),int)
    for i in range(_Elementos):
        for j in range(_Elementos):
            if i!=j:
                matriz1[i][j] = rd.randint(valorMnimoM1,valorMaximoM1)
    return matriz1

def Avalia(n,s,m1):
    valor = 0
    for i in range(0,n-1):
      valor += m1[s[i]][s[i+1]]
    valor += m1[s[n-1]][s[0]]
    return valor

def Solucao_Inicial(n):
    s = []
    for i in range(n):
        s.append(i)
    rd.shuffle(s)
    return s

def encosta(solucao_inicial, matriz1, valor):
  atual = cp.deepcopy(solucao_inicial)
  va = valor

  while True:
    novo, vn = sucessores_enc(atual, matriz1, va)

    if vn >= va:
        return atual, va
    else:
        atual = novo
        va = vn

def sucessores_enc(solucao_inicial, matriz1, valor):
        melhor = cp.deepcopy(solucao_inicial)
        vm = valor
        c = rd.randrange(0, len(solucao_inicial))
        print("\nCidade:",c)
        for i in range(len(solucao_inicial)):
            aux = cp.deepcopy(solucao_inicial)
            x = aux[c]
            aux[c] = aux[i]
            aux[i] = x
            _aux = cp.deepcopy(aux)
            print("AUX:  ", _aux)
            valor_aux = Avalia(len(solucao_inicial),_aux, matriz1 )

            if valor_aux < vm:
                melhor = aux
                vm = valor_aux
                print("MELHOR",melhor)
                print("Valor Melhor", vm)
        return melhor, vm


def encostaAlterada(solucao_inicial, matriz1, valor):
  atual = cp.deepcopy(solucao_inicial)
  va = valor
  tmax = 3
  t = 0
  while True:
    novo, vn = sucessores_enc_alterada(atual, matriz1, va)
    if vn >= va:
        if t <= tmax:
          t += 1
          return atual, va
    else:
        atual = novo
        va = vn
        t = 0

def sucessores_enc_alterada(solucao_inicial, matriz1, valor):
        melhor = cp.deepcopy(solucao_inicial)
        vm = valor
        c = rd.randrange(0, len(solucao_inicial))
        print("\nCidade:",c)
        for i in range(len(solucao_inicial)):
            aux = cp.deepcopy(solucao_inicial)
            x = aux[c]
            aux[c] = aux[i]
            aux[i] = x
            _aux = cp.deepcopy(aux)
            print("AUX:  ", _aux)
            valor_aux = Avalia(len(solucao_inicial),_aux, matriz1 )

            if valor_aux < vm:
                melhor = aux
                vm = valor_aux
                print("MELHOR",melhor)
                print("Valor Melhor", vm)
        return melhor, vm

def calcular_rota (_Elementos,valorMnimoM1,valorMaximoM1):
    mat1 = Gerar_Problema(_Elementos,valorMnimoM1,valorMaximoM1)
    print("Matriz de Adjacências para o Problema")
    print("\nMatriz")
    print(mat1)

    si = Solucao_Inicial(_Elementos)
    vi = Avalia(_Elementos,si,mat1)
    _atual, _va = encosta(si,mat1,vi)

    print("\nSolução inicial",si)
    print("Valor da solução inicial: ",vi)
    print("\nSubida de encosta")
    print("Solução atual: ", _atual)
    print("Valor atual: ", _va)

    print("\nSubida de encosta alterada")
    _atualAlterada, _vaAlterada = encostaAlterada(si,mat1,vi)
    print("Solução atual: ", _atualAlterada)
    print("Valor atual: ", _vaAlterada)

    return si , vi, _atual , _va, _atualAlterada, _vaAlterada