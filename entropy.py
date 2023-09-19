import math

def calcular_entropia_dado():
    num_caras = 6
    probabilidad_individual = 1 / num_caras  # Probabilidad de obtener una cara específica
    entropia = 0
    
    for x in range(num_caras):
        entropia += probabilidad_individual * math.log2(1 / probabilidad_individual)

    return entropia

entropia_dado = calcular_entropia_dado()
print(f"La entropía es: {entropia_dado:.2f} bits")