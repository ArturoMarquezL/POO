class Temperaturas:#definimos la clase

    def __init__(self):# metodo constructor
        pass

    def promedioTemperaturas(self):#metodo
        centigrados=[] #almacenara los grados en centigrados
        farentheit=[]#almacena los grados que ce convertieron a fahrenheit
        respuesta="S"
        contador=0 #cuenta el numero veses que se repitio el codigo

        while respuesta=="S" or respuesta=="s": #si respuesta es S o s
            contador+=1 #contador aumentara 1 vez
            temperatura=int(input("Ingresa la temperatura ")) #ingresa la temperatura de tipo entero
            centigrados.append(temperatura) #agraga los valores de temperatura a la variable centigrados
            convertir=(temperatura*9/5)+32 #convierte los centigrados a farentheit
            farentheit.append(convertir) #agrega la convercion a la variable farentheit
            respuesta=input("¿Deseas leer otra temperatura? ") #pregunta si otra temperatura
            if respuesta=="N" or respuesta=="n": #si la se respuesta es N o n

                abrir=open("Temperaturas.txt","a") #abre el archivo de texto en modo de agregar
                abrir.write("Resultado\n") #agrga el siguente texto Resultado + un salto de linea
                abrir.write("las temperaturas leidas en centigrados son "+str(centigrados)+"\n") #escrebe las temperaturas de centigrados
                abrir.write("Las temperaturas convertidas a farentheit son "+str(farentheit)+"\n")#escribe las temperatutas en farentheit
                promedio=sum(centigrados)/contador#suma todos los grados °C y los divide entre la variavle contador para determinar el promedio de las temperaturas
                promedio_farentheit=sum(farentheit)/contador#suma todos los °F y los divide entre la variable contador para el promedio de las temperaturas
                abrir.write("El promedio de la temperatura en centigrados es "+str(promedio)+"\n")#escreibe el promedio de los °C
                abrir.write("El promedio de las temperaturas en farentheit es "+str(promedio_farentheit)+"\n")#escribe el promedio de los °F
                abrir.close()#cierra el archivo de texto

                print("El promedio de la temperatura en centigrados es "+str(promedio))#imprime en pantalla el promedio de °C
                
                print("El promedio de las tempertaruras en farentheit es "+str(promedio_farentheit)) #imprime en pantalla el promedio de °F

                break #termina el proceso

objeto_Temperaturas=Temperaturas() #llamar a la clase primaria
objeto_Temperaturas.promedioTemperaturas() #llamar a su metodo.