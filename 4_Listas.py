# 11. Ingresar notas hasta -1, calcular el promedio y cuántos están por debajo.

total = 0
cantidad_notas = 0
cantidad_debajo = 0
notas = []

nota = int(input("Ingrese una nota: "))

while nota != -1:
    cantidad_notas += 1
    total += nota
    notas.append(nota)
    nota = int(input("Ingrese una nota: "))

promedio = total / cantidad_notas
for nota in notas:
    if nota < promedio:
        cantidad_debajo += 1

print(f"Cantidad debajo del promedio {promedio}: {cantidad_debajo}")

# 12. Dada una lista de palabras, construir otra con las que tengan más de 5 letras.

