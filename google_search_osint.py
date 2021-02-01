#Marcelino Joshua Campillo Arjon - Fecha de creacion: 31 de enero de 2021
#Version 1.0

# Importando el modulo de Google, modulo para llamar a path, modulo para el tiempo y hora, modulo para abrir csv
from googlesearch import search
import os.path
import csv
import time

# Guarda terminos a buscar en una lista
lista_terminos = []  # Definicion de listas
fila = 0 # Numero de resultados
opcion = 0 # Seleccion del menu


# Opciones del menu
print ("1: Carga archivo con terminos de busqueda")
print ("2: Ingresa manualmente los terminos")
opcion = input('Ingresa la opcion de ingreso de terminos: ')
opcion = int(opcion) 
#print (opcion)

# Procedimientos de los menus
if opcion == 1:
	# Seleccionamos archivo con terminos de busqueda y lo agregamos a una lista
	archivo = input('Ingresa el path completo de tu archivo de terminos a continuacion: ')
	f=open(archivo)
	reader = csv.reader(f)
	for row in reader:
		temp=row
		termino=temp[0]
		lista_terminos.append(termino)

		
elif opcion == 2:
	# El usuario ingresa manualmente los terminos y los pone en una lista
	while True:
    		termino = input('Ingresa un termino (deja vacio para finalizar): ')
    		if not termino:
        		break
    		lista_terminos.append(termino)
else:
	print ("Error vuelve a intentarlo")

print ("Lista de terminos: ")
print(lista_terminos) # Para imprimir los terminos ingresados

save_path = input('Ingresa el directorio para guardar tus resultados: ') #Directorio para guardar tus archivos

Manifest_file=time.asctime() + "_Manifest.csv" #Archivo de manifest
Manifest=os.path.join(save_path,Manifest_file)

print ("Podras encontrar tu archivo de resultados en la siguiente ruta: ",Manifest)
#with open(Manifest, 'w', newline='') as file: #Escribimos en el archivo de manifest
#	writer2 = csv.writer(file)
#	writer2.writerow(["Keyword","Results","Path"])

f2 = open(Manifest, 'w', newline='') #Escribimos en el archivo de manifest
writer2 = csv.writer(f2)
writer2.writerow(["Keyword","Results","Path"])


for j in lista_terminos: #Llamamos a la lista de terminos ingresados
	name_of_file = j + "_Google.csv" #Nombre de archivo se complementa con lista de terminos
	completeName = os.path.join(save_path, name_of_file) #Completar el nombre del archivo
	#with open(completeName) as csv_file: #Abrimos el archivo


#Escritura de los resultados de las URL en archivo CSV
	with open(completeName, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["#", "URL"])
		
		fila = 0 #Reiniciamos resultados
		print ('Tiempo de espera de 60 segundos  - Buscando el termino ',j,':') #Imprime que termino esta buscando en este momento
		time.sleep(60) #Esperamos un minuto
	
		
		for i in search(j,lang='es',num=10,start=0,stop=100,pause=2.0,safe='off'): #Hacemos busqueda
			writer.writerow([fila+ 1,i])
			fila = fila + 1
		print ('El termino ',j,'arrojo ',fila,'resultados') #Imprime cuantos resultados
		writer2.writerow([j,fila,completeName])
