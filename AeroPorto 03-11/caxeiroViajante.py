import numpy as np
import random as rd
import copy as cp
import math   as ma

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
#********************Inicio subida encosta***************************
def encosta(solucao_inicial, matriz1, valor):
  atual = cp.deepcopy(solucao_inicial)
  va = valor

  while True:
    novo, vn = sucessores_enc(atual, matriz1, va)
    if vn >= va:
        return atual, va
    else:
        atual = cp.deepcopy(novo)
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
#********************Inicio subida encosta alterada***************************
def encostaAlterada(solucao_inicial, matriz1, valor):
  atual = cp.deepcopy(solucao_inicial)
  va = valor
  tmax = len(solucao_inicial) - 1
  t = 0
  while True:
    novo, vn = sucessores_enc_alterada(atual, matriz1, va)
    if vn >= va:
        if t >= tmax:
          return atual, va
        else:
          t += 1
    else:
        atual = cp.deepcopy(novo)
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

#********************Inicio tempera simulada***************************
def tempera(si,vi,n,m1,t_ini,t_fim,fr):
  atual = cp.deepcopy(si)
  aux   = cp.deepcopy(si)
  va    = vi
  vaux  = vi
  t = t_ini

  while t>t_fim:
      novo, vn = sucessores2(atual,va,n,m1)
      de = vn - va
      if de>=0:
          ale = rd.uniform(0,1)
          auxiliar = ma.exp(-de/t)
          if ale<=auxiliar:
             atual = cp.deepcopy(novo)
             va = vn
      else:
          atual = cp.deepcopy(novo)
          va = vn
      if va<vaux:
          aux = cp.deepcopy(atual)
          vaux  = va

      t = t*fr

  return aux, vaux

def sucessores2(atual,va,n,m1):
  suc   = cp.deepcopy(atual)
  ind1  = rd.randrange(n)
  ind2  = rd.randrange(n)
  while ind1==ind2:
      ind2  = rd.randrange(n)

  aux       = suc[ind1]
  suc[ind1] = suc[ind2]
  suc[ind2] = aux
  vs = Avalia(n,suc,m1)
  return suc, vs

def Gera_Temp(n,m1):
  qt = 10
  de = 0
  v = []
  c = 0

  for i in range(qt):
      sol = Solucao_Inicial(n)
      v.append(Avalia(n,sol,m1))

  for i in range(qt-1):
      for j in range(i,qt):
          de += ma.fabs(v[i] - v[j])
          c += 1
  de = float(de/c)

  temp = -de/ma.log(0.999)

  return temp
#********************Fim tempera simulada***************************

def calcular_rota_todas (_Elementos,valorMnimoM1,valorMaximoM1,fr):
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
    print("\nSubida de encosta alterada")
    print("Solução atual: ", _atualAlterada)
    print("Valor atual: ", _vaAlterada)

    # MÉTODO TÊMPERA SIMULADA
    t_ini = Gera_Temp(len(si),mat1)
    t_fim = 0.01
    sf, vf = tempera(si,vi,len(si),mat1,t_ini,t_fim,fr)
    print("\nTêmpera Simulada com Fator red. 0.8....................:",vf)

    return si , vi, _atual , _va, _atualAlterada, _vaAlterada , sf, vf

def calcularSubidaEncosta (_Elementos,valorMnimoM1,valorMaximoM1):
    mat1 = Gerar_Problema(_Elementos,valorMnimoM1,valorMaximoM1)
    print("Matriz de Adjacências para o Problema")
    print("\nMatriz")
    print(mat1)

    si = Solucao_Inicial(_Elementos)
    vi = Avalia(_Elementos,si,mat1)
    _atual, _va = encosta(si,mat1,vi)

    return si , vi, _atual , _va

def calculoSubidaAlterada (_Elementos,valorMnimoM1,valorMaximoM1):
    mat1 = Gerar_Problema(_Elementos,valorMnimoM1,valorMaximoM1)
    print("Matriz de Adjacências para o Problema")
    print("\nMatriz")
    print(mat1)

    si = Solucao_Inicial(_Elementos)
    vi = Avalia(_Elementos,si,mat1)

    print("\nSolução inicial",si)
    print("Valor da solução inicial: ",vi)

    print("\nSubida de encosta alterada")
    _atualAlterada, _vaAlterada = encostaAlterada(si,mat1,vi)
    print("\nSubida de encosta alterada")
    print("Solução atual: ", _atualAlterada)
    print("Valor atual: ", _vaAlterada)

    return si , vi,_atualAlterada, _vaAlterada

def calcularTempera (_Elementos,valorMnimoM1,valorMaximoM1,fr):

    mat1 = Gerar_Problema(_Elementos,valorMnimoM1,valorMaximoM1)
    print("Matriz de Adjacências para o Problema")
    print("\nMatriz")
    print(mat1)

    si = Solucao_Inicial(_Elementos)
    vi = Avalia(_Elementos,si,mat1)

    print("\nSolução inicial",si)
    print("Valor da solução inicial: ",vi)

    # MÉTODO TÊMPERA SIMULADA
    t_ini = Gera_Temp(len(si),mat1)

    t_fim = 0.01
    sf, vf = tempera(si,vi,len(si),mat1,t_ini,t_fim,fr)
    print("\nTêmpera Simulada com Fator red. 0.8....................:",vf)

    return si , vi, sf, vf