class estudiante:
  
  Nombre = "Arturo"
  Apellidos = "Marquez"
  Matricula = "1719110363"
  Escuela = "Utec"
  Grado = "2"
  
  def __init__(self):
    print("Datos estudiante ")
    
  def Estudiar (self):
    print("Estudiar")

  def aprender (self):  
    print("aprender")

class estudia (estudiante):
  def __init__(self):
    print("Estudiante")

  def aprender (self):
    print("Aprender a desenvolverce")      

objeto = estudiante() 
objeto.Estudiar()
objeto.aprender()
objeto_estudi = estudia()
objeto_estudi.Estudiar()
objeto_estudi.aprender()
print(objeto_estudi.Nombre)
print(objeto_estudi.Apellidos)
print(objeto_estudi.Matricula)
print(objeto_estudi.Escuela)
print(objeto_estudi.Grado)