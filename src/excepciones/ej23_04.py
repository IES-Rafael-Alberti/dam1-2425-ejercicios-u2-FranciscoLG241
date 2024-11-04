


def main():
    try:
        numero = int(input("Ingrese un número entero: "))  
        print(f"Has ingresado el número: {numero}")
        
        
    except ValueError as e:
        print("La entrada no es correcta.")  
        raise e  



if __name__ == "__main__":
    main()

