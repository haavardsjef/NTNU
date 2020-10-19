from math import sqrt, log
# Order of convergence for iterations
# Test problem: Newtons method for x^2-a=0
a = 4
print("\n")


def g(x):
    # return (x**2+a)/(2*x)   # g(x) = x-f(x)/f'(x)
    return (x-(x**3-x**2-x+1)/(3*x**2-2*x-1))   # g(x) = x-f(x)/f'(x)


x_exact = 1           # Exact solution
x = 2                      # Starting value
errors = [abs(x_exact-x)]        # Array to store errors
Nit = 10                    # Number of iterations

# Start the iterations
print('The Newton iterations:')
for k in range(Nit):
    x = g(x)                # One iteration
    ek = abs(x_exact-x)     # Find the error
    print('k = {:2d},   x_k = {:10.8f},   e_k = {:8.2e}'.format(k, x, ek))
    if ek < 1.e-15:         # If the error is small, terminate.
        Nit = k+1
        break
    errors.append(ek)            # Append the new error to the array of errors

# Find the order and the error constant C
print('\nThe order p and the error constant C')
for k in range(Nit-2):
    p = log(errors[k+2]/errors[k+1])/log(errors[k+1]/errors[k])
    C = errors[k+2]/errors[k+1]**p
    print('k = {:2d},  p = {:4.2f},  C = {:6.4f}'.format(k, p, C))

print("\n")
