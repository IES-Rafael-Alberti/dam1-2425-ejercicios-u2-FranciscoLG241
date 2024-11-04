



def suma_digitos(numero):
    suma = 0
    
    for digito in numero:
        suma += int(digito)  # Convertir el carácter a entero y sumar
        
    return suma

def main():
    numero = input("Introduce un número entero positivo: ")

    if numero.isdigit():
        resultado = suma_digitos(numero) 
        print("La suma de los dígitos es:", resultado)
        
    else:
        print("Por favor, introduce un número entero positivo válido.")


if __name__ == "__main__":
    main()
