



def main():
    total_compras = 0.0  

    while True:
        try:
            monto = float(input("Ingresa el monto de la compra (0 para terminar): "))


            if monto == 0:
                break

            
            if monto < 0:
                print("El monto no puede ser negativo. Por favor, ingresa un monto válido.")
                monto = float(input("Ingresa el monto de la compra (0 para terminar): "))  
                

            total_compras += monto

        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

    
    if total_compras > 1000:
        total_compras *= 0.9  

    
    print(f"El total a pagar es: {total_compras:.2f}$")


if __name__ == "__main__":
    main()
