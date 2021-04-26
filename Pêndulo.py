import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow, figure
import math



T = 30 # tempo final
h = 0.05 # passo
l = 3.0 # comprimento da haste
g = 9.8 # valor da gravidade
alfa = 1 # coeficiente de amortecimento
x0 = 0
w0 = 0 # velocidade angular inicial
t0 = 0 #tempo inicial
theta_graus  = 90 # angulo inicial
theta0 = theta_graus*math.pi/180 # angulo inicial em radianos

vetX = [x0]
vetW = [w0]
vetT = [t0]

def make_fig():
    x = l * (math.cos(theta0 - (math.pi/2)))
    y = l * (math.sin(theta0 - (math.pi/2)))
    plt.plot((-0.5,0.5),(0,0),color='black') # plotagem do teto
    plt.plot((0,x),(0,y))#plotagem da haste
    plt.plot(0, 0, marker='o', markersize=3, color='black') # ponto de apoio da haste
    plt.plot(x, y, marker='o', markersize=10, color='red') #plotagem do circulo
    plt.axis((-3.0, 3.0, -l - 1, 0.25))
    plt.grid(True)


while(t0 <= T):
    thetaProximo = theta0 + (h * w0)
    #wProximo = - ((g/l)math.sin(x0) - (alfa/l)w0)
    wProximo = w0+(h*(-(g/l) * np.sin(theta0) - ((alfa/l)) * w0))
    t0 += h

    w0 = wProximo
    theta0 = thetaProximo

    vetX.append(theta0)
    vetW.append(w0)
    vetT.append(t0)

    drawnow(make_fig)
'''plt.plot(vetT, vetX,color = "green")
plt.plot(vetT, vetW,color = "red")
plt.show()
'''
