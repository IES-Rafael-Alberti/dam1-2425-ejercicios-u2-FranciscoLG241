def comprobar_par():
        return print("El número es par")
    
def comprobar_impar():   
        return print("El número es impar")
    
def main():
    num = int(input("Introduce un número para saber si es par o impar: "))
    if num % 2 == 0:
        comprobar_par()
    else:
        comprobar_impar()
        
if __name__ == "__main__":
    main()
    