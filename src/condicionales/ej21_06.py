def comprobar_genero():
    genero = input("Introduce tu genero (hombre o mujer): ").strip().lower()
    
    if genero not in ["hombre", "mujer"]:
        print("Género no reconocido. Por favor, introduce 'hombre' o 'mujer'.")
        return None

    nombre = input("Introduce tu nombre: ").strip()

    if genero == "mujer":
        if nombre[0].upper() < 'M':
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B")
    elif genero == "hombre":
        if nombre[0].upper() > 'N':
            print("Perteneces al grupo A")
        else:
            print("Perteneces al grupo B")
    
def main():
    comprobar_genero()
    
if __name__ == "__main__":
    main()
