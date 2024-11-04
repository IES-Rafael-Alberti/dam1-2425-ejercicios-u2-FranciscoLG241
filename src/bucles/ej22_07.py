def tablas_multiplicar():
    for i in range(1, 11):  
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):  
            print(f"{i} x {j} = {i * j}")
        print() 

def main():
    print(tablas_multiplicar())
    
if __name__ == "__main__":
    main()
    
    