class Banco:
  
  cajeros = "automaticos" 
  Compania = "BBVA" 
  Asientos = "sillas" 
  Computadoras = " especiales"
  Ubicacion = "Mexico"
  
  def __init__(self):
    print("contructor Banco ")
    
  def cobrar (self):
    print("Cobrar")

  def transferir(self):  
    print("Trasferir")

class bancoBBVA(Banco):
  def __init__(self):
    print("Constructor BBVA") 

  def transferir(self):
    print("Transferencias de cuenta")     

objeto = Banco() 
objeto.cobrar()
objeto.transferir()
objeto_banco_bbva = bancoBBVA()
objeto_banco_bbva.cobrar()
objeto_banco_bbva.transferir()
print(objeto_banco_bbva.cajeros)
print(objeto_banco_bbva.Compania)
print(objeto_banco_bbva.Asientos)
print(objeto_banco_bbva.Computadoras)
print(objeto_banco_bbva.Ubicacion)