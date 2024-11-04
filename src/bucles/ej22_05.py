def introducir_cantidad():
    amount = float(input("Introduce la cantidad a invertir: "))
    interest = float(input("Introduce el interés anual: "))
    
    amount *= 1 + interest / 100
    
    años = int(input("Introduce durante cuantos años: "))
    capital = amount * años
    
    return print(f"Tu capital en {años} años, será de {capital}")



def main():
    introducir_cantidad()
    
    
    
    
if __name__ == "__main__":
    main()


    