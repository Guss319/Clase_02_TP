def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    return x / y


print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        break
    elif choice == '5':
        print("Salida")
        break
    else:
        print("Entrada invalida")
