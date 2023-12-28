class Usuarios:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def muestra_datos(self):
        print("nombre: "+ self.nombre, "edad: ", self.edad);

usuario1= Usuarios("Eduardo", 35);
usuario1.muestra_datos();


class Usuarios_premium (Usuarios):
    def __init__(self, nombre, edad, instagram):
        Usuarios.__init__(self, nombre, edad)
        self.instagram= instagram
    def datos_premium(self):
           print("nombre: "+ self.nombre, "edad: ", self.edad, "insta", self.instagram);



usuario2 = Usuarios_premium("Juan", 40, "kromee344");
usuario2.datos_premium();