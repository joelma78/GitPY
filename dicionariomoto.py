motos = [{"modelo": "harley", "marca": "patron", "cor": "prata", "ano": 1998},
              {"modelo": "honda", "marca": "CG", "cor": "preto", "ano": 2000},
              {"modelo": "suzuky", "marca": "lambreta", "cor": "azul", "ano": 2002}]

print("Iterando sobre as motod e acessando os valores:")
for moto in motos:
    print(f"Modelo: {moto['modelo']}, Marca: {moto['marca']}, Cor: {moto['cor']}, Ano: {moto['ano']}")

