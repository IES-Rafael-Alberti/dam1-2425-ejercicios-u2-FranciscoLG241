



def mostrar_inicio():
    print("\n Menu")
    print("1.- Comenzar programa")
    print("2.- Imprimir listado")
    print("3.- Finalizar programa")
    
    
    
def main():
    while True:
        mostrar_inicio()
    
        seleccion = input("Seleccione una de las opciones (1, 2 ,3): ")
    
        
        if seleccion == "1":
            print("Has comenzado el programa.")
            

        elif seleccion == "2":
            print("Imprimiendo listado...")
            

        elif seleccion == "3":
            print("Finalizando el programa. ¡Adiós!")
            break  

        else:
            print("Opción incorrecta. Por favor, elige 1, 2 o 3.")



if __name__ == "__main__":
    main()
        
        
    
    
    
    
    
    