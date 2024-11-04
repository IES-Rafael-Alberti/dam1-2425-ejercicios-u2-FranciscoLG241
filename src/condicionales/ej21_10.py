def comprobar_pizza() ->str:
    pedir = input("Elige que pizza te gustaría pedir (vegetariana o no vegetariana): ").strip().lower()
    
    
    if pedir == "vegetariana":
        print("Solo puedes elegir un ingrediente aparte de la mozzarella y el tomate")
        ingrediente = input("Ingredientes vegetarianos: pimiento y tofu, elija el que usted prefiera: ").strip().lower()
        
        
        if ingrediente == "pimiento" or "tofu":
            return print(f"Usted ha pedido una pizza vegetariana con los ingredientes: tomate, mozzarella y {ingrediente}")
            
            
        else:
            print("Solo puede elegir uno de los ingredientes proporcionados")
            ingrediente = input("Ingredientes vegetarianos: pimiento y tofu, elija el que usted prefiera: ").strip().lower()
            return print(f"Usted ha pedido una pizza vegetariana con los ingredientes: tomate, mozzarella y {ingrediente}")
            
            
            
    elif pedir == "no vegetariana":
        print("Solo puedes elegir un ingrediente aparte de la mozzarella y el tomate")
        ingrediente = input("Ingredientes no vegetarianos: peperoni, jamón y salmón, elija el que usted prefiera: ").strip().lower()
        
        
        if ingrediente == "peperoni" or "jamón" or "salmón":
            return print(f"Usted ha pedido una pizza no vegetariana con los siguientes ingredienets: tomate, mozzarella y {ingrediente}")
            
            
        else:
            print("Solo puede elegir uno de los ingredientes proporcionados")
            ingrediente = input("Ingredientes no vegetarianos: peperoni, jamón y salmón, elija el que usted prefiera: ").strip().lower()
            return print(f"Usted ha pedido una pizza no vegetariana con los siguientes ingredienets: tomate, mozzarella y {ingrediente}")
            
            

    else:
        print("Debe elegir entre una de los dos tipos de pizza")
        comprobar_pizza()
        
            


def main():
    comprobar_pizza()
    
    
if __name__ == "__main__":
    main()
             
        
            
            
        