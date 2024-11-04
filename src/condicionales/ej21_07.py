def comprobar_renta() -> float:
    renta = float(input("Introduce tu renta: ").strip())
    
    if renta < 10000:
        print(f"Según tu renta de {renta}, te corresponde un impositivo del 5%")
    
    elif 10000 <= renta < 20000:
        print(f"Según tu renta de {renta}, te corresponde un impositivo del 15%")
        
    elif 20000 <= renta < 35000:
        print(f"Según tu renta de {renta}, te corresponde un impositivo del 20%")
        
    elif 35000 <= renta < 60000:
        print(f"Según tu renta de {renta}, te corresponde un impositivo del 30%")
        
    else:
        print(f"Según tu renta de {renta}, te corresponde un impositivo del 45%")
        
    return renta

def main():
    comprobar_renta()
    
if __name__ == "__main__":
    main()


