import matplotlib.pyplot as plt
import numpy as np

E = 10.0 # Tensao constante da fonte
C = 0.000001 # Capacitancia
R = 2000.0 # Resistencia

### Condicao inicial ###

t0 = 0.0 # tempo incial
q0 = 0.0 # carga inicial

h = 0.000001

### Tempo maximo da simulacao ###

M = 6*R*C

vetQ = [q0]
vetT = [t0]
vetE = [E]

while(t0 < M):

        
    E1 = (R * np.diff(q0, t0) + (1/C)) * q0
    t1 = t0 + h
    E = E1
    q1 = q0 + h
    t0 = t1

    t0 += h

    vetQ.append(q0)
    vetT.append(t0)
    vetE.append(E)

plt.plot(vetT, vetQ, "o", markersize = 2, color = "red")
plt.plot(vetT, vetE, "o", markersize = 2, color = "green")
plt.show()
