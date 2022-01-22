def esBinario(strbinario):
    numero_decimal = 0

    for posicion, digito_string in enumerate(strbinario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion

    return numero_decimal


strbinario = str(input("Introduce un número binario: "))

print(esBinario(strbinario))
