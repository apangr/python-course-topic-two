# Declaración de enteros
edad = 25
temperatura_bajo_cero = -10
población_mundial = 8_000_000_000  # Los guiones bajos mejoran la legibilidad


# Diferentes bases numéricas
decimal = 42  # Base 10 (por defecto)
binario = 0b101010  # Base 2 (binario)
octal = 0o52  # Base 8 (octal)
hexadecimal = 0x2A  # Base 16 (hexadecimal)

print(decimal)  # Salida: 42
print(binario)  # Salida: 42
print(octal)  # Salida: 42
print(hexadecimal)  # Salida: 42


# Declaración de flotantes
altura = 1.75
pi = 3.14159
pequeño = 1.7e-5  # Notación científica: 1.7 × 10^-5 = 0.000017
grande = 6.022e23  # Notación científica: 6.022 × 10^23

# Declaración de flotantes
altura = 1.75
pi = 3.14159
pequeño = 1.7e-5  # Notación científica: 1.7 × 10^-5 = 0.000017
grande = 6.022e23  # Notación científica: 6.022 × 10^23

resultado = 0.1 + 0.2
print(resultado)  # Salida: 0.30000000000000004
print(round(resultado, 1))  # Salida: 0.3

# Comparación de flotantes
a = 0.1 + 0.2
b = 0.3

# Evitar esto:
print(a == b)  # Salida: False

# Preferir esto:
print(abs(a - b) < 1e-10)  # Salida: True
# O usar el módulo math para comparaciones más robustas
import math

print(math.isclose(a, b))  # Salida: True
