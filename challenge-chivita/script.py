import random

animales = ["el lobo", "el toro", "elefante", "león", "tigre", "jirafa", "mono", "ardilla", "conejo", "ratón", "hámster", "serpiente",
            "cocodrilo", "pingüino", "tortuga", "canguro", "koala", "hipopótamo", "rinoceronte", "camello", "cebra", "murciélago",
            "búho", "águila", "loro", "tucán", "pato", "cisne", "pollo", "gallo", "vaca", "caballo", "oveja", "cerdo", "conejo",
            "rana", "pulpo", "ballena", "delfín", "tiburón", "pez espada", "salmón", "tortuga marina", "caracol", "mariposa", "abeja",
            "mosca", "araña", "escorpión", "saltamontes", "hormiga", "araña", "ciervo", "oso", "zorro", "mapache", "castor", "morsa",
            "orca", "foca", "hipocampo", "medusa", "anguila", "caballito de mar", "pollo", "gallina", "cabrito", "gallina", "avestruz",
            "cocodrilo", "tortuga", "grillo", "lucio", "pavo", "ratón", "topo", "búho", "abeja", "chivito", "dromedario", "elefante",
            "flamenco", "gaviota", "hipopótamo", "iguana", "jaguar", "koala", "lagartija", "mono", "nutria", "oso", "puma", "quetzal",
            "ratón", "serpiente", "tigre", "uapití", "vaca", "yak", "zebra"]

print("Sal de ahí chivita chivita, sal de ahí de ese lugar")

actualmente = "la chiva"
llamar_a = {}

N = 20 #N = 1, 10, --> 50? y 200? Memoria insuficiente
contador = 4
for _ in range(N):
    prox = random.choice(animales)
    llamar_a[actualmente] = prox
    print("Hay que llamar a", prox, "para que saque a", actualmente)
    actualmente = prox

    remover = []
    inspeccionar = "la chiva"
    contador = contador + 9
    while inspeccionar in llamar_a:
        remover.append(f" {llamar_a[inspeccionar]} no quiere sacar a {inspeccionar}")
        inspeccionar = llamar_a[inspeccionar]
        contador = contador + 4
    for i in reversed(remover):
        print(i)
        contador = contador + 3
    print("La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar")

print(contador)
