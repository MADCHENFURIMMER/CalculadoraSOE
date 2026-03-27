from Math import add_numbers, subtract_numbers
from Tarea.CalculadoraSOE.functions.menu import mostrar_menu
from Tarea.CalculadoraSOE.functions.saludo import pedir_nombre, saludar

def main():

    nombre = pedir_nombre()
    saludar(nombre)

    try:

        while True:
            mostrar_menu()

            opcion = input("Seleccione una opción: ")

            if opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print(f"Elegiste la opción {opcion}")

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