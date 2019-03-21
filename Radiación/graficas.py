import numpy as np
import matplotlib.pyplot as plt

a=np.genfromtxt('manto10s.txt')

a2=a[:,1]

abar=np.mean(a2)
adesv=np.sqrt(abar)
print(abar)
print(adesv)

print(len(a2))
a2=a2[a2<=abar+adesv]
print(len(a2))
a3=a2[a2>=abar-adesv]
print(len(a3))

a2=a[:,1]

print(len(a2))
a2=a2[a2<=abar+2*adesv]
print(len(a2))
a3=a2[a2>=abar-2*adesv]
print(len(a3))


plt.hist(a[:,1],bins=20, alpha=0.5)
plt.title('Histograma de conteos')
plt.ylabel('Frecuencia')
plt.xlabel(r'$C$')
plt.savefig('Histograma.png')


