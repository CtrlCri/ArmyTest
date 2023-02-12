## Sal de ahí chivita
Un joven estaba elaborando un generador automático de una versión ampliada y aleatoria de la canción para niños "Sal de ahí chivita". Te mostramos el pseudocódigo para que busques la siguiente respuesta:
Considerando que cada línea lleva 1 milisegundo en ejecutarse,
¿Cuál es el tiempo esperado de ejecución para N = 1, 10, 50 y 200? Tené en cuenta que los puntos son para indentación.

Pseudocódigo:
array animales = [“el lobo”, “el toro”, … ]; // 100 animales

map LlamarA = {}

print(“Sal de ahí chivita chivita, sal de ahí de ese lugar”)
actualmente = “la chiva”
Realizar N veces {
..prox = elemento_random(animales)
..LlamarA[actualmente] = prox
..print(“Hay que llamar a “ + prox + “ para que saque a “ + actualmente)
..actualmente = prox
..array remover = [ ]
..inspeccionar = “la chiva”
..repetir hasta que inspeccionar no esté en LlamarA {
....remover.insertar_primero(LlamarA[inspeccionar] + “ no quiere sacar a ” + inspeccionar)
....inspeccionar = LlamarA[inspeccionar]
..}
for i in remover {
....print(i)
..}
..print(“La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar”)
}


Ejemplo de output para N = 3

Sal de ahí chivita chivita, sal de ahí de ese lugar
Hay que llamar a el lobo para que saque a la chiva
el lobo no quiere sacar a la chiva
La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar
Hay que llamar a el perro para que saque a el lobo
el perro no quiere sacar a el lobo
el lobo no quiere sacar a la chiva
La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar
Hay que llamar a el leon para que saque a el perro
el leon no quiere sacar a el perro
el perro no quiere sacar a el lobo
el lobo no quiere sacar a la chiva
La chiva no quiere salir de ahí. Sal de ahí chivita chivita, sal de ahí de ese lugar