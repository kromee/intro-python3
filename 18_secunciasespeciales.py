import re

texto = "Siete séptimos son siete séptimas más de los que tienes"

resultado = re.findall("sép|timas|tienes|e|é|[a-z]", texto);

print(resultado);