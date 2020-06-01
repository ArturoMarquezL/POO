class cajero:
  
  cajeros = "BBVA" 
  Compania = "BBVA" 
  pantalla = "medina" 
  color = "blanco y azul"
  Ubicacion = "Mexico"
  
  def __init__(self):
    print("contructor cajeros ")
    
  def cobrar (self):
    print("Cobrar")

  def transferir(self):  
    print("Trasferir")

class bancoBBVA(cajero):
  def __init__(self):
    print("Constructor cajeros BBVA")    

objeto = cajero() 
objeto.cobrar()
objeto.transferir()
objeto_banco_bbva = bancoBBVA()
objeto_banco_bbva.cobrar()
objeto_banco_bbva.transferir()
print(objeto_banco_bbva.cajeros)
print(objeto_banco_bbva.Compania)
print(objeto_banco_bbva.pantalla)
print(objeto_banco_bbva.color)
print(objeto_banco_bbva.Ubicacion)