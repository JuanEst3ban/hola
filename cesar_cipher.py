
def main():
    texto = input("Escribe el texto a encodear: ")
    llave = input("Escribe la llave: ")
    texto_cifrado =obtener_cifrado(llave,texto)
    print(texto_cifrado)
    documento = open("cifrado.txt", "w")
    documento.write(texto_cifrado)


def obtener_cifrado(llave, texto_plano):
    cif = ""
    for index, val in enumerate(texto_plano):
        c = ord(val) ^ ord(llave[0])
        cif += str(chr(c))
    return cif

main()