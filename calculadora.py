# Funciones para realizar operaciones matemáticas

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    # Manejando el caso de división por cero
    if b == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return a / b

# Función principal para la calculadora

def main():
    while True:
        print("\nCalculadora básica")
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione la operación (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = suma(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif opcion == '2':
            resultado = resta(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif opcion == '4':
            resultado = division(num1, num2)
            print("El resultado de la división es:", resultado)
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
