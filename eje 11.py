class Cuenta:
    def __init__(self,saldo):
        self.saldo = saldo
    def depositar(self, m):
        self.saldo += m
    def retirar(self, m):
        if m <= self.saldo:
            self.saldo -= m
        else:
            print("Salado insuficiente")
mi_cuenta = Cuenta(100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(150)
print(f"saldo final: {mi_cuenta.saldo}")
