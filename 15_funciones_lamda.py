import math;

def area (radio):
    resutado= round(math.pi* radio* radio, 2);
    print(resutado);

area (2);

area = lambda radio: round(math.pi* radio* radio, 2);
print(area(2));
