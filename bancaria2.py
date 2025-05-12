class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial = 0):
        self.numero_conta = numero_conta
        self._saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0 :
            self._saldo += valor
            print (f" Deposito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Valor para depoisito invalido")

    def sacar(self, valor):
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f" Saque de R$ {valor:.} realizado na conta {self.numero_conta}. ")
                return False
        else:
            print("Valor para saque invalido")
            return False

    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta} : R$ {self._saldo:.2f}")


class ContaCorrente(ContaBancaria): 
    def __init__ (self, numero_conta, saldo_inicial=0, limite_cheque_especial=0): 

        super().__init__(numero_conta, saldo_inicial)

        self.limite_cheque_especial = limite_cheque_especial

        print(f" Conta Corrente {self.numero_conta} criada com limite de cheque especial de R$ {self.limite_cheque_especial:.2f}")

    def sacar (self, valor) :
        if valor > 0:
                if self._saldo + self.limite_cheque_especial >= valor:
    
            if  self._saldo -= valor

                print(f"Saque de R$ {valor:.2f} realizado na conta corrente {self.numero_conta}")
                if self._saldo < 0:
                    print(f" Utilizando cheque especial. Saldo atual: R$ {self.numero_conta}.")
                    return True
                else:
                    print(f" Erro: saldo insuficiente (Incluindo cheque especial) na conta {self.numero_conta}.")
                    return False
            else:    
                print("Valor para saque invalido")

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, taxa_juros=0.0):
             super().__init__(numero_conta, saldo_inicial)     
             self.taxa_juros = taxa_juros   
             print(f" conta poupanca {self.numero_conta} criada com taxa de juros {self.taxa_juros*100:.2f} %")     


    def aplicar_juros(self):
           
           if self.taxa_juros > 0 and self._saldo > 0 :
               
               juros = self._saldo * self.taxa_juros

               self._saldo += juros

    print(f" juros de R$ {juros:.f} aplicados na conta {self.numero_conta}. Novo saldo: R$ {self._saldo:.f}") 

    else:
    
    print(f"Juros não aplicados na conta {self.numero_conta} . Saldo não positivo ou taxa zero ")  


Conta_Corrente = Conta_Corrente (12345-6 , 400, 500)
Conta_Corrente.conta.verificar_saldo()
Conta_Corrente.depositar (200.0)



