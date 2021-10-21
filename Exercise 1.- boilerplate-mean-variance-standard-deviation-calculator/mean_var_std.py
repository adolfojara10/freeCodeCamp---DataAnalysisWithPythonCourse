import numpy as np

def calculate(list):

  try:
    matriz = np.array(list).reshape(3,3)
    mean = []
    
    mean.append(matriz.mean(axis=0))
    mean.append(matriz.mean(axis=1))
    mean.append(matriz.mean())


    variance = []
    variance.append(matriz.var(axis=0))
    variance.append(matriz.var(axis=1))
    variance.append(matriz.var())


    stde = []
    stde.append(matriz.std(axis=0))
    stde.append(matriz.std(axis=1))
    stde.append(matriz.std())
    
    maximum =[]
    maximum.append(matriz.max(axis=0))
    maximum.append(matriz.max(axis=1))
    maximum.append(matriz.max())

    minimum = []
    minimum.append(matriz.min(axis=0))
    minimum.append(matriz.min(axis=1))
    minimum.append(matriz.min())

    suma=[]
    suma.append(matriz.sum(axis=0))
    suma.append(matriz.sum(axis=1))
    suma.append(matriz.sum())

    calculations ={'mean' : mean, 'var' : variance,    'standard deviation' : stde, 'max' : maximum, 'min' : minimum, 'sum' : suma
    }

    return calculations

  except (ValueError):
    print("List must contain nine numbers.")

    