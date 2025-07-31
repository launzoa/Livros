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

plt.plot(t, y, 'r-+', label="Solução Analítica")
plt.plot(t, w, 'b-+', label="Método de Euler Modificado")
plt.plot(t, u, 'g-+', label="Método de Ponto Médio")
plt.plot(t, v, 'y-+', label="Método de Heun (RK2)")

plt.title("Euler Modificado vs Ponto Médio vs RK2 vs RK4")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()

plt.savefig("a.png")
plt.show()