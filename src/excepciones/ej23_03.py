


def main():
    while True:
        
        try:
            numero = int(input("Ingrese un número entero positivo: "))  
            
            
            if numero <= 0:
                print("Por favor, ingrese un número entero positivo.")
                numero = int(input("Ingrese un número entero positivo: "))  
            
            
            cuenta_atras = ""
            
            
            for i in range(numero, -1, -1):  
                cuenta_atras += str(i) + ", "  
            
            
            cuenta_atras = cuenta_atras.rstrip(", ")
            
            
            print("Cuenta atrás desde", numero, "hasta 0:", cuenta_atras)
            break  
        
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")




if __name__ == "__main__":
    main()


