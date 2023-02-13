# Código en Python que implementa el generador automático de la canción "Sal de ahí chivita" y calcula el tiempo esperado de ejecución para diferentes valores de N:
import random

animales = ["el lobo", "el toro", ...]  # 100 animales
LlamarA = {}

def elemento_random(lista):
    return random.choice(lista)

def generador_cancion(N):
    print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
    actualmente = "la chiva"

    tiempo_ejecucion = 0  # Variable para almacenar el tiempo de ejecución total

    for _ in range(N):
        prox = elemento_random(animales)
        LlamarA[actualmente] = prox
        print("Hay que llamar a " + prox + " para que saque a " + actualmente)
        actualmente = prox
        remover = []
        inspeccionar = "la chiva"

        while inspeccionar not in LlamarA:
            remover.insert(0, LlamarA[inspeccionar] + " no quiere sacar a " + inspeccionar)
            inspeccionar = LlamarA[inspeccionar]

        for i in remover:
            print(i)

        print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar")

        # Actualizar el tiempo de ejecución total
        tiempo_ejecucion += 9 + len(remover) * 9

    return tiempo_ejecucion


if __name__ == '__main__':
    # Calcular el tiempo esperado de ejecución para diferentes valores de N
    N_valores = [1, 10, 50, 200]
    for N in N_valores:
        tiempo_esperado = generador_cancion(N)
        print(f"Tiempo esperado de ejecución para N={N}: {tiempo_esperado} ms")
