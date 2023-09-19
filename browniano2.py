import matplotlib.pyplot as plt
import random


def simulation(num_pelotas,num_cajas):
    positions = []
    num_filas = 12
    for o in range(num_cajas):
        positions.append(0)

    for s in range(num_pelotas): #numero de pelotas
        izq = 0
        der = 0
        for a in range(num_filas): #iteraciones
            side = random.randint(0,1)
            if (a == 4 and izq == len(positions)-1) or (a == 6 and izq == len(positions)) or (a == 8 and izq == len(positions)+1):
                side = 1
                der +=1
            else:
                if side == 0:
                    izq += 1
                   
            if (a == 4 and der == len(positions)-1) or (a == 6 and der == len(positions)) or (a == 8 and der == len(positions)+1):
                side = 0
                izq +=1
            else:
                if side == 1:
                    der += 1  
           
        for i in range(num_cajas):
            if izq == (len(positions)+1-i):
                positions[i] += 1
            
    # print(positions)            
    return positions

#print(simulation(100,9))

positions = simulation(10000,9)

# Crear una gráfica de barras
plt.bar(range(len(positions)), positions)
plt.xlabel('Posición')
plt.ylabel('Frecuencia')
plt.title('Distribución de pelotas en la máquina de Galton')
plt.xticks(range(len(positions)))
plt.show()