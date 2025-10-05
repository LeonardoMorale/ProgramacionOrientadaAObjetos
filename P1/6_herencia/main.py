from coches import *

""" coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,5)
 """

#Solicitar los datos que posteriormente seran los atributs del objeto
""" num_coches = int(input("Cuantos coches tiene?"))
for i in range(0,num_coches):
    print("Datos del auto")
    marca = input("Marca: ").upper()
    color = input("Color: ").upper()
    modelo = input("Modelo: ").upper()
    velocidad = int(input("Velocidad: ").upper())
    potencia = int(input("Potencia: ").upper())
    plazas = int(input("Plazas: ").upper())
    coche = Coches(marca,color,modelo,velocidad,potencia,plazas)

 """

coche = Coches("BMW","Blanco","2020",220,100,2)
print(coche._color,coche.acelerar())
camion = Camiones("Volvo","Azul","2012",200,100,2,4,2000)
print(camion._color,camion.acelerar())
camioneta = Camionetas("RAM","Gris","2023",180,90,4,2,4)
print(camioneta._color,camioneta.acelerar())