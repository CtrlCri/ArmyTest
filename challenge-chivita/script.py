# Código en Python que implementa el generador automático de la canción "Sal de ahí chivita" y calcula el tiempo esperado de ejecución para diferentes valores de N:
import random

ANIMALES = ["perro", "gato", "elefante", "león", "tigre", "jirafa",
    "mono", "ardilla", "conejo", "ratón", "hámster", "serpiente",
    "cocodrilo", "pingüino", "tortuga", "canguro", "koala", "hipopótamo",
    "rinoceronte", "camello", "cebra", "murciélago", "búho", "águila",
    "loro", "tucán", "pato", "cisne", "pollo", "gallo", "vaca", "caballo",
    "oveja", "cerdo", "conejo", "rana", "pulpo", "ballena", "delfín",
    "tiburón", "pez espada", "salmón", "tortuga marina", "caracol",
    "mariposa", "abeja", "mosca", "araña", "escorpión", "saltamontes",
    "hormiga", "araña", "ciervo", "oso", "zorro", "mapache", "castor",
    "morsa", "orca", "foca", "hipocampo", "medusa", "anguila", "caballito de mar",
    "pollo", "gallina", "cabrito", "gallina", "avestruz", "cocodrilo",
    "tortuga", "grillo", "lucio", "pavo", "ratón", "topo", "búho", "abeja",
    "chivita", "dromedario", "elefante", "flamenco", "gaviota", "hipopótamo",
    "iguana", "jaguar", "koala", "lagartija", "mono", "nutria", "oso",
    "puma", "quetzal", "ratón", "serpiente", "tigre", "uapití", "vaca",
    "yak", "zebra"]  # 100 animales
LLAMAR_A = {}

def obtener_elemento_aleatorio(lista):
    return random.choice(lista)

def generar_cancion(N):
    print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
    actualmente = "chivita"

    tiempo_ejecucion = 0  # Variable para almacenar el tiempo de ejecución total

    for _ in range(N):
        prox = obtener_elemento_aleatorio(ANIMALES)
        LLAMAR_A[actualmente] = prox
        print(f"Hay que llamar a {prox} para que saque a {actualmente}")
        actualmente = prox
        remover = []
        inspeccionar = "chivita"

        while inspeccionar not in LLAMAR_A:
            remover.insert(0, f"{LLAMAR_A[inspeccionar]} no quiere sacar a {inspeccionar}")
            inspeccionar = LLAMAR_A[inspeccionar]

        for i in remover:
            print(i)

        print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar")

        # Actualizar el tiempo de ejecución total
        tiempo_ejecucion += 9 + len(remover) * 9

    return tiempo_ejecucion

# Calcular el tiempo esperado de ejecución para diferentes valores de N
if __name__ == "__main__":
    N = 10 #, 10, 50, 200

    tiempo_esperado = generar_cancion(N)
    print(f"Tiempo esperado de ejecución para N={N}: {tiempo_esperado} ms")
