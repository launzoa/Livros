import numpy as np
import matplotlib.pyplot as plt

solAnalitica = lambda t: t * np.log(t) + 2*t
f = lambda t, y : 1 + (y/t)

a = 1; b = 2; h = 0.25; n = int((b-a) / h)

t = np.linspace(a, b, n+1)
y = solAnalitica(t)

# MÉTODO DE EULER APRIMORADO
e = np.zeros(n+1)
e[0] = 2

for i in range(n):
    k1 = f(t[i], e[i])

    eM = e[i] + h * k1

    k2 = f(t[i+1], eM)

    e[i+1] = e[i] + (h/2) * (k1 + k2)


# MÉTODO DO PONTO MÉDIO

p = np.zeros(n+1)
p[0] = 2

for i in range(n):
    k1 = t[i] + (h/2)

    k2 = p[i] + (h/2) * f(t[i], p[i])

    p[i+1] = p[i] + h * f(k1, k2)


# MÉTODO DE HEUN DE 3 ORDEM

u = np.zeros(n+1)
u[0] = 2

for i in range(n):
    k1 = f(t[i], u[i])

    k2 = f(t[i] + h/3, u[i] + (h/3) * k1)

    k3 = f(t[i] + (2*h)/3, u[i] + (2*h/3) * k2)

    u[i+1] = u[i] + (h/4) * (k1 + 3*k3)


# MÉTODO DE RUNGE-KUTTA DE QUARTA ORDEM

k = np.zeros(n+1)
k[0] = 2

for i in range(n):
    k1 = h * f(t[i], k[i])

    k2 = h * f(t[i] + (h/2), k[i] + (1/2) * k1)

    k3 = h * f(t[i] + (h/2), k[i] + (1/2) * k2)

    k4 = h * f(t[i+1], k[i] + k3)

    k[i+1] = k[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

plt.plot(t, y, '--', label="Solução analítica")
plt.plot(t, e, '--', label="Euler Modificado")
plt.plot(t, p, '--', label="Ponto Médio")
plt.plot(t, u, '--', label="Heun de 3 Ordem")
plt.plot(t, k, '--', label="Runge-Kutta de 4 ordem")

plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)

plt.legend()
plt.savefig("1c.png")
plt.show()