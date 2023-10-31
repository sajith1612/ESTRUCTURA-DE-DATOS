def invertir_palabras(frase):
    palabras = frase.split()
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    return " ".join(palabras_invertidas)

def main():
    frase = input("Ingrese una frase: ")
    frase_invertida = invertir_palabras(frase)
    print("Frase con palabras invertidas:")
    print(frase_invertida)

if __name__ == "__main__":
    main()
