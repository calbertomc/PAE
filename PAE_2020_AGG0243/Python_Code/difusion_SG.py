#!/usr/bin/env python3

# MODULOS DO PYTHON

import numpy as np
import math as mh #scipy.special as sps
import scipy.special as sps
import multiprocessing as mp
import matplotlib.pyplot as plt
import matplotlib.colorbar as cbar

from matplotlib.patches import Rectangle

# ------------------------- FUNCOES -------------------------
def calc_T(T0,z,a,t): # CALCULA TEMPERATURA AO LONGO DO TEMPO PARA UMA PROFUNDIDADE
    T = np.zeros_like(t)
    
    for i in range(len(T)):
        T[i] = T0*(sps.erf(z/(2*a*mh.sqrt(t[i])))) # calcula a evolucao termica da camada
    
    return T

def zipa(T0,z,a,t): # ZIPA OS DADOS PARA USAR PARALELISMO 
    data = [(T0,z[i],a,t) for i in range(len(z))]

    return data

# ----------------- PROGRAMA PRINCIPAL ---------------------

T0 = 1200 # temperatura inicial em ºC
a = mh.sqrt(0.031) # coeficiente de difusidade termica em (km²/milenio)

t = np.arange(0,500) # tempo decorrido 500 milenios (500000 anos)

z = np.arange(100,1000,100) # vetor de profundidades da camada em metros
z = z/1000 # converte de metro pra quilometro

Tf = np.zeros((len(t),len(z))) # vetor do mesmo tamanho que t para guardar a temperatura ao longo do tempo

data = zipa(T0,z,a,t) # zipar dados a serem calculados

pool = mp.Pool() # usa todos os nucleos disponiveis
res = pool.starmap(calc_T,data) # paralelismo do calculo de temperaturas
pool.close()
pool.join()

for i in range(len(z)): #organiza a saida do paralelismo em matriz
    Tf[:,i] = res[i]

# ------ PLOTA CURVAS DE DECAIMENTO DA TEMPERATURA ----------------------
for i in range(len(z)):
    plt.plot(t,Tf[:,i],label=str(z[i])+" km")
plt.legend()
plt.xlabel("Tempo (milenios)")
plt.ylabel("Temperatura (°C)")
plt.show()

# ------ ANIMACAO SECAO 1D EM PROFUNDIDADE -------------------------------

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

normal = plt.Normalize()
jet = plt.cm.get_cmap('jet')
colors = jet(normal(Tf)) # mapa de cores normalizado para Tf

for j in range(len(t)-396):
    for i in range(len(z)):
        rect = Rectangle((0,z[i]-0.1),100,0.1,facecolor=colors[j][i][:], edgecolor=colors[j][i][:]) #coordenadas canto superior, esquerdo, largura, espessura
        ax.add_patch(rect) #adiciona retangulo a figura
    
    plt.draw()
    plt.pause(.0001)
    if j == 0:
        ax.set_ylabel([0,0.9])
        ax.set_xlim([0,100])
        cax, _ = cbar.make_axes(ax) 
        cb2 = cbar.ColorbarBase(cax, cmap=jet,norm=normal)
        cb2.set_label("Temperatura °C") 
        ax.invert_yaxis()
    
    
    ax.set_xlabel("Distancia (km)")
    ax.set_ylabel("Profundidade (km)")
    ax.set_title(str(t[j])+" milenios")