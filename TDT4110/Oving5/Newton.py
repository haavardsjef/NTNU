#Newtons metode av Håvard Hjelmeseth ITGK Oving 5
#Importer moduler
import math

#Definer funksjoner
def f(x):
	ans = ((x - 12)*(math.e**(5*x))) - (8*((x+2)**2))
	return ans

def g(x):
	ans = (-1*x)-(2*x**2)-(5*x**3)+(6*x**4)
	return ans
	
def derivate(h,x,func):
	ans = (func(x+(h/2))-func(x-(h/2)))/h
	return round(ans,7)

def newtons_method(h,x,func,tol):
    dx = tol+1
    x_new = x
    while dx >= tol:
        x_old = x_new
        x_new = x_old - func(x_old)/derivate(h, x_old, func)
        dx = abs(x_new-x_old)
    return x_new

#Kall funksjoner
print("f(0) =", f(0))
print("g(1) =", g(1))
print("Derivate(0.000001,-2,f) =", derivate(0.000001,-2,f))
print("Funksjonen naermer seg x =",newtons_method(0.00000001,-2,f,0.0000000001), ", da er y =", f(newtons_method(0.00000001,-2,f,0.0000000001)))
