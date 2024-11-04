def pedir_puntuacion() -> float:
    puntuacion = float(input("Introduzca su puntuación: ").strip())
    
    if puntuacion == 0.0:
        print(f"Si tu puntuacion es de {puntuacion}, has tenido un nivel inaceptable")
        puntuacion2 = 2400 * puntuacion
        print(f"Por lo tanto, la cantidad de dinero que ganarás es de {puntuacion2}")
        return puntuacion2
        
    elif puntuacion == 0.4:
        print(f"Si tu puntuacion es de {puntuacion}, has tenido un nivel aceptable")
        puntuacion2 = 2400 * puntuacion
        print(f"Por lo tanto, la cantidad de dinero que ganarás es de {puntuacion2}")
        return puntuacion2
        
    elif puntuacion >= 0.6:
        print(f"Si tu puntuacion es de {puntuacion}, has tenido un nivel meritorio")
        puntuacion2 = 2400 * puntuacion
        print(f"Por lo tanto, la cantidad de dinero que ganarás es de {puntuacion2}")
        return puntuacion2
        
    else:
        print("**ERROR**, has introducido una puntuación indebida")
        return pedir_puntuacion()
        

def main():
    pedir_puntuacion()
    
if __name__ == "__main__":
    main()
    
    
   
     
        