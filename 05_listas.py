telefonos = ["Nokia", "Motorola", "iPhone"]

#imprime todos
print(telefonos);
#por elemento de la lista
print(telefonos[1]);


#ultimo de la lista
print (telefonos[-1])
## con menos vas de el ultimo al primero.
print (telefonos[-2])

#eliminar de la lista
del telefonos[1];
del telefonos[-1];
print(telefonos);


#Eliminar por nombre Remove()
telefonos.remove("Nokia");
print(telefonos);


# eliminar Pop()
colores = ["verde", "azul", "negro"];
guardarLista = colores.pop(1);
print(colores);
print(guardarLista);

# añadir elementos al final de la lista  Append()
colores.append("Amarillo")
print(colores);


#añadir en cualquier pos Insert()
colores.insert(0,"rojo");
colores.insert(-1,"Gris");
print(colores);

## ordenar lista
colores.sort();
print(colores);
colores.sort(reverse=True);
print (colores);

print (sorted(colores));

#Contar elementos de la lista
print (len(colores));
