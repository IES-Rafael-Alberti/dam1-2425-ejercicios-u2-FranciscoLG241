def obtener_numero() -> int:
    while True:
        try:
            numero = int(input("Introduce un número (0 para terminar): ").strip())
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
        
        if numero > 0:
            sumatorio += numero
            
    print(f"La sumatoria de los números positivos es: {sumatorio}")


if __name__ == "__main__":
    main()
