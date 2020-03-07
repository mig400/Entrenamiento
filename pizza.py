# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:22:14 2020

@author: Miguel_Ángel
"""
#  recibe un numero de trozos de pizza maximos a encargar (numslice) , recibe el
#  recibe el numero de pizzas disponibles en catalogo
#  recibes el catalogo de pizzas con el numero de trozos que tiene cada una (tamaños)
#  buscamos como primera prioridad asegurar que el numslices es el correcto eligiendo 
#  eligiendo apropiadamente las pizzas , como segunda prioridad tenemos 
#  que la variedad de pizzas elegidaas sea la mayor posible
#  hay que hallar la selección de pizzas más apropiada y devolver el numero de pizzas
#  elegidas y que numero de catalogo que son

# nota importante , no se puede repetir el tipo de pizza




# =============================================================================
#  modulos involucrados
# =============================================================================
from random import randrange 

# =============================================================================
# funcion de coste , evalua lo optima que es la solucion
# =============================================================================
def cost_func (K,order,numslice):
    cost = abs(numslice-sum(order))/K
    return cost,K
# =============================================================================
# funcion que resuelve el problema
# =============================================================================

def pizza (numslice,numpizza,catlog):
    
    for i in range(0,numpizza):
        
    # variables de salida
        Kopt=0
        order_opt = [0]*numpizza
    #variables internas
        K = 0
        order = []
        cost_vec = [0]*numpizza
        K_vec = [0]*numpizza
        winner = []
        winner_index = []
    # seleccion de las pizzas
    
    # llamada a la funcion de coste
        cost_vec[i], K_vec[i] = cost_func (K,order,numslice)
    # selección de la mejor solucion al problema
    minval =  min(cost_vec)
    for i in range(0,numpizza):
        if  cost_vec[i] == minval:
            winner.append(K_vec[i])
            winner_index.append(i)
    Kopt = K_vec[winner.index(max(winner))]
    
    return Kopt , order_opt  
    
    
    
#fragmento no ejecutable del modulo , unicamente para pruebas , a modo de generador de 
# problemas alaeatorios
if __name__ == "__main__":
    numslice = randrange(50)
    numpizza = randrange(10,30)
    catlog = [0]*numpizza
    for i in range(0,numpizza) :
        catlog[i]= randrange(1,15)
    print(numslice,numpizza,catlog)    
    pizza (numslice,numpizza,catlog)