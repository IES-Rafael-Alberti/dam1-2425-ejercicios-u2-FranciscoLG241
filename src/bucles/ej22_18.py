




def suma_digitos(numero):
    suma = 0
    for digito in numero:
        suma += int(digito)  
    return suma


def main():
    cantidad_pares = 0  

    while True:
        numero = input("Introduce un número entero positivo (-1 para terminar): ")

        if numero == "-1":
            break

        if numero.isdigit():
            resultado = suma_digitos(numero)
            print("La suma de los dígitos es:", resultado)

            if int(numero) % 2 == 0:
                cantidad_pares += 1
                
        else:
            print("Por favor, introduce un número entero positivo válido.")

    
    print("Se ingresaron", cantidad_pares, "números pares.")


if __name__ == "__main__":
    main()
