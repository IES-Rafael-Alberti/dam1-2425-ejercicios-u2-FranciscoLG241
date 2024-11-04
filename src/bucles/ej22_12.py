def comprobar_letra(letra):
    return len(letra) == 1

def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    
    if not comprobar_letra(letra):
        print("Por favor, introduce solo una letra.")
        return

    
    cont = 0
    for letra_frase in frase:  
        if letra_frase.lower() == letra.lower():  
            cont += 1

    print(f"La letra '{letra}' aparece {cont} veces en la frase.")

if __name__ == "__main__":
    main()

    
    