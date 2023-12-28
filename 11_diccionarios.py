teclado1={
    "categoria":"teclados",
    "modelo": "Modelo x",
    "Precio": 78.99
}

teclado2={
    "categoria":"teclados",
    "modelo": "Modelo y",
    "Precio": 89.99
}

#consulta por diccionario
consulta = teclado1["modelo"], teclado1["Precio"], teclado2["modelo"];
print(consulta);

#método dict
print (dict(teclado1));


#modificar el precio 

teclado1["Precio"]="85";
print (teclado1.get("Precio"));

## for 
for x, y in teclado2.items():
    print(x+":",y)   

#elimina precio
del teclado1["Precio"];
print (dict(teclado1));


# eliminar diccionario
teclado1.clear();
print (teclado1);

teclado1={
    "categoria":"teclados",
    "modelo": "Modelo x",
    "Precio": 78.99
}

#copia
unacopia = teclado1.copy();
print (unacopia);

#diccionarios dentro de diccionario

teclado={
"teclado1":{
    "categoria":"teclados",
    "modelo": "Modelo x",
    "Precio": 78.99
},

"teclado2":{
    "categoria":"teclados",
    "modelo": "Modelo y",
    "Precio": 89.99
}

}

print(teclado)
