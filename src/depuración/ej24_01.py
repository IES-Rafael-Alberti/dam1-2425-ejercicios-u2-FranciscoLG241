
def burbuja(arr):
    n = len(arr)
    
    for i in range(n - 1):  
        intercambiado = False 
        
        for j in range(n - 1 - i):  
            
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        
        if not intercambiado:
            break
        
    return arr





def main():
    a = [8, 3, 1, 19, 14]
    sorted_a = burbuja(a)
    
    print(f"La lista ordenada es: {sorted_a}")
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
    




