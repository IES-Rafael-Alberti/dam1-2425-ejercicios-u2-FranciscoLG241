def obtener_palabra():
    while True:
        palabra = input("Introduce una palabra: ").strip().lower()
        
        if palabra.isalpha():
            return palabra
        else:
            print("**ERROR**, la palabra introducida debe ser solo letras.")


def main():
    while True:
        palabra = obtener_palabra()
        
        if palabra == "salir":
            print("Bye, bye...")
            break
        
        print(f"ECO: {palabra}")


if __name__ == "__main__":
    main()

    