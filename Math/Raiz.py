 def raiz_cuadrada(self, x: float) -> float:
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo en ℝ.")
        return math.sqrt(x)

    def raiz_enesima(self, x: float, n: float) -> float:
        """
        Calcula la raíz enésima: x^(1/n)
        """
        if n == 0:
            raise ValueError("El índice n no puede ser 0.")

        if x < 0 and n % 2 == 0:
            raise ValueError("No se puede calcular raíz par de un número negativo en ℝ.")

        return x ** (1 / n)