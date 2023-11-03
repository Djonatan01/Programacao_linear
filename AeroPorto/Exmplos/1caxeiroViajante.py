import numpy as np
import random as rd

#Gerar as matriz
def Gerar_Problema ():

    matriz1 = np.array([

    [0, 365, 1020, 586, 2101, 2353, 2767, 3346, 875, 991],
    [365, 0, 1175, 397, 1987, 2605, 3018, 3554, 1229, 1167],
    [1020, 1175, 0, 716, 1445, 2043, 2453, 3424, 2117, 1707],
    [586, 397, 716, 0, 1480, 2087, 2505, 3172, 915, 586],
    [2101, 1987, 1445, 1480, 0, 800, 973, 2931, 3651, 2753],
    [2353, 2605, 2043, 2087, 800, 0, 629, 3552, 4060, 3155],
    [2767, 3018, 2453, 2505, 973, 629, 0, 3022, 4609, 3674],
    [3346, 3554, 3424, 3172, 2931, 3552, 3022, 0, 4575, 3960],
    [875, 1229, 2117, 915, 3651, 4060, 4609, 4575, 0, 501],
    [991, 1167, 1707, 586, 2753, 3155, 3674, 3960, 501, 0]])

    return matriz1

def Avalia(n,s,m1):
    valor = 0
    for i in range(0,n-1):
      valor += m1[s[i]][s[i+1]]
      print("-"*10,i,valor)
    valor += m1[s[n-1]][s[0]]
    print("-"*10,i,valor)

    return valor

def Solucao_Inicial(n):
    """
    s = []
    for i in range(n):
        s.append(i)
    rd.shuffle(s)
    print("Solução inicial: ",s)
    """
    s = [9, 7, 4, 3, 8, 2, 1, 5, 0, 6]
    return s

def calcular_rota ():
    mat1 = Gerar_Problema()
    print("Matriz de Adjacências para o Problema", mat1)
    return(mat1)
