from collections import Counter
import string
import sys


def analizar_frecuencias(texto):
    """Analiza y muestra las frecuencias de cada letra en el texto"""
    texto = texto.upper()
    letras = [c for c in texto if c in string.ascii_uppercase]
    total_letras = len(letras)
    contador = Counter(letras)

    print("FRECUENCIAS DE LETRAS EN EL TEXTO CIFRADO:")
    print("-" * 45)
    for letra, count in contador.most_common():
        porcentaje = (count / total_letras) * 100
        print(f"{letra}: {count:3d} ocurrencias ({porcentaje:5.2f}%)")

    return contador


def sustituir_letras_seguro(texto, mapeo):
    caracteres = list(texto)
    mapeo_temporal = {orig: f"_{i}_" for i, (orig, nueva) in enumerate(mapeo.items())}

    for i in range(len(caracteres)):
        if caracteres[i].upper() in mapeo_temporal:
            if caracteres[i].isupper():
                caracteres[i] = mapeo_temporal[caracteres[i].upper()]
            else:
                caracteres[i] = mapeo_temporal[caracteres[i].upper()].lower()

    texto_temporal = ''.join(caracteres)

    for orig, nueva in mapeo.items():
        temp = mapeo_temporal[orig]
        texto_temporal = texto_temporal.replace(temp, nueva)
        texto_temporal = texto_temporal.replace(temp.lower(), nueva.lower())

    return texto_temporal


# -------------------------------
# LEER TEXTO CIFRADO DESDE UN ARCHIVO
# -------------------------------
if len(sys.argv) < 2:
    print("Uso: python3 desencriptar.py archivo.txt")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    texto_cifrado = f.read()

# 1. ANALIZAR FRECUENCIAS
frecuencias = analizar_frecuencias(texto_cifrado)

print("\n" + "=" * 60)

# 2. MAPEO MANUAL - AJUSTA A TU GUSTO
mapeo_manual = {
    'R': 'C',
    'I': 'O',
    'J': 'N',
    'A': 'D',
    'Z': 'U',
    'K': 'R',
    'H': 'T',
    'C': 'I',
    'P': 'M',
    'X': 'E',
    'T': 'L',
    'S': 'Q',
    'E': 'A',
    'N': 'S',
    'G': 'J',
    'F': 'X',
    'D': 'P',
    'Q': 'B',
    'O': 'F',
    'V': 'Y',
    'U': 'V',
    'M': 'H'
}

print("\nSUSTITUCIONES APLICADAS:")
print("-" * 25)
for cif, plana in mapeo_manual.items():
    print(f"  {cif} -> {plana}")

print("\n" + "=" * 60)

# 3. APLICAR SUSTITUCIONES
texto_descifrado = sustituir_letras_seguro(texto_cifrado, mapeo_manual)

print("\nTEXTO DESCIFRADO:")
print("-" * 40)
print(texto_descifrado)
print("-" * 40)

# Mostrar letras sin sustituir
letras_sin_mapear = [letra for letra in string.ascii_uppercase
                     if letra in texto_cifrado.upper() and letra not in mapeo_manual]
print(f"\nLetras sin sustituir: {', '.join(letras_sin_mapear)}")

