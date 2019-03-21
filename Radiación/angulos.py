import matplotlib.pyplot as plt
import numpy as np

a=np.genfromtxt('angulos_campo.txt').T
campo=(np.mean(a,axis=1))

b=np.genfromtxt('angulos_campoinv.txt').T
campoinv=(np.mean(b,axis=1))

c=np.genfromtxt('angulos_sincampo.txt').T
campono=(np.mean(c,axis=1))

d=np.genfromtxt('angulos_plomo.txt').T
plomo=(np.mean(d,axis=1))

"""
angulos=np.arange(-90,100,10)
plt.scatter(angulos,campo,label=r'$\vec{B}>0$',color='r')
plt.plot(angulos,campo,color='r')
plt.scatter(angulos,campono,label=r'$\vec{B}=0$',color='b')
plt.plot(angulos,campono,color='b')
plt.scatter(angulos,campoinv,label=r'$\vec{B}<0$',color='orange')
plt.plot(angulos,campoinv,color='orange')
plt.legend()
plt.ylabel(r'$C$')
plt.xlabel(r'Ángulos $[\°]$')
plt.title('Conteos según el ángulo')
plt.savefig('mediciones.png')
plt.close()
"""
angulos=np.arange(-90,100,10)
angulos=angulos/360*2*np.pi
plt.scatter(campo*np.sin(angulos),campo*np.cos(angulos),label=r'$\vec{B}>0$',color='r')
plt.plot(campo*np.sin(angulos),campo*np.cos(angulos),color='r')
plt.scatter(campono*np.sin(angulos),campono*np.cos(angulos),label=r'$\vec{B}=0$',color='b')
plt.plot(campono*np.sin(angulos),campono*np.cos(angulos),color='b')
plt.scatter(campoinv*np.sin(angulos),campoinv*np.cos(angulos),label=r'$\vec{B}<0$',color='orange')
plt.plot(campoinv*np.sin(angulos),campoinv*np.cos(angulos),color='orange')
plt.legend()
plt.ylabel(r'Tasa de conteos $[\frac{conteos}{1s}]$')
plt.xlabel(r'Tasa de conteos $[\frac{conteos}{1s}]$')
plt.title('Conteos según el ángulo')
plt.savefig('mediciones.png')
plt.close()

