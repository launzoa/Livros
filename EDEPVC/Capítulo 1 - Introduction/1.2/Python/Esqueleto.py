import numpy as np
import matplotlib.pyplot as plt

""" Gráficos 2D
x = np.arange(-2, 2, 0.01)
y = np.exp(x)
plt.plot(x, y, color="green", linewidth=3.0) # Plota o gráfico, eixos

plt.title("Gráfico") # Título do gráfico
# plt.axis("off") Tira o eixo
# plt.savefig("figura.png", transparent=True) Salvar a imagem. Modo transparente o que permite flexibilidade para apresentações
plt.show()
"""

# Cria a figura e os eixos 3D
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

def z(x,y):
    return x**2 + y**2

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = z(X, Y)

ax.plot_surface(X, Y, Z, color="aqua")
ax.set_title("Paraboloide: z = x² + y²")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
plt.show()