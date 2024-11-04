


def main():
    lineas_completas = 0  
    

    while True:
        total_digitos = 0  
        libros_ingresados = 0  
        

        while libros_ingresados >= 0:
            libro = input("Libro: ")

            
            if libro == "*":
                
                if lineas_completas == 0:
                    print("Fin. No se leyeron líneas completas.")
                     
                else:
                    print(f"Fin. Se leyeron {lineas_completas} líneas completas.")
                return  

            
            if libro == "/":
                print(f"Línea completa. Aparecen {total_digitos} dígitos numéricos.")
                lineas_completas += 1  
                break  

            
            for caracter in libro:
                if caracter.isdigit():
                    total_digitos += 1  
            libros_ingresados += 1 




if __name__ == "__main__":
    main()

