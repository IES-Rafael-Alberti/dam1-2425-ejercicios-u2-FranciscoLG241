



def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    
    if len(letra) != 1:
        print("Por favor, ingresa solo una letra.")
        return

    
    posicion = 0

    
    for caracter in frase:
        if caracter == letra:
            print(f"Coincidencia encontrada en la posición {posicion + 1}.")
            break  
        else:
            print(f"No hay coincidencia en la posición {posicion + 1}.")
        
        posicion += 1
        
    else:
        print("No se encontró ninguna coincidencia en la frase.")


if __name__ == "__main__":
    main()

