import numpy as np
import matplotlib.pyplot as plt

## Import dos data (three columns: energy (eV), dos (states/eV), IDOS (states))
dos = np.genfromtxt('data/si.dos')

## Shift all energies by Fermi energy (Make sure the values for bands and DOS are consistent!)
Ef =  -9.305
dos[:,0] = dos[:,0] - Ef

fig = plt.figure(1, [10, 4], dpi=100)

plt.title('DOS')
plt.xlim(0,30)
#plt.ylim(0.0, 20.0)
#plt.xticks(np.linspace(-24.0, 20.0, num=12, dtype=float, endpoint=True))
#plt.yticks(np.linspace(-0, 20.0, num=11, dtype=float, endpoint=True))
plt.xlabel(r'Energy ($eV$)')
plt.ylabel(r'DOS ($st/eV$)')
#plt.vlines(0, 0, 20.0, linestyle='--', color='b')
#plt.hlines(8.0, -24, 20.0, linestyle='--', color='b')

plt.plot(dos[:,0], dos[:,1], color = 'k')
plt.plot(dos[:,0], dos[:,2], color = 'r')


#plt.savefig('edos.png', transparent=False, dpi=300, bbox_inches='tight')
plt.show()
