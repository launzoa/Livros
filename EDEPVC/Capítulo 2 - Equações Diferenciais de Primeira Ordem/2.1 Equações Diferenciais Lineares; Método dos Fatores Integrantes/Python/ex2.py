import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1.5, 20)
y = np.linspace(-5, 2, 20)

T, Y = np.meshgrid(t, y)

DY = 2*Y + T**2 *np.exp(2*T)
DT = np.ones(DY.shape)

magnitudade = np.sqrt(DT**2 + DY**2)
DT = DT / magnitudade
DY = DY / magnitudade

plt.figure(figsize=(10, 6))
plt.quiver(T,Y,DT,DY)
plt.title("Campo de direções para y' - 2y = t²e^{2t}")
plt.xlabel("Tempo (t)")
plt.ylabel("y(t)")
plt.grid(True)

plt.show()