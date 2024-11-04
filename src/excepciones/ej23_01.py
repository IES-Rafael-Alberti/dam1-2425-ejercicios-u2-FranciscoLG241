



def main():
    while True:
        
        try:
            edad = int(input("Ingrese su edad: ")) 
            
            
            if edad < 1:
                print("Por favor, ingrese una edad válida (mayor que 0).")
                edad = int(input("Ingrese su edad: ")) 
            
            
            print("Usted ha cumplido los siguientes años:")
            for año in range(1, edad + 1):
                print(año)
            break  
        
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")




if __name__ == "__main__":
    main()
