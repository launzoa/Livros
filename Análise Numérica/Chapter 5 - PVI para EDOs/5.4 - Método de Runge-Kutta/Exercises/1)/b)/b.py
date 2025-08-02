import numpy as np
import matplotlib.pyplot as plt

solAnalitica = lambda t: t + 1/(1-t)

f = lambda t,y: 1 + (t-y)**2

a = 2; b = 3; h = 0.5; n = 2

t = np.linspace(a,b, n+1)
y = solAnalitica(t)
# MÉTODO DE EULER MODIFICADO

w = np.zeros(n+1)
w[0] = 1

for i in range(n):
    k1 = f(t[i], w[i])

    eM = w[i] + h*k1

    k2 = f(t[i+1], eM)

    w[i+1] = w[i] + (h/2) * (k1+ k2)


# MÉTODO DE PONTO MÉDIO

p = np.zeros(n+1)
p[0] = 1

for i in range(n):
    k1 = t[i] + (h/2)

    k2 = p[i] + (h/2) * f(t[i], p[i])

    p[i+1] = p[i] + h * f(k1, k2)


# MÉTODO DE HEUN (3 ORDEM)

j = np.zeros(n+1)
j[0] = 1

for i in range(n):
    k1 = f(t[i], j[i])

    k2 = f(t[i] + (h/3), j[i] + (h/3) * k1)

    k3 = f(t[i] + ((2*h)/3), j[i] + ((2*h)/3) * k2)

    j[i+1] = j[i] + (h/4) * (k1 + 3*k3)


# MÉTODO RUNGE-KUTTA 4 ORDEM (RK4)

k = np.zeros(n+1)
k[0] = 1

for i in range(n):
    k1 = h * f(t[i], j[i])

    k2 = h * f(t[i] + (h/2), k[i] + (1/2) * k1)

    k3 = h * f(t[i] + (h/2), k[i] + (1/2) * k2)

    k4 = h * f(t[i+1], k[i] + k3)

    k[i+1] = k[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

plt.plot(t, y, '--', label="Solução analítica")
plt.plot(t, w, '--', label="Método de Euler Modificado")
plt.plot(t, p, '--', label="Método de Ponto Médio")
plt.plot(t, j, '--', label="Método de Heun de 3 Ordem")
plt.plot(t, k, '--', label="Método de Runge-Kutta de 4 Ordem (RK4)")

plt.grid(True)
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")

plt.legend()
plt.savefig("1b.png")
plt.show()