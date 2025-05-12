import math

def menu():
    print("\nCalculadora Científica Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("0. Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Encerrando...")
            break

        if escolha in ["1", "2", "3", "4", "5"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if escolha == "1":
                print(f"Resultado: {a + b}")
            elif escolha == "2":
                print(f"Resultado: {a - b}")
            elif escolha == "3":
                print(f"Resultado: {a * b}")
            elif escolha == "4":
                if b != 0:
                    print(f"Resultado: {a / b}")
                else:
                    print("Erro: divisão por zero.")
            elif escolha == "5":
                print(f"Resultado: {math.pow(a, b)}")

        elif escolha in ["6", "7", "8", "9"]:
            x = float(input("Digite o número: "))

            if escolha == "6":
                if x >= 0:
                    print(f"Resultado: {math.sqrt(x)}")
                else:
                    print("Erro: raiz de número negativo.")
            elif escolha == "7":
                print(f"Resultado: {math.sin(math.radians(x))}")
            elif escolha == "8":
                print(f"Resultado: {math.cos(math.radians(x))}")
            elif escolha == "9":
                print(f"Resultado: {math.tan(math.radians(x))}")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()