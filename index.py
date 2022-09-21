num1 = int(input("introduce tu primer numero"))
num2 = int(input("introduce tu segundo numero"))
opcion= 0
while True:
    print("""opciones:
    1) Suma
    2) Resta
    3) Salir""")
    opcion=int(input("Ingresa la operacion a realizar"))
    if opcion == 1:
        print("la suma es: ", num1 + num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta=input()
        if rpta=="s":
            continue
        else:
            break

    elif opcion == 2:
        print("la resta es: ", num1 - num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta=input()