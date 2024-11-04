def division_numeros(num1, num2):
    division = num1 /num2
    return division

def comprobar_cero(num2: float) -> bool:
    if num2 == 0:
        return False
    else:
        return True
 
def main():
    num1 = float(input("Introduce un primer número: "))
    num2 = float(input("Introduce un segundo número: "))
    
    while not comprobar_cero(num2):
        print("**ERROR**, el divisor no puede ser 0")
        num2 = float(input("Introduce un segundo número: "))
        
    print(division_numeros(num1, num2))
    
if __name__ == "__main__":
    main()
    