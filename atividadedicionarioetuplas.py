pontos_de_interesse = {"Torre eiffel": (48.8544, 2.2945),
                        "Estatua da Liberdade" : (40.6892, 74.0445),
                        "Machu Pichu": (-13.1631, -72.5450),
                        "Bondinho": (45.6547, 69.6548)}

print("Dicionário 'pontos_de_interesse'  : ")
print(pontos_de_interesse)
print("-" * 30)

# Acessar as coordenadas de um local específico 
nome_lugar_para_acessar = "Torre eiffel"
coordenadas_torre = pontos_de_interesse[nome_lugar_para_acessar]
print(f"Coordenadas de {nome_lugar_para_acessar}: {coordenadas_torre}")

latitude = coordenadas_torre[0]
longitude = coordenadas_torre[1]

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print  ("-"*30)

print("---Passo 4 : Adicionando um novo lugar ao dicionario---")
nome_novo_lugar = "Cristo Redentor"
coordenadas_novo_lugar = (-22.9519, -43.2105)
pontos_de_interesse[nome_novo_lugar] = coordenadas_novo_lugar
print(f"Dicionario apos adicionar '{nome_novo_lugar}': ")
print(pontos_de_interesse)
print("-"*30)

nome_lugar_para_acessar = "Cristo Redentor"
coordenadas_torre = pontos_de_interesse[nome_lugar_para_acessar]
print(f"Coordenadas de {nome_lugar_para_acessar}: {coordenadas_torre}")

latitude = coordenadas_torre[0]
longitude = coordenadas_torre[1]

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print  ("-"*30)                                   