"""
Math module for basic arithmetic operations.
"""

# Importamos las funciones para exponerlas al nivel del paquete
from .addition import add_numbers
from .subtraction import subtract_numbers

# Definimos qué funciones son accesibles al usar "from Math import *"
__all__ = ['add_numbers', 'subtract_numbers']