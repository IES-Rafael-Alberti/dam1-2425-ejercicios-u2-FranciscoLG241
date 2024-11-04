def pedir_altura():
    altura = int(input("Introduce la altura del triángulo rectángulo: "))

    for i in range(1, altura + 1):
        print('*' * i)
    
    
def main():
    pedir_altura()
    
if __name__ == "__main__":
    main()

    
    