class vacaciones:
  
  Lugar= "tuxpan"
  fecha="31/05/2020"
  Hora_de_salida="1am"
  hora_de_llegada="6am"
  transporte = "carro"

  def __init__(self):
    print("constructor de vacaciones ")
    
  def conocer (self):
    print("conocer")

  def disfrutar (self):  
    print("disfrutar")

class expedicion (vacaciones):
  def __init__(self):
    print("constructor de expedicion")  

  def disfrutar(self):
    print("disfrutar de la vista")    

objeto = vacaciones() 
objeto.conocer()
objeto.disfrutar()
objeto_expe = expedicion()
objeto_expe.conocer()
objeto_expe.disfrutar()
print(objeto_expe.Lugar)
print(objeto_expe.fecha)
print(objeto_expe.Hora_de_salida)
print(objeto_expe.hora_de_llegada)
print(objeto_expe.transporte)