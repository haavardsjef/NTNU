#Multiplikasjon

def mult(tol):
	prod = 1
	dx = 1
	n = 0
	diff = 1
	while diff >= tol:	
		n += 1
		dx = (1+(1/(n**2)))
		prod2 = prod * dx
		diff = prod2-prod
		prod = prod2
	return prod, n
tol = float(input("Toleranse: "))	
prod, n = mult(tol)
print("Produktet ble", round(prod,2), "etter", n, "iterasjoner.")
	
		