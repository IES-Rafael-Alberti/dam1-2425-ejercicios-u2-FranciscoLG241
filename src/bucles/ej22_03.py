def pedir_numero_positivo() -> int:
    numero = (input("Introduce un número entero positivo: "))
    if numero.isdigit():
        numero = int(numero)
        for i in range(1, numero + 1, 2):
            if i < numero - 1:
                print(i, end=", ")
            else:
                print(i)
        
        
    else:
        print("**ERROR**, debe de ser un número entero positivo")
        pedir_numero_positivo()
        
    
def main():
    pedir_numero_positivo()
    
    
if __name__ == "__main__":
    main()
    