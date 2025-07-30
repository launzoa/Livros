import numpy as np
import matplotlib.pyplot as plt


solAnalitica = lambda t,C: (t/5) * np.exp(3*t) - (1/25) * np.exp(3*t) + C * np.exp(-2*t)

a = 0; b = 1; h = 0.5; n = 2; C = 1/25

ti = np.linspace(a, b, n+1)
wi = np.zeros(n+1)
wi[0] = 0


yi = solAnalitica(ti, C)

for i in range(n):
    t = ti[i]
    w = wi[i]

    f = t * np.exp(3*t) - (2 * w)               # (f) Função

    f1 = np.exp(3*t) + t * np.exp(3*t) + 4*w    # (f') Primeira derivada

    wi[i+1] = w + (h * f) + ((h**2) /2) * f1


plt.plot(ti, wi, 'b-+', label="Taylor 2 Ordem")
plt.plot(ti, yi, 'r-+', label="Solução Analítica")
plt.xlabel("Tempo (t)")
plt.ylabel('y(t)')
plt.grid(True)
plt.title("Taylor 2 Ordem Superior")
plt.legend()
plt.savefig('ex1_a.png')
plt.show()