class serie:
  
  canal="5"
  horario="5a6"
  dias="Luna a Viernes"
  capitulos="15"
  temporadas="5"

  def __init__(self):
    print("constructor de serie de tv ")
    
  def entretener (self):
    print("entretener")

  def disfrutar (self):  
    print("disfrutar")

class serie_5 (serie):
  def __init__(self):
    print("constructor de serie canal 5")    

objeto = serie() 
objeto.entretener()
objeto.disfrutar()
objeto_seri = serie_5()
objeto_seri.entretener()
objeto_seri.disfrutar()
print(objeto_seri.canal)
print(objeto_seri.horario)
print(objeto_seri.dias)
print(objeto_seri.capitulos)
print(objeto_seri.temporadas)