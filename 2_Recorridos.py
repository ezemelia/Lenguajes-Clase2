# 5. Pedir una palabra y contar cuántas vocales tiene.
palabra = input("Ingrese una palabra: ")
vocales = "aeiou"
con_tilde = "áéíóú"
palabra_sin_mayusculas = palabra.lower()
cantidad_vocales = 0
for indice, vocal in enumerate(vocales):
    palabra = palabra_sin_mayusculas.replace(con_tilde[indice], vocal)
    cantidad_vocales += palabra.count(vocal)
print("'" + palabra + "' tiene " + str(cantidad_vocales) + " vocales.")

# 6. Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'.
for i in range(4):
    palabra = input("Ingrese una palabra: ")
    if "r" in palabra:
        print("Ingresaste " + palabra)

# 7. Ingresar palabras hasta escribir FIN; imprimir las que empiecen y terminen con la misma letra.
palabra = input("Ingrese una palabra: ")
primera_letra = 0
ultima_letra = len(palabra) - 1
while palabra != "FIN":
    if palabra[primera_letra] == palabra[ultima_letra]:
        print("Ingresaste " + palabra)
    palabra = input("Ingrese una palabra: ")
    ultima_letra = len(palabra) - 1