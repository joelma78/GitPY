convidados=[]


for i in range(5):
        entrada = (input("Insira o nome do convidado : "))
        convidados.append(entrada)

for lista in convidados :
        if  len(lista) == 5:
               print(lista)
               
        else:
         
              print (" A lista está ficando grande.") 