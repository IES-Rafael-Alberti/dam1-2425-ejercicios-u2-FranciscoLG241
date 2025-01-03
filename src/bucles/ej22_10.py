
def comprobar_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    numero = int(input("Introduce un número entero: "))

    if comprobar_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
        
        
if __name__ == "__main__":
    main()

    
    