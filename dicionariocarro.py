carros = [{"modelo": "chevrolet", "marca": "palio", "cor": "verde", "ano": 1998},
              {"modelo": "fiat", "marca": "siena", "cor": "preto", "ano": 2000},
              {"modelo": "wolks", "marca": "fusca", "cor": "azul", "ano": 2002}]

print("Iterando sobre os carros e acessando os valores:")
for carro in carros:
    print(f"Modelo: {carro['modelo']}, Marca: {carro['marca']}, Cor: {carro['cor']}, Ano: {carro['ano']}")


