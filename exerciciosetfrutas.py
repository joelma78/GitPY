frutas = {"maçã", "banana", "laranja", "kiwi", "uva"}
frutas_comprar = {"melao", "jaca"}

print("Frutas disponíveis:", frutas)
fruta = input("Procure uma fruta: ")

if fruta in frutas:
    print("Fruta disponível.")
else:
    print("Fruta indisponível.")
    print("Escolha uma dessas para encomendar:")

    # Mostra as frutas sugeridas para compra
    for fruta_sugerida in frutas_comprar:
        print(fruta_sugerida)

    # Usuário escolhe uma fruta para encomendar
    frutacomprar = input("Que fruta você quer encomendar: ")
    frutas_comprar.add(frutacomprar)
    print("Lista de frutas para comprar atualizada:", frutas_comprar)
