# Calculadora Simples em Python

# Função para somar dois números
def somar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Exibir o menu de opções
def mostrar_menu():
    print("\nCalculadora Simples")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

# Programa principal
while True:
    mostrar_menu()
    
    # Obter a escolha do usuário
    opcao = input("Digite sua opção (1/2/3/4/5): ")
    
    # Verificar se o usuário quer sair
    if opcao == '5':
        print("Saindo da calculadora...")
        break  # Este break está DENTRO do while, então não causa erro
    
    # Verificar se a opção é válida
    if opcao not in ('1', '2', '3', '4'):
        print("Opção inválida! Tente novamente.")
        continue
    
    # Obter os números do usuário
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue
    
    # Realizar a operação selecionada
    resultado = None
    if opcao == '1':
        resultado = somar(num1, num2)
        operacao = "+"
    elif opcao == '2':
        resultado = subtrair(num1, num2)
        operacao = "-"
    elif opcao == '3':
        resultado = multiplicar(num1, num2)
        operacao = "*"
    elif opcao == '4':
        resultado = dividir(num1, num2)
        operacao = "/"
    
    # Exibir o resultado
    if isinstance(resultado, str):
        print(resultado)  # Exibe mensagem de erro
    else:
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")