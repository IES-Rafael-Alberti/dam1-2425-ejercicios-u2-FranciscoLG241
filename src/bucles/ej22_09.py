

def main():
    contraseña = input("Introduce tu contraseña: ").strip()
    
    while contraseña != "contraseña":
        print("**ERROR**, la contraseña introducida es incorrecta")
        contraseña = input("Verifica tu contraseña: ")
        
    print("ACCESO PERMITIDO")
    

if __name__ == "__main__":
    main()
    
