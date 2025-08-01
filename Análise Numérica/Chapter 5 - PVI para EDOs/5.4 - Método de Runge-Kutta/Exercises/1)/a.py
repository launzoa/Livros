import numpy as np
import matplotlib.pyplot as plt

solAnalitica = lambda t: ((1/5) * t * np.exp(3*t)) - (((1/5)**2) * np.exp(3*t)) + (((1/5)**2) * np.exp(-2*t))

a = 0; b = 1; h = 0.5; n = 2

t = np.linspace(a,b, n+1)
w = np.zeros(n+1)
w[0] = 0

y = solAnalitica(t)

f = lambda t,y: t * np.exp(3*t) - 2*y

# MÉTODO DE EULER APRIMORADO
for i in range(n):
    k1 = f(t[i], w[i])

    eq = w[i] + h * k1
    k2 = f(t[i+1], eq)

    w[i+1] = w[i] + (h/2) * (k1 + k2)


u = np.zeros(n+1)
u[0] = 0
# MÉTODO DE PONTO MÉDIO
for i in range(n):
    k1 = t[i] + (h/2)

    k2 = u[i] + (h/2) * f(t[i], u[i])

    u[i+1] = u[i] + h * f(k1, k2)


v = np.zeros(n+1)
v[0] = 0
# MÉTODO DE HEUN (RK2)
for i in range(n):
    k1 = f(t[i], v[i])

    k2 = f(t[i+1], v[i] + h * k1)

    v[i+1] = v[i] + h * (k1+k2) / 2


j = np.zeros(n+1)
j[0] = 0
# MÉTODO DE HEUN (Terceira Ordem)
for i in range(n):
    k1 = f(t[i], j[i])

    k2 = f(t[i] + (h/3), j[i] + (h/3) * k1)

    k3 = f(t[i] + ((2*h)/3), j[i] + ((2*h)/3) * k2)

    j[i+1] = j[i] + (h/4) * (k1 + 3*k3)


k = np.zeros(n+1)
k[0] = 0
#MÉTODO DE RUNGE-KUTTA DE QUARTA ORDEM (RK4)
for i in range(n):
    k1 = h * f(t[i], k[i])

    k2 = h * f(t[i] + (h/2), k[i] + (1/2) * k1)

    k3 = h * f(t[i] + (h/2), k[i] + (1/2) * k2)

    k4 = h * f(t[i+1], k[i] + k3)

    k[i+1] = k[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

plt.plot(t, y, '--', label="Solução Analítica")
plt.plot(t, w, '--', label="Método de Euler Modificado")
plt.plot(t, u, '--', label="Método de Ponto Médio")
plt.plot(t, v, '--', label="Método de Heun (RK2)")
plt.plot(t, j, '--', label="Método de Heun (3 ordem)")
plt.plot(t, k, '--', label="Runge-Kutta de 4 ordem (RK4)")

plt.title("Euler Modificado vs Ponto Médio vs RK2 vs Heun O(3) vs RK4")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()

plt.savefig("a.png")
plt.show()