class coche:
  
  color = "blanco"
  Modelo = "2020"
  tipo = "deportivo"
  Marca = "mugstan"
  motor = "grande jajajaja xd "

  def __init__(self):
    print("constructor carro ")
    
  def conducir (self):
    print("conducir")

  def transportar (self):  
    print("transportar")

class cocheblanco (coche):
  def __init__(self):
    print("constructor de coche blanco")    

objeto = coche() 
objeto.conducir()
objeto.transportar()
objeto_carro = cocheblanco()
objeto_carro.conducir()
objeto_carro.transportar()
print(objeto_carro.color)
print(objeto_carro.Modelo)
print(objeto_carro.tipo)
print(objeto_carro.Marca)
print(objeto_carro.motor)