itic3 = [" Sajith Alexandro Montaño Grimaldo, Emanule de Jessús Esparza, Melani Chavez, Fernanda Pantoja, Eduardo Flores Gallegos"]
carreras = [" tecnologias de la comunicacion e informacion, gestion empresarial, logistica, mecatronica,"]
edades = ["18,18,19,20,20,19,19,18,19,19,19,19"]



# imprimir lista
print (carreras)
print (itic3)
print(edades)

# imprimir el tercer campo de listas 
print(" carreras _ [2] ")

# agregar elementos al final de la lista
itic3.append('sajih') 
print(itic3)


# agregar otro lista 
itic3.extend(['juan,santi'])
print(itic3)



# agregar elementos en la pocición 5
itic3.insert(4,'reinier')
print(itic3)


# borrar un elemento determinado
del edades[0]
print(edades)


# ver el tamaño de nuestras listas 
print(len(edades))
print(len(itic3))
print(len(carreras))



# eliminar un elemento en especifico
edades.remove(32)
print(edades)
print("-----------------------------")


# ordenar elementos 
print(edades)
edades.sort()
print(edades)
