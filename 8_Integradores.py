# 19. Escribir frecuencias_letras(frase) que devuelva un diccionario con la cantidad de apariciones de cada letra (ignorar espacios y may/min).

def frecuencias_letras(frase: str) -> dict:
    letras = "abcdefghijklmnñopqrstuvwxyz"

    tildes = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }

    apariciones = {}

    frase_sin_mayusculas = frase.lower()

    frase_sin_espacios = frase_sin_mayusculas.replace(" ", "")


    caracteres_de_frase = set(frase_sin_espacios)

    for caracter in caracteres_de_frase:

        if caracter in letras or caracter in tildes:
            letra = caracter

            if letra in tildes:
                letra = tildes[caracter]
                frase_sin_espacios = frase_sin_espacios.replace(caracter, letra)

            apariciones[letra] = frase_sin_espacios.count(letra)

    return apariciones

print(frecuencias_letras(input("Ingrese frase: ")))