class Datos: 
  
  def __init__(self): #costructor
    pass

  def bucleWhile(self): #metodo que hace el bucle While
    respuesta="S" #caracter para la respuesta
    while respuesta=="S" or respuesta=="s": #para saber si se continua el programa

      cadena=input() #para meter el valor
      print(cadena) #imprimir la cadena
      print(cadena.replace(" ", "")) #elimina los espacios de la cadena
      print(len(cadena)) #lee la longitud de la cadena
      
      if cadena.isalpha()==True or cadena.islower()==True or cadena.istitle()==True: # checa si es de tipo cadena

        print("Tu dato es de tipo cadena")
      if cadena.isdigit()==True: #checa si es tipo numero
        print("Tu dato es de tipo numerico")
      if cadena.isdecimal()==True: #checa si es tipo decimal
        print("Tu dato es de tipo decimal")
      print(cadena.split(" "))#separa cada parte por caracter

      respuesta=input("¿Desea checar otra cadena s/n?")#pregunta si deseas checar otra cadena
      if respuesta=="N" or respuesta=="n": #si la respuesta es N o n se rompe el bucle y se termina el programa
        break

        
objecto_cadena=Datos() 
objecto_cadena.bucleWhile()