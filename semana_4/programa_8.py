class calculadora:
  
  color = "blanco"
  Modelo = "2020"
  tipo = "solar"
  Marca = "casio"
  pantalla="chica"

  def __init__(self):
    print("constructor calculadora ")
    
  def sumar (self):
    print("sumar")

  def restar (self):  
    print("restar")

class calcusolar (calculadora):
  def __init__(self):
    print("constructor de calculadora solar") 

  def restar (self):  
    print("restar valores")     

objeto = calculadora() 
objeto.sumar()
objeto.restar()
objeto_solar = calcusolar()
objeto_solar.sumar()
objeto_solar.restar()
print(objeto_solar.color)
print(objeto_solar.Modelo)
print(objeto_solar.tipo)
print(objeto_solar.Marca)
print(objeto_solar.pantalla)