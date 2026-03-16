# Función que determina si un número es par o impar
def verificar_par(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

# Pedir número al usuario
num = int(input("Ingrese un número: "))

# Llamar a la función
resultado = verificar_par(num)

# Mostrar resultado
print(resultado)

1