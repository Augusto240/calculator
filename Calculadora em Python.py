# Calculadora simples em Python!

# Adição
def add(x, y):
   return x + y

# Subtração
def subtract(x, y):
   return x - y

# Multiplicação
def multiply(x, y):
   return x * y

# Divisão
def divide(x, y):
   return x / y

# Main program
print("BEM-VINDO A CALCULADORA DO AUGUSTO!")

while True:
    # input
    print("ESCOLHA UMA OPERAÇÃO xD:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    choice = input("Escolha (1/2/3/4/5): ")

    # se o usuário quiser sair
    if choice == '5':
        print("OBRIGADO POR UTILIZAR A CALCULADORA DO AUGUSTO!")
        break


    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == '4':
        if num2 == 0:
            print("Error: divisão por zero:( ")
        else:
            print(num1, "/", num2, "=", divide(num1,num2))

    else:
        print("Invalid input. Please try again.")
