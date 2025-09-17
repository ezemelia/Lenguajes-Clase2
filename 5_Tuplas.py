# 13. Guardar coordenadas (x, y) en una tupla e imprimir la distancia al origen.

punto = (
        int(input("Ingresá X: ")),
        int(input("Ingresá Y: "))
        )

distancia = ((punto[0]**2) + (punto[1]**2)) ** 0.5

print(distancia)

# 14. Dada una lista de tuplas (nombre, edad), imprimir solo los mayores de 18.

lista = [
        ("Eze", 27),
        ("Mati", 24),
        ("Santi", 21),
        ("Lucas", 16)
]

for persona in lista:
        if persona[1] > 18:
                print(persona[0])