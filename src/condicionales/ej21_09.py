def comprobar_edad() ->int:
    edad = int(input("Introduzca su edad: ").strip())
    
    if  1 <= edad < 4:
        print(f"Al tener {edad} años, su entrada es gratis")
        
    elif 4 <= edad < 18:
        print(f"Al tener {edad} años, su entrada valdrá 5€")
        
    elif edad >= 18:
        print(f"Al tener {edad} años, su entrada valdrá 10€")
        
    else:
        print("**ERROR**, introduzca une edad válida")
        comprobar_edad()
        
    return edad
        
def main():
    comprobar_edad()
    
if __name__ == "__main__":
    main()
    