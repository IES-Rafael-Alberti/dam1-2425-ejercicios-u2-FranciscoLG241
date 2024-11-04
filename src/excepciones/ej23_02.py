


def main():
    while True:
        
        try:
            numero = int(input("Ingrese un número entero positivo: ")) 
            
            
            if numero <= 0:
                print("Por favor, ingrese un número entero positivo.")
                continue
            
            
            resultado = ""
            
            
            for i in range(1, numero + 1):
                if i % 2 != 0:  
                    resultado += str(i) + ", "  
            
            
            if resultado:  
                resultado = resultado.rstrip(", ")
            
            
            print("Números impares desde 1 hasta", numero, ":", resultado)
            break  
        
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")



if __name__ == "__main__":
    main()


