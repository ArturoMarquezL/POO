class futbolista:
  
  Nombre = "Arturo"
  Apellidos = "Marquez"
  posicion = "delantero"
  equipo = "cruz azul"
  numero = "1"
  
  def __init__(self):
    print("Datos futbolista ")
    
  def anotar (self):
    print("anotar")

  def mover_balon (self):  
    print("mover el balon")

class fichaje (futbolista):
  def __init__(self):
    print("fichaje")   

  def mover_balon (self):  
    print("mover el balon a la canasta") 

objeto = futbolista() 
objeto.anotar()
objeto.mover_balon()
objeto_ficha= fichaje()
objeto_ficha.anotar()
objeto_ficha.mover_balon()
print(objeto_ficha.Nombre)
print(objeto_ficha.Apellidos)
print(objeto_ficha.posicion)
print(objeto_ficha.equipo)
print(objeto_ficha.numero)