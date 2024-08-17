import cmath
from math import sqrt
#Le pregunto los datos al usuario, para este caso no hay necesidad de que los ingrese en orden
t1=float(input("Ingrese el primer termino  "))
exp1=int(input("ingrese el exponente correspondiente al primer termino para la variable x, si no tiene excriba 0: "))
t2=float(input("Ingrese el segundo termino "))
exp2=int(input("Ingrese el exponente correspondiente al segundo termino para la variable x, si no tiene escriba 0: "))
t3=float(input("Ingrese el tercer termino  "))
exp3=int(input("Ingrese el exponente correspondiente al tercer termino para la variable x, si no tiene escriba 0: "))
#Con los datos ingresados, ya que puede ser en desorden, procedemos a comparar sus exponentes para organizar sus terminos de tal manera que quede: 
# ax**2+bx+c=0
if exp1==2: 
    a=t1
    if exp2==1 and exp3==0:
        b=t2
        c=t3 
        print(a,"x**2",b"x",c)
    else: 
        b=t3
        c=t2
        print(a,"x**2",b"x",c)
elif exp2==2: 
    a=t2
    if exp1==1 and exp3==0:
        b=t1
        c=t3 
        print(a,"x**2",b"x",c)
    else: 
        b=t3
        c=t1
        print(a,"x**2",b"x",c)
elif exp3==2: 
     a=t3
     if exp1==1 and exp2==0:
        b=t1
        c=t2 
        print(a,"x**2",b"x",c)
     else: 
        b=t2
        c=t1
        print(a,"x**2",b"x",c)

#Con los resultados ya organizados por la comparación, 
#Llamo a la función que calculará la ecuación cuadratica: 

print("Orden de terminos: "+ a, b, c)

def calcular(): 
 y = b ** 2 - 4 * a * c
 r = cmath.sqrt(y)
 x1= (-b + r) / (2 * a)
 x2 = (-b - r) / (2 * a)
 print("El resultado es:", x1, "y", x2)
 return x1, x2 


calcular()
