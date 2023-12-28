import datetime, locale

locale.setlocale(locale.LC_ALL, "");

fecha1= datetime.datetime(2023, 9, 29, 12, 40, 30);
#fecha sistema
fecha2= datetime.datetime.now();
print(fecha1);
#solo año
print(fecha2.year, fecha2.month, fecha2.day)

#strtime
fecha3= datetime.datetime.now();
print(fecha3.strftime("%A"));

