numsecreto =7
numero=input ("Insira seu palpite: ")
palpite= int(numero)

if palpite== numsecreto:
    print("Parabéns! Você acertou!")
elif numsecreto<10:
    print ("Tente novamente. O valor está muito baixo")
else:
    print("Tente novamente. O valor está alto")

