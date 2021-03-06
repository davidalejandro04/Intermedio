import numpy as np
import matplotlib.pyplot as plt

datos=np.genfromtxt('varioshojas.txt').T
hojas=datos[0,:]*0.05
numero=datos[1,:]
print(numero)
plt.scatter(hojas,numero)
plt.errorbar(hojas,numero,xerr=0.03,yerr=20, fmt='o',color='k')
plt.scatter(hojas,numero,color='gray')
plt.xlabel(r'Grosor $[mm]$')
plt.ylabel(r'Conteos $[conteo/1s]$')
plt.title('Intensidad vs grosor de hojas')
plt.grid(True)
plt.savefig('varioshojas.png')
plt.close()


datos=np.genfromtxt('varioscartones.txt').T
hojas=datos[0,:]*2
numero=datos[1,:]
print(numero)
plt.scatter(hojas,numero)
plt.errorbar(hojas,numero,xerr=0.08,yerr=20, fmt='o',color='k')
plt.scatter(hojas,numero,color='gray')
plt.xlabel(r'Grosor $[mm]$')
plt.ylabel(r'Conteos $[conteo/1s]$')
plt.title('Intensidad vs grosor de cartones')
plt.grid(True)
plt.savefig('varioscartones.png')
plt.close()


datos=np.genfromtxt('variosplomo.txt').T
hojas=datos[0,:]*0.4
numero=datos[1,:]
print(numero)
plt.scatter(hojas,numero)
plt.errorbar(hojas,numero,xerr=0.08,yerr=1, fmt='o',color='k')
plt.scatter(hojas,numero,color='gray')
plt.xlabel(r'Grosor $[mm]$')
plt.ylabel(r'Conteos $[conteo/1s]$')
plt.title('Intensidad vs grosor de plomo')
plt.grid(True)
plt.savefig('variosplomo.png')
plt.close()


datos=np.genfromtxt('variosaluminio.txt').T
hojas=datos[0,:]*0.4
numero=datos[1,:]
print(numero)
plt.scatter(hojas,numero)
plt.errorbar(hojas,numero,xerr=0.005,yerr=5, fmt='o',color='k')
plt.scatter(hojas,numero,color='gray')
plt.xlabel(r'Grosor $[mm]$')
plt.ylabel(r'Conteos $[conteo/1s]$')
plt.grid(True)
plt.title('Intensidad vs grosor de aluminio')
plt.savefig('variosaluminio.png')


