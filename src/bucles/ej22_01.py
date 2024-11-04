def introducir_palabra() ->str:
    palabra = input("Introduce la primera palabra que se te venga a la cabeza: ")
    for i in range (10):
        print(palabra)
        
        
def main():
    introducir_palabra()
    

if __name__ == "__main__":
    main()
    