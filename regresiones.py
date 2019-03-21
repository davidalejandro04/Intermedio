import numpy as np
import matplotlib.pyplot as plt

B=np.array([-0.11,-0.18,-0.3,-0.5,-0.72,-0.9,-1.05,-1.2,-1.37,-1.6,-1.82,-2,-2.12,-2.33,-2.55,-2.7,-2.85])
I=np.array([0.16,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75,4])

def regresion(x0,y0,color0,nombre='Datos'):

	m,b = np.polyfit(x0, y0, 1)
	plt.scatter(x0,y0,color=color0,label=r'$%.3e*x+%.3e$ $(%s)$'%(m,b,nombre))
	x=np.linspace(x0[0],x0[-1])
	y=x*m+b
	plt.plot(x,y,color='k')
	plt.legend(loc=4)
	plt.errorbar(x0,y0,yerr=2*((x0*m+b) - y0),fmt='o',color=color0)
	return m,b



m,b=regresion(I,B,'k','Datos')
plt.xlabel(r' $I_{A}$ [A]')
plt.ylabel(r' $B$ [mT]')
plt.title(r'$B$ vs $I_A$')
plt.savefig('regresion1.png')
plt.close()
##Actividad2

#radio2cm
I=np.array([-2.09,-2.45,-2.73,-3.05,-3.3,-3.49,-3.69,-3.91])
V=np.array([100,125,150,175,200,225,250,275])

def getCampoB(I0,m,b):
	campoB=I0*m+b	
	return campoB*10**(-3)
r=0.02
B=getCampoB(I,m,b)
em=-2*V/(B*r)**2

plt.hist(em,bins=3,color='gray')
s=np.std(em)
mu=np.mean(em)
plt.title(r'Histograma de $e/m$ $\sigma$=$%.2e$, $\mu$=$%.2e$'%(s,mu))
plt.xlabel(r'$e/m$')
plt.savefig('mismoradio.png')

plt.close()

#varios rarios


regresion(-(B**2*r**2)/2.0,V,'gray','2 [cm]')

V3=np.array([350,325,300,275,250,225,200,175,150,125])
I3=np.array([-2.8,-2.67,-2.55,-2.43,-2.3,-2.18,-2.04,-1.88,-1.7,-1.58])

r=0.03
B=getCampoB(I3,m,b)
em=-2*V3/(B*r)**2
s=np.std(em)
mu=np.mean(em)
print(s)
print(mu)

regresion(-(B**2*r**2)/2.0,V3,'g','3 [cm]')



V4=np.array([150,175,200,225,250,275,300,325,350])
I4=np.array([-1,-1.1,-1.2,-1.26,-1.35,-1.42,-1.49,-1.57,-1.62])

r=0.04
B=getCampoB(I4,m,b)
em=-2*V4/(B*r)**2
s=np.std(em)
mu=np.mean(em)
print(s)
print(mu)

regresion(-(B**2*r**2)/2.0,V4,'b','4 [cm]')


V5=np.array([350,325,300,275,250,225,200,175,150])
I5=np.array([-2.01,-1.97,-1.9,-1.77,-1.67,-1.58,-1.47,-1.35,-1.19])

r=0.04
B=getCampoB(I5,m,b)
em=-2*V5/(B*r)**2
s=np.std(em)
mu=np.mean(em)
print(s)
print(mu)

regresion(-(B**2*r**2)/2.0,V5,'r','5 [cm]')
plt.title(r'Voltaje $V$ en funcion de $B^2$')
plt.ylabel(r'$V$ $[V]$')
plt.xlabel(r'$\frac{1}{2}(B \cdot r)^2$ $[T\cdot m]^2$')
plt.xlim([0.5*max(-(B**2*r**2)/2.0), 1.2*min(-(B**2*r**2)/2.0)])
plt.savefig('regresiones.png')
plt.show()
