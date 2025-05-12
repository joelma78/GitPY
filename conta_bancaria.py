class Contabancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0 
        print(f"conta para {self.titular} criada com sucesso")

    def depositar (self, valor):
        if valor > 0:
          if self.saldo >= 0:
           self.valor += valor
           print(f" saque de R$ {self.valor:.2f} realizado. Verifique seu saldo atual: R$ {self.saldo:.2f}")
          else:
             print("valor de deposito invalido")
    
    def sacar (self, valor):
       if valor >0:
         if self.saldo >= 0:
            self.valor += valor
            print(f" saque de R$ {self.valor:.2f} realizado. Verifique seu saldo atual: R$ {self.saldo:.2f}")
         else:
           print("Saldo insuficiente para saque")
           
       else:
          print(" Valor de saque invalido")

    def consultar_saldo(self):
     print(f" saldo da conta de {self.titular} :    R$ {self.saldo:.2f}")
     
conta_joao = Contabancaria
conta_joao.depositar(1000)
conta_joao.depositar(500)
conta_joao.consultar_saldo()

    
      

