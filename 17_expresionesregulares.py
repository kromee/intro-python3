import re

texto = "texto a buscar para expresión regular";
busqueda = re.search("buscar", texto);
print (busqueda);

#buscar todo
busquedaall = re.findall("x", texto);
print (busquedaall);


#separar palabras y que busque hasta 4 espacios
split = re.split(" ", texto, 3);
print (split);



#reemplaza laas coinciddencias y limitar a 4 espacios
split = re.sub(" ","-----", texto, 4);
print (split);
