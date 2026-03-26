from Math import add_numbers, subtract_numbers

def main():
    try:
        # Pedir los números al usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Ejecutar las funciones del módulo
        res_add = add_numbers(num1, num2)
        res_sub = subtract_numbers(num1, num2)

        # Mostrar resultados
        print(f"\nResultados:")
        print(f"Suma: {res_add}")
        print(f"Resta: {res_sub}")

    except ValueError:
        # Manejo de error si el usuario no ingresa un número
        print("Error: Por favor ingresa numeros válidos.")

if __name__ == "__main__":
    main()