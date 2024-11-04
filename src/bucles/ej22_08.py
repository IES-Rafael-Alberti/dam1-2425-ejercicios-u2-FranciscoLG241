def introducir_altura():
    
    altura = int(input("Introduce la altura del triángulo rectángulo: "))


    for i in range(1, altura + 1):
        fila = ""  
        for j in range(i):
            fila += str(2 * (i - j) - 1) + " "  
        print(fila.strip())  

def main():
    introducir_altura()
    
    
if __name__ == "__main__":
    main()
    
    
