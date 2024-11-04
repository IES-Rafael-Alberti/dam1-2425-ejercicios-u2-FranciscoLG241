


def main():
    frase = input("Ingrese una frase: ")

    
    palabras = frase.split()  
    

    if not palabras:
        print("No se ingresaron palabras.")
        return

    
    palabra_mas_larga = ""
    
    
    
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    
    cantidad_palabras = len(palabras)

    
    print(f"La cantidad de palabras en la frase es: {cantidad_palabras}")
    print(f"La palabra más larga es: '{palabra_mas_larga}'")





if __name__ == "__main__":
    main()

