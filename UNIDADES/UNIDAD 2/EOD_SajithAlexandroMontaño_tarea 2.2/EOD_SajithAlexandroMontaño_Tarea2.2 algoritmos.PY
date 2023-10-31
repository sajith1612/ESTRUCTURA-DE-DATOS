from collections import deque

def main():
    numeros = set()
    cola = deque()
    pila = []

    while True:
        try:
            numero = int(input("Ingrese un número (o '0' para detenerse): "))
            if numero == 0:
                break
            if numero not in numeros:
                numeros.add(numero)
                cola.append(numero)
                pila.append(numero)
            else:
                print("Este número ya ha sido registrado. Ingrese otro número.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

    print("Números únicos ingresados en la cola:")
    while cola:
        print(cola.popleft())

    print("Números únicos ingresados en la pila:")
    while pila:
        print(pila.pop())

if __name__ == "__main":
    main()
