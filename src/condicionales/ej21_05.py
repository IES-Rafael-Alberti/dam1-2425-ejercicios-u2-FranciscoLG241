def comprobar_edad() -> int:
    edad = int(input("Introduce tu edad: "))
    
    while edad < 16:
        print("**ERROR**, tu edad debe de ser mayor de 16")
        edad = int(input("Introduce tu edad: "))
        
    return edad

def comprobar_ingresos() -> float:
    ingresos = float(input("Introduce tus ingresos: "))
    
    while ingresos < 1000:
        print("**ERROR**, tus ingresos deben de ser mayores de 1000")
        ingresos = float(input("Introduce tus ingresos: "))
        
    return ingresos

def main():
    edad = comprobar_edad()
    print(f"¡Felicidades!, tienes {edad} suficiente para tributar")
    ingresos = comprobar_ingresos()
    print(f"¡Felicidades!, tienes {ingresos} suficiente para tributar")
    
    
if __name__ == "__main__":
    main()

    