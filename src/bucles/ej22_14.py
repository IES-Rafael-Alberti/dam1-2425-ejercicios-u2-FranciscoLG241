def obtener_numero() -> int:
    while True:
        try:
            numero = int(input("Introduce un número: ").strip())
            return numero
        
        except ValueError:
            print("**ERROR**, solo se pueden introducir números enteros.")


def main():
    sumatorio = 0
    
    while True:
        numero = obtener_numero()
        
        if numero == 0:
            print("Bye, bye...")
            break
        
        sumatorio += numero
        print(f"El sumatorio hasta ahora es: {sumatorio}")
        
    print(f"La sumatoria total es: {sumatorio}")


if __name__ == "__main__":
    main()

    