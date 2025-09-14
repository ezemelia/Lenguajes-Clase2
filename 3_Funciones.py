# 8. Escribir es_palindromo(cadena) que devuelva True si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).

def es_palindromo(cadena: str) -> bool:
    cadena = cadena.replace(" ", "")
    cadena = cadena.lower()

    primera_letra = 0
    ultima_letra = len(cadena) - 1

    palindromo = True

    while palindromo and primera_letra < ultima_letra:
        palindromo = cadena[primera_letra] == cadena[ultima_letra]
        primera_letra += 1
        ultima_letra -= 1

    return palindromo


cadena = input("Ingrese una cadena de caracteres: ")

print(es_palindromo(cadena))

# 9. Escribir contar_vocales(cadena) que retorne un diccionario con la cuenta de cada vocal.

def contar_vocales(cadena: str) -> dict:
    vocales = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    con_tilde = "áéíóú"
    cadena_sin_mayusculas = cadena.lower()

    for indice, vocal in enumerate(vocales):
        cadena = cadena_sin_mayusculas.replace(con_tilde[indice], vocal)
        vocales[vocal] = cadena.count(vocal)

    return vocales

print(contar_vocales(cadena))

# 10. Escribir normalizar_palabras(frase) que retorne una lista de palabras sin signos de puntuación y en minúsculas.

def normalizar_palabras(frase: str) -> list:
    frase = frase.lower()
    frase_sin_comas = frase.replace(",", "")
    frase_sin_puntuacion = frase_sin_comas.replace(".", "")
    lista = frase_sin_puntuacion.split()

    return lista

print(normalizar_palabras(cadena))
