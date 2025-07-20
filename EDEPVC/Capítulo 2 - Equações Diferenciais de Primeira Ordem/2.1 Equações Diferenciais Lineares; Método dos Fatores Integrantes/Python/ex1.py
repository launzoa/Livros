import numpy as np
import matplotlib.pyplot as plt

# Intervalo dos pontos (t,y)
t = np.linspace(-1, 3, 20)
y = np.linspace(-1, 1, 20)

T, Y = malha = np.meshgrid(t, y) # Criando a malha com os pontos (t,y)

DY = T + np.exp(-2*T) - (3 * Y)
DT = np.ones(DY.shape)

magnitude = np.sqrt(DT**2 + DY**2)
DT = DT / magnitude
DY = DY / magnitude

plt.figure(figsize=(10,7))
plt.quiver(T, Y, DT, DY,  color="b")

plt.title("Campo de direções para y' + 3y = t + e^{-2t}")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)


plt.show()