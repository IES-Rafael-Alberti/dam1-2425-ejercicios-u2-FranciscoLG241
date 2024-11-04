


def es_primo(numero):
    if numero <= 1:
        return False
    
    if numero % 2 == 0:
        return True
    
    else:
        return False
    
    

def contar_primos():
    cantidad_primos = 0


    while True:
        try:
            numero = int(input("Ingrese un número mayor que 1 (0 para finalizar): "))
            
            if numero == 0:
                break
            
            if numero > 1:
                if es_primo(numero):
                    cantidad_primos += 1
                    
            else:
                print("Por favor, ingrese un número mayor que 1.")
                
                
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
            

    return cantidad_primos

def main():
    cantidad_primos = contar_primos()
    print(f"La cantidad de números primos ingresados es: {cantidad_primos}")





if __name__ == "__main__":
    main()
