import numpy as np
import matplotlib.pyplot as plt

# Equação Q(t) = VC*(1 - 1/e^t/RC)

if __name__ == "__main__":
    V = 10; R = 1; C = 1
    t = np.arange(0, 10, 0.01)

    Q = (V * C) * (1 - np.exp(-t / (R * C)))

    plt.figure(figsize=(10, 6))
    plt.plot(t, Q, "b--")

    plt.title('Carga de um Capacitor em um Circuito RC')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Carga (Coulombs)')
    plt.grid(True)
    plt.legend()

    plt.show()