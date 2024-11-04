def obtener_numero() -> int:
    while True:
        try:
            numero = int(input("Introduce un número (0 para terminar): ").strip())
            return numero
        
        except ValueError:
            print("**ERROR**, solo se pueden introducir números enteros.")
            
            
            

def main():
    mayor = None  

    while True:
        numero = obtener_numero()
        
        if numero == 0:
            
            if mayor is not None:
                print(f"El mayor número ingresado fue: {mayor}")
                
            else:             
                print("No se ingresaron números positivos.")
            print("Bye, bye...")
            break
        
        if numero > 0:
            
            if mayor is None or numero > mayor: 
                mayor = numero





if __name__ == "__main__":
    main()




