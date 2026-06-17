class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")
            
    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: Fondos insuficientes.")
        elif monto <= 0:
            print("Error: El monto a retirar debe ser mayor a 0.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo}")

nombre_titular = input("Nombre del titular de la cuenta: ")
cuenta = CuentaBancaria(nombre_titular)

monto_deposito = float(input("¿Cuánto deseas depositar?: "))
cuenta.depositar(monto_deposito)

monto_retiro = float(input("¿Cuánto deseas retirar?: "))
cuenta.retirar(monto_retiro)