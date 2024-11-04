def introducir_edad():
    edad = input("Introduce tu edad: ")
    while edad.startswith("-") or not edad.isdigit():
        print("Ups!, tu edad no puede ser negativa o no válida")
        edad = input("Introduce tu edad: ")
    return int(edad)


def main():
    edad = introducir_edad()
    edad2 = 18 - edad
    if edad < 18:
        print(f"Eres menor de edad, te faltan {edad2} para ser mayor de edad")
    else:
        print("Eres mayor de edad")
        
if __name__ == "__main__":
    main()
    