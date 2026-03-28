class CalculadoraCientifica:
    
    def cuadrado(self, x: float) -> float:
        return x ** 2

    def potencia(self, x: float, n: float) -> float:
        """
        Calcula la potencia enésima: x^n
        Soporta exponentes reales y negativos.
        """
        # Caso especial: 0^0 indefinido
        if x == 0 and n == 0:
            raise ValueError("0^0 es una indeterminación.")

        # Caso: base negativa con exponente fraccionario → complejo
        if x < 0 and not n.is_integer():
            raise ValueError("Resultado sería complejo. Usa cmath si deseas soportarlo.")

        return x ** n
