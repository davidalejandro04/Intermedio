import numpy as np
import matplotlib.pyplot as plt

datos=np.genfromtxt('distancia.txt')
distancia=datos[0,:]
distancia=1/distancia**2
conteos=datos[1:,:]
conteos=np.mean(conteos,axis=0)
m,b = np.polyfit(distancia, conteos, 1)

plt.scatter(distancia,conteos,label='Datos',color='gray')
x=np.linspace(0,0.13)
y=x*m+b
plt.plot(x,y,color='k',label=r'$%.1e*x+%.1e$'%(m,b),)
plt.legend()
plt.xlabel(r'1/$r^2$ $[1/cm^2]$')
plt.ylabel(r'Conteos $[\frac{1}{2.5s}]$')
plt.title('Intensidad en función de la distancia')
plt.errorbar(distancia,conteos,yerr=(distancia*m+b) - conteos,fmt='o')
plt.savefig('distancia.png')
plt.close()


datos=np.genfromtxt('distanciaplomo.txt')
distancia=datos[0,:]
distancia=1/distancia**2
conteos=datos[1:,:]
conteos=np.mean(conteos,axis=0)
m,b = np.polyfit(distancia, conteos, 1)

plt.scatter(distancia,conteos,label='Datos',color='gray')
x=np.linspace(0,0.13)
y=x*m+b
plt.plot(x,y,color='k',label=r'$%.1e*x+%.1e$'%(m,b),)
plt.legend()
plt.xlabel(r'1/$r^2$ $[1/cm^2]$')
plt.ylabel(r'Conteos $[\frac{1}{2.5s}]$')
plt.title('Intensidad en función de la distancia con plomo')
mse = (((distancia*m+b) - conteos)**2/abs(distancia*m+b)).mean(axis=0)
plt.errorbar(distancia,conteos,yerr=(distancia*m+b) - conteos,fmt='o')
plt.savefig('distanciaplomo.png')
plt.close()


datos=np.genfromtxt('distanciahoja.txt')
distancia=datos[0,:]
distancia=1/distancia**2
conteos=datos[1:,:]
conteos=np.mean(conteos,axis=0)
m,b = np.polyfit(distancia, conteos, 1)

plt.scatter(distancia,conteos,label='Datos',color='gray')
x=np.linspace(0,0.13)
y=x*m+b
plt.plot(x,y,color='k',label=r'$%.1e*x+%.1e$'%(m,b),)
plt.legend()
plt.xlabel(r'1/$r^2$ $[1/cm^2]$')
plt.ylabel(r'Conteos $[\frac{1}{2.5s}]$')
plt.title('Intensidad en función de la distancia con hoja')
mse = (((distancia*m+b) - conteos)**2/abs(distancia*m+b)).mean(axis=0)
plt.errorbar(distancia,conteos,yerr=(distancia*m+b) - conteos,fmt='o')
plt.savefig('distanciahoja.png')
plt.close()

