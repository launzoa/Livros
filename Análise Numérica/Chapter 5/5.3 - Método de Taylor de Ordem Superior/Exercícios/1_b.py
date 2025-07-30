import numpy as np
import matplotlib.pyplot as plt


solAnalitica = lambda t,C: t - 1/(t+C)

a = 2; b = 3; h = 0.5; n = 2; C = -1

ti = np.linspace(a, b, n+1)
wi = np.zeros(n+1)
wi[0] = 1


yi = solAnalitica(ti, C)

for i in range(n):
    t = ti[i]
    w = wi[i]

    f = 1 + (t-w)**2        # (f) Função

    f1 = -2 * (t-w)**3      # (f') Primeira derivada

    wi[i+1] = w + (h * f) + ((h**2) /2) * f1


plt.plot(ti, wi, 'b-+', label="Taylor 2 Ordem")
plt.plot(ti, yi, 'r-+', label="Solução Analítica")
plt.xlabel("Tempo (t)")
plt.ylabel('y(t)')
plt.grid(True)
plt.title("Taylor 2 Ordem Superior")
plt.legend()
plt.savefig('ex1_b.png')
plt.show()