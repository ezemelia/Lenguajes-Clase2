# 15. Leer nombres y notas hasta FIN y guardar en un diccionario. Luego mostrar:
# Promedio general, mejor estudiante, y los/as que están por debajo del promedio.

def mejor_estudiante(mejor_actual, nuevo, personas) -> str:
    mejor = mejor_actual
    if mejor_actual is None or personas[nuevo] > personas[mejor_actual]:
        mejor = nuevo
    return mejor

personas = {}
totalNotas = 0
cantidadAlumnos = 0
mejor = None

nombre = input("Ingrese un nombre completo: ")

while (nombre.upper() != "FIN"):
    personas[nombre] = int(input("Ingrese su nota: "))
    totalNotas += personas[nombre]
    cantidadAlumnos += 1
    mejor = mejor_estudiante(mejor, nombre, personas)
    nombre = input("Ingrese un nombre completo: ")

if cantidadAlumnos > 0:
    promedio_general = totalNotas / cantidadAlumnos

    for persona in personas:
        if personas[persona] < promedio_general:
            print(f"{persona} está debajo del promedio {promedio_general}")

    print(f"Mejor: {mejor}")

# 16. Construir un diccionario {palabra: longitud} a partir de una frase.

longitudes = {}

frase = input("Ingrese una frase: ")
frase = frase.replace(".", "")
frase = frase.replace(",", "")

palabras = frase.split()

for palabra in palabras:
    longitudes[palabra] = len(palabra)

print(longitudes)



