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

# Resolución

El pseudocódigo proporcionado describe un generador automático de una versión ampliada y aleatoria de la canción para niños "Sal de ahí chivita". El generador selecciona aleatoriamente animales de una lista y los asigna a la chiva en cada iteración. El código también realiza un seguimiento de las llamadas realizadas para sacar a los animales anteriores y, al final de cada iteración, muestra los mensajes correspondientes.

El ejercicio pide calcular el tiempo esperado de ejecución para diferentes valores de N, que representan el número de iteraciones del bucle principal.

El tiempo esperado de ejecución se calcula sumando el tiempo de ejecución de cada línea del pseudocódigo multiplicado por el número de veces que se ejecuta esa línea.

Dado que se indica que cada línea lleva 1 milisegundo en ejecutarse, podemos calcular el tiempo esperado de ejecución para los valores de N solicitados:

Para N = 1:
Líneas 1-4: 4 * 1 ms = 4 ms
Línea 6: 1 * 1 ms = 1 ms
Líneas 7-9: 3 * 1 ms = 3 ms
Línea 10: 1 * 1 ms = 1 ms
Líneas 11-14: 4 * 1 ms = 4 ms
Línea 15: 1 * 1 ms = 1 ms
Tiempo esperado de ejecución total: 4 ms + 1 ms + 3 ms + 1 ms + 4 ms + 1 ms = 14 ms

Para N = 10:
Líneas 1-4: 4 * 1 ms = 4 ms
Línea 6: 1 * 1 ms = 1 ms
Líneas 7-9: 3 * 10 ms = 30 ms (se ejecutan N veces)
Línea 10: 1 * 1 ms = 1 ms
Líneas 11-14: 4 * 10 ms = 40 ms (se ejecutan N veces)
Línea 15: 1 * 1 ms = 1 ms
Tiempo esperado de ejecución total: 4 ms + 1 ms + 30 ms + 1 ms + 40 ms + 1 ms = 77 ms

Para N = 50:
Líneas 1-4: 4 * 1 ms = 4 ms
Línea 6: 1 * 1 ms = 1 ms
Líneas 7-9: 3 * 50 ms = 150 ms (se ejecutan N veces)
Línea 10: 1 * 1 ms = 1 ms
Líneas 11-14: 4 * 50 ms = 200 ms (se ejecutan N veces)
Línea 15: 1 * 1 ms = 1 ms
Tiempo esperado de ejecución total: 4 ms + 1 ms + 150 ms + 1 ms + 200 ms + 1 ms = 357 ms

Para N = 200:
Líneas 1-4: 4 * 1 ms = 4 ms
Línea 6: 1 * 1 ms = 1 ms
Líneas 7-9: 3 * 200 ms = 600 ms (se ejecutan N veces)
Línea 10: 1 * 1 ms = 1 ms
Líneas 11-14: 4 * 200 ms = 800 ms (se ejecutan N veces)
Línea 15: 1 * 1 ms = 1 ms
Tiempo esperado de ejecución total: 4 ms + 1 ms + 600 ms + 1 ms + 800 ms + 1 ms = 1407 ms

Por lo tanto, el tiempo esperado de ejecución para N = 1 es de 14 ms, para N = 10 es de 77 ms, para N = 50 es de 357 ms y para N = 200 es de 1407 ms. Estos cálculos asumen que cada línea del pseudocódigo lleva exactamente 1 milisegundo en ejecutarse.