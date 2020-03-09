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

def iniciadora (numslice,numpizza,catlog):
    solution = []
    temp_solution = []
    start = 0
    resto = numslice
    catlog.sort()
    nosvamos = False
    pizza (numslice , numpizza , catlog , start , resto , solution , temp_solution , nosvamos)

# =============================================================================
# funcion recursiva que resuelve el problema
# =============================================================================
def pizza (numslice , numpizza , catlog , start , resto , solution , temp_solution , nosvamos):
    
    
    temp_solution=[] 
    
    for i in range (0, len(solution)) :   
        temp_solution.append(solution[i])
                    
        
    resto = numslice - sum(solution)
    
    
    if resto in catlog[start : ] and resto >= 0:
       
        solution.append(resto)
        K = len(solution)
        slicesgot = sum (solution)
        print( 'solution is = ',solution , ' number of pizzas is = ' , K , ' slices ordered are = ' , slicesgot )
        nosvamos = True
        return
    else:
        
        if not resto < 0 :
            solution.append(catlog[start])
            start += 1
            if not start == len (catlog) :
                pizza (numslice , numpizza , catlog , start , resto , solution , temp_solution , nosvamos)
            else:
                
                if  sum(temp_solution) >= sum (solution) :
                    K = len(temp_solution)
                    slicesgot = sum (temp_solution)
                    for i in range (0, len(solution)) :   
                        solution[i]= temp_solution[i]
                    return 
                else:
                    return 
            resto += catlog[start] + catlog[start-1]
            start = start - 1
            print(solution)
            if not nosvamos == True :
                solution.pop(start-1)
                solution.pop(start-2)
                pizza (numslice , numpizza , catlog , start , resto , solution , temp_solution , nosvamos)
            else:
                return
        else:
            
            if  sum(temp_solution) >= sum(solution) :
                K = len(temp_solution)
                slicesgot = sum (temp_solution)
                for i in range (0, len(solution)) :   
                    solution[i]= temp_solution[i]
                return 
            else:
                return 
            resto += catlog[start] + catlog[start-1]
            start = start - 1
            print(solution)
            solution.pop(start-1)
            solution.pop(start-2)
            pizza (numslice , numpizza , catlog , start , resto , solution , temp_solution , nosvamos)
        return

#fragmento no ejecutable del modulo , unicamente para pruebas , a modo de generador de 
# problemas alaeatorios
if __name__ == "__main__":
    numslice = randrange(15,50)
    numpizza = randrange(5,15)
    catlog = [0]*numpizza
    for i in range(0,numpizza) :
        catlog[i]= randrange(1,15)
    print('initial data' , numslice,numpizza,catlog)    
    iniciadora (numslice,numpizza,catlog)