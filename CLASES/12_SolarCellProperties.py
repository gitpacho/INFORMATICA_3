import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
#from scipy.interpolate import interp1d
#import warnings
#warnings.filterwarnings('ignore')

Kb = 8.6 * 10  ** (-5)                 # eV/K            cte boltzman
q = 1.602 * 10 ** (-19)                # cm              carga electrica
T = 300                                # kelvin          temperatura de la celda
eps_0 = (8.85 * 10 ** -12) / 10000     # C^2 / (N*cm^2)  permitividad en el vacio
c = (3 * 10 ** 8) * 10 ** 9            # nm/s            velocidad de la luz
h = 4.135667731 * 10 ** (-15)          # ev*s            cte planck
m0 = 9.10938291 * 10 ** -31            # Kg              masa del electron

#Get the solar spectrum
spectrum = pd.read_csv('CLASES/espectro.csv', header=0, delimiter=';', decimal = ",")

#We choose the AM1.5G spectrum
lamb  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1937.0), 'Wvlgth nm'])
I_AM15  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1937.0), 'Global tilt  W*m-2*nm-1'])
photon_flux = I_AM15 * lamb / (q * 1240) / 10000   # 1 / (cm² * nm)

#Total radiation in the material
I_AM15_  = np.array(spectrum['Global tilt  W*m-2*nm-1'])
P_inc = (integrate.simps(I_AM15_) / 10000) * 1000   # mW / cm²     # P_inc = 100  #energia del sol

