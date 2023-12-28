def saludo(saludo):
    print(saludo);

saludo("eduardo "+ "Saludando desde la función");


# pasando argumentos 
def alumnos (*args):
    print("Argumentos: " + args[1]);

alumnos ("alumno 1", "Alumno 2", "Alumno3");



##  argumentos obligatorios y argumentos arbitrarios
def alumnos_maestros (profesor, sustituto, *args):
    print("Profesor: " +  profesor);
    print("Sutituto: " +  sustituto);
    for x in args:
        print("Alumno: " + x);

lista_alumnos = ["Eduardo", "Juan", "Rosario"];
alumnos_maestros ("Patricio", "Soledad", *lista_alumnos) ;        


## argumento por default
def colores (color="Rojo"):
    print("Mi color favorito es el "+ color);

colores("Azul");
colores();
colores("Amarillo");

