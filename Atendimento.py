filatend = []

while True:
    entrada=input("Digite 'sim' para um novo cliente ou 'fim' para encerrar: ")
    if entrada == 'sim' :
        nomecliente = input("Digite o nome do cliente:  ")
        filatend.append(nomecliente)
        print("Fila atual:",filatend)
        
    elif entrada=='fim':
        break

    else:
        print("entrada inválida. Por favor, digite 'sim' ou 'fim'.  ")
        
    while filatend:
        entrada = input("Digite 'atender' para chamar o próximo cliente ou 'Fim' para encerrar o atendimento: " )
        if entrada== "atender":
            nomecliente = filatend.pop(0)

