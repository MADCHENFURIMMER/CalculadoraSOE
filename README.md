# CalculadoraSOE 🧮

Una calculadora modular escrita en **Python** que destaca por su organización limpia, separando la interfaz de usuario de la lógica matemática mediante paquetes y módulos.

## 🚀 Características
El sistema está diseñado para ser escalable, dividiendo las responsabilidades en módulos específicos:

### 🔢 Módulo de Matemáticas (`Math/`)
Contiene la lógica de cálculo puro:
- **Aritmética Básica:** Suma (`addition.py`), Resta (`subtraction.py`) y División (`division.py`).
- **Cálculo Avanzado:** Potenciación (`Potencia.py`) y Radicación (`Raiz.py`).

### ⚙️ Módulo de Funciones (`functions/`)
Gestiona la interacción y el flujo con el usuario:
- **Navegación:** Menú interactivo para seleccionar operaciones (`menu.py`).
- **Experiencia:** Sistema de entrada de datos y saludos personalizados (`saludo.py`).

## 💻 Funcionamiento (main.py)
El programa principal sigue un flujo lógico:
1. **Identificación:** Solicita el nombre del usuario y le da la bienvenida.
2. **Interfaz:** Despliega un menú de opciones mediante un bucle `while`.
3. **Cálculo:** Solicita los operandos, valida que sean números reales y ejecuta la función matemática correspondiente.
4. **Seguridad:** Incluye un bloque `try-except` para evitar errores si el usuario ingresa datos no numéricos.

## 📂 Estructura del Proyecto
```text
CalculadoraSOE/
├── main.py                # Punto de entrada y gestión de errores
├── Math/                  # Lógica matemática (suma, resta, potencia, etc.)
│   ├── addition.py
│   ├── subtraction.py
│   ├── division.py
│   ├── Potencia.py
│   └── Raiz.py
└── functions/             # Interfaz de usuario (menú y saludos)
    ├── menu.py
    └── saludo.py
