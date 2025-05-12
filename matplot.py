import matplotlib.pyplot as plt

horas_estudo = [2,3,4,5,6,7,10]
notas_prova = [50,60,75,80,45,87,90]
               
plt.scatter (horas_estudo, notas_prova, label='Notas dos Alunos')
plt.title (' Relaçao entre Horas de Estudo e Notas da Prova')
plt.xlabel ('Horas de Estudo')
plt.ylabel ('Notas de Prova')
plt.legend()

plt.show()