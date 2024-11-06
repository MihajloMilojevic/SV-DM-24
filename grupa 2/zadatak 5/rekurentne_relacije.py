# FUNKCIJA: f(x) = x**2 - sin(2x)

import autograd.numpy as np
from autograd import grad, hessian

def f(x):
    return x**2 - np.sin(2*x)

def NjutnRapsonovMetod(x, epsilon, iteration = 0):
    xk = x - grad(f)(x)/hessian(f)(x)[0,0]
    iteration += 1
    if abs(x - xk) > epsilon:
        return NjutnRapsonovMetod(xk, epsilon, iteration)
    return xk, iteration

def MetodSecice(x1, x2, epsilon, iteration = 0):
    xk = x1 - grad(f)(x1)*(x1 - x2)/(grad(f)(x1) - grad(f)(x2))
    iteration += 1
    if abs(xk - x2) > epsilon:
        return MetodSecice(x2, xk, epsilon, iteration)
    return xk, iteration

def FibonacijevBroj(n, num1 = 1, num2 = 1):
    if n != 0:
        return FibonacijevBroj(n-1, num2, num2 + num1)
    return num2

def FibonacijevMetod(a, b, n, iteration = 0, max = True):
    x1 = a + FibonacijevBroj(n-2)/FibonacijevBroj(n)*(b-a)
    x2 = a + FibonacijevBroj(n-1)/FibonacijevBroj(n)*(b-a)
    iteration += 1
    if n != 0:
        if max:
            if f(x1) > f(x2):
                b = x2
            else:
                a = x1
            return FibonacijevMetod(a, b, n-1)
        else: 
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1
            return FibonacijevMetod(a, b, n-1)
    return a,b, iteration

def ZlatniPresek(a, b, epsilon, max = True, iteration = 0):
    c = 0.618
    x2 = b - (b-a)/c
    x1 = a + (b-a)/c
    iteration += 1
    if abs(a - b) > epsilon:
        if max:
            if f(x2) < f(x1):
                a = x1
            else:
                b = x2
        else:
            if f(x2) < f(x1):
                a = x2
            else:
                b = x1
        return ZlatniPresek(a, b, epsilon, max)
    return (a + b) /2, iteration
