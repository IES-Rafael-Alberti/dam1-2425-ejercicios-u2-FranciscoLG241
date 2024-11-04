def introducir_contraseña():
    return input("¿Cuál es tu contraseña?: ")

def main():
    contraseña = input("Introduce tu contraseña: ") 
    introducir_usuario = introducir_contraseña()  

    while contraseña.lower() != introducir_usuario.lower(): 
        print("La contraseña es incorrecta.")
        introducir_usuario = introducir_contraseña() 

    print("La contraseña es correcta.")  

if __name__ == "__main__":
    main()

