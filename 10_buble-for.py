for x  in "python":
    print(x);


cursos=["Javascript", "C#", "html y css"]

for x  in cursos:
    if x=="C#":
        continue
    print(x);


#continue and break
for x  in cursos:
    if x=="C#":
        #continue
        break
    print(x);


# in range
for x in range (10):
    print(x);

# de rango a otro, y un salto de 2 en 2
for x in range (5,30, 2):
    print(x);

# in range con else 
for x in range (10):
    print(x);
else:
    print("proceso terminado");