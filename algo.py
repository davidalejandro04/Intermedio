
import numpy as np
import matplotlib.pyplot as plt


Bm=np.array([1.2,1.3,1.37,1.3,1.2])*10**(-3)
x=np.array([14.5,9.8,0,-9.8,-14.5])*10**(-2)

I=-2.0
N=154
mu=4.0*np.pi*10**(-7)
z=np.linspace(-15,15,100)*10**-2
a=0.2
d=2.0*a
B=mu*N*I/(2*a) *( 1/((z/a + d/(2*a))**2+1)**(3/2) + 1/((z/a-d/(2*a))**2 +1)**(3/2))+2*Bm[0]-0.000064


axes = plt.gca()
plt.scatter(x*10**2,Bm*10**3,color='k',label='Observado')
plt.plot(z*10**2,B*10**3,color='gray',label='Calculado')
plt.legend()
plt.title(r'$B(x)$ para corriente $I_{A}$=-2.0 [A]')
plt.xlabel(r'$x$ [cm]')
plt.ylabel(r'$B$ [mT]')
axes.set_ylim([0.00117*10**3,0.00144*10**3])
plt.savefig('campoB.png')
plt.show()
