class avion:
  
  color = "blanco"
  Modelo = "2020"
  Aerolinea = "Mexico"
  Marca = "airbus"
  motores = "2 motores"

  def __init__(self):
    print("constructor de avion ")
    
  def volar (self):
    print("volar")

  def transportar (self):  
    print("transportar")

class avionair (avion):
  def __init__(self):
    print("constructor avion air")    

  def transportar (self):
    print("transportar la mercancia")  

objeto = avion() 
objeto.volar()
objeto.transportar()
objeto_air = avionair()
objeto_air.volar()
objeto_air.transportar()
print(objeto_air.color)
print(objeto_air.Modelo)
print(objeto_air.Aerolinea)
print(objeto_air.Marca)
print(objeto_air.motores)