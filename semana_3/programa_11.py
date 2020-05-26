class Banco:
  def __init__(self):
    print("Constructor de banco")
     
  def atributos(self):
    print("Cajeros") 
    print("Compañia") 


  def metodos(self):
    print("Trasferir")
    print("Cobrar")
    print("Prestar")
    print("Consultar Saldo")
    print("depositar")

class bancoBBVA(Banco):
  def __init__(self):
    print("Constructor BBVA")    

objeto = Banco()
objeto.atributos() 
objeto.metodos()

objeto_banco_bbva = bancoBBVA()
objeto_banco_bbva.atributos()
objeto_banco_bbva.metodos()