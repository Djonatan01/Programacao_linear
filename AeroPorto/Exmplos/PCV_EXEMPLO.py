import random as rd
import copy   as cp
import math   as ma

def Gerar_Problema(n,me1,ma1,me2,ma2):

    m1 = [[0,2,2,3,4,5],
          [1,0,4,3,2,9],
          [1,3,0,4,3,2],
          [8,2,4,0,5,5],
          [5,6,2,1,0,3],
          [2,3,4,3,4,0]
         ]
    return m1

def Avalia(n,s,m1):
    valor = 0
    for i in range(0,n-1):
      valor += m1[s[i]-1][s[i+1]-1]
    valor += m1[s[n-1]-1][s[0]-1]
    return valor

def Solucao_Inicial(n):
    s = [6,4,5,1,2,3]
    return s
'''
def sucessores(atual,va,n,m1):
    melhor = cp.deepcopy(atual)
    vm     = va
    ind    = rd.randrange(n)
    for i in range(n):
        suc = cp.deepcopy(atual)
        aux      = suc[i]
        suc[i]   = suc[ind]
        suc[ind] = aux
        vs = Avalia(n,suc,m1)
        if vs<vm:
            melhor = cp.deepcopy(suc)
            vm = vs
    return melhor, vm

def sucessores1(atual,va,n,m1,cid):
    melhor = cp.deepcopy(atual)
    vm     = va
    ind    = cid.pop()
    for i in range(n):
        suc = cp.deepcopy(atual)
        aux      = suc[i]
        suc[i]   = suc[ind]
        suc[ind] = aux
        vs = Avalia(n,suc,m1)
        if vs<vm:
            melhor = cp.deepcopy(suc)
            vm = vs
    return melhor, vm
'''

'''
def sub_encosta(si,vi,n,m1):
    atual = cp.deepcopy(si)
    va = vi
    while True:
        novo, vn = sucessores(atual,va,n,m1)
        if vn>=va:
            return atual, va
        atual = cp.deepcopy(novo)
        va = vn

def sub_encosta1(si,vi,n,m1,tmax): ####
    atual = cp.deepcopy(si)
    va = vi
    t = 1
    cidades = []
    for i in range(n):
        cidades.append(i)
    rd.shuffle(cidades)
    while True:
        novo, vn = sucessores2(atual,va,n,m1,cidades)
        if vn>=va:
            if t>tmax:
                return atual, va
            else:
                t = t + 1
        else:
            atual = cp.deepcopy(novo)
            va = vn
            t = 1
            cidades = []
            for i in range(n):
                cidades.append(i)
            rd.shuffle(cidades)
'''
def tempera(si,vi,n,m1,t_ini,t_fim,fr,ind1,ind2):
    atual = cp.deepcopy(si)
    aux   = cp.deepcopy(si)
    va    = vi
    vaux  = vi
    t = t_ini

    while t>t_fim:
        novo, vn = sucessores2(atual,va,n,m1,ind1,ind2)
        print(30 * "*")
        print("prox = ",novo)
        print("Vp = ",vn)
        de = vn - va
        if de>=0:
            ale = float(input("Informe valor do ALE\n"))
            #ale = rd.uniform(0,1)
            auxiliar = float(ma.exp(-de/t))
            print("AUX = ",auxiliar)
            if ale<=auxiliar:
               atual = cp.deepcopy(novo)
               va = vn
        else:
            ale=0
            auxiliar=0
            print("ALE = ",ale)
            print("AUX = ",auxiliar)
            atual = cp.deepcopy(novo)
            va = vn
        t = t*fr
        print("temperatura = ",t)

        ind1 = int(input("Informe a prineira posição\n")) - 1
        ind2 = int(input("Informe a segunda posição\n")) - 1
    return aux, vaux

def sucessores2(atual,va,n,m1,ind1,ind2):
    suc   = cp.deepcopy(atual)
    aux       = suc[ind1]
    suc[ind1] = suc[ind2]
    suc[ind2] = aux
    vs = Avalia(n,suc,m1)
    return suc, vs

# MÓDULO PRINCIPAL
N    = 8    # TAMANHO DO PROBLEMA
MIN1 = 10   # VALOR MÍNIMO PARA O CUSTO ENTRE PONTOS
MAX1 = 30   # VALOR MÁXIMO PARA O CUSTO ENTRE PONTOS
MIN2 = 2    # VALOR MÍNIMO PARA O CUSTO ENTRE PONTOS
MAX2 = 8    # VALOR MÁXIMO PARA O CUSTO ENTRE PONTOS

mat1 = Gerar_Problema(N,MIN1,MAX1,MIN2,MAX2)

si=[]
si = input("Informe a solução, separando os elementos por vírgula:\n")
si_list = [int(x) for x in si.split(',')]
si = si_list

temp = float(input("Informe a temperatura\n"))
vi = int(input("Informe valor inicial\n"))
redutor = 0.8
ind1 = int(input("Informe a prineira posição\n")) - 1
ind2 = int(input("Informe a segunda posição\n")) - 1

t_fim=0
print("Matriz de Adjacências para o Problema\n",mat1)
print("Lista de soluções:\n", si_list)
print("Valor da solução inicial....:\n",vi)
vp = tempera(si,vi,len(si),mat1,temp,t_fim,redutor,ind1,ind2)

print(vp)
