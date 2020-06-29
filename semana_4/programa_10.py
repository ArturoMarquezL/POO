class classroom:
  
  clases = "8"
  materias = "8"
  grupo = "Ti22"
  alumnos = "Utec"
  informacion = "por materia"
  
  def __init__(self):
    print("constructor")
    
  def Estudiar (self):
    print("Estudiar")

  def aprender (self):  
    print("aprender")

class tareas (classroom):
  def __init__(self):
    print("tareas")  

  def aprender (self):  
    print("aprender en linea")    

objeto = classroom() 
objeto.Estudiar()
objeto.aprender()
objeto_estudi = tareas()
objeto_estudi.Estudiar()
objeto_estudi.aprender()
print(objeto_estudi.clases)
print(objeto_estudi.materias)
print(objeto_estudi.grupo)
print(objeto_estudi.alumnos)
print(objeto_estudi.informacion)