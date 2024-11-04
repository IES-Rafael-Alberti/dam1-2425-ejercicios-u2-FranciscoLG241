


def main():
    contrasena_correcta = "Francisco"

    contrasena = input("Ingrese la contraseña: ")


    try:
        if contrasena == contrasena_correcta:  
            print("Contraseña correcta. Acceso concedido.")
            
        else:  
            raise NameError("Incorrect Password!!")  
        
    
    except NameError as e:
        print("Error:", e)  




if __name__ == "__main__":
    main()


