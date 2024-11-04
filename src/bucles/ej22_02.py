def introducir_edad():
    edad = int(input("Introduce tu edad: "))
    for i in range(1, edad + 1, 1):
        print(i, end=" ")
        
        
def main():
    introducir_edad()
    
    
if __name__ == "__main__":
    main()
    