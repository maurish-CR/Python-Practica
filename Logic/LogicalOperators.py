#>,<,==,!=
print(4!=5)
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
if num1 < num2:
    print(f'{num1} es {num2 - num1} unidades menor que el numero {num2}')
elif num1 > num2:
    print(f'{num1} es {num1 - num2} unidades mayor que el numero {num2}')
elif num1 == num2:
    print(f'{num1} y {num2} son iguales')


a = [1,2,3]
b = a
print(a is b)