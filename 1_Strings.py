# 1. Pedir una palabra y mostrarla en mayúsculas, minúsculas y title case.

palabra = input("Ingrese una palabra: ")
print(palabra.upper())
print(palabra.lower())
print(palabra.title())

# 2. Pedir una frase y contar cuántas veces aparece cada vocal.
frase = input("Ingrese una frase: ")
vocales = "aeiou"
con_tilde = "áéíóú"
frase_sin_mayusculas = frase.lower()

for indice, vocal in enumerate(vocales):
    frase = frase_sin_mayusculas.replace(con_tilde[indice], vocal)
    print("Apariciones de '" + vocal + "' = " + str(frase.count(vocal)))

# 3. Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando slicing.
print("Primeras 3 letras: " + frase[:4] + " | Últimas 3 letras: " + frase[-3:])

# 4. Verificar si una palabra contiene la letra 'r'. (Tip: in)
if "r" in palabra:
    print(palabra + " contiene 'r'.")
else:
    print(palabra + " NO contiene 'r'.")