mensaje = "hola"
mensaje += " "
mensaje += "Ernesto"
print (mensaje)

print("concatenacion:")

mensaje = "hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("el resultado de la suma es: " + resultado)

print("busqueda:")

mensaje = " Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)

mensaje = "Hola Ernesto"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
