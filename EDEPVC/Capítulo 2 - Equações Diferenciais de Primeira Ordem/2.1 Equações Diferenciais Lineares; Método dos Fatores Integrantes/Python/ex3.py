import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 10, 20)
y = np.linspace(-10, 10, 20)

T,Y = np.meshgrid(t, y)

DY = -Y + T*np.exp(-T) + 1
DT = np.ones(DY.shape)

magnitude = np.sqrt(DT**2 + DY**2)
DT = DT / magnitude
DY = DY / magnitude

plt.figure(figsize=(7,4))
plt.quiver(T, Y, DT, DY, color="b")
plt.title("Campo de direções da EDO y' + y = te^{-t} + 1")
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()