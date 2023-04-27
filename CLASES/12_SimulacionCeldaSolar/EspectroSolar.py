"""
Este archivo contiene:                
               * Radiacion solar I_AM15 
               * Flujo fotonico de la radiacion solar N_0
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
from scipy.interpolate import interp1d
import warnings

Kb = 8.6 * 10  ** (-5)           # eV/K
q = 1.602 * 10 ** (-19)          # cm
T = 300                                # T
eps_0 = (8.85 * 10 ** -12) / 10000     # C^2 / (N*cm^2)
c = (3 * 10 ** 8) * 10 ** 9            # nm/s
h = 4.135667731 * 10 ** (-15)          # ev*s
m0 = 9.10938291 * 10 ** -31            # Kg

#Download the solar spectrum
spectrum = pd.read_csv('CLASES/12_SimulacionCeldaSolar/12_data.csv', header=0, delimiter=';', decimal = ",")

#We choose the AM1.5G spectrum
lamb  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1107.0), 'Wvlgth nm'])  # nm
I_AM15  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1107.0), 'Global tilt  W*m-2*nm-1'])
photon_flux = I_AM15 * lamb / (q * 1240) / 10000   # 1 / (cm² * nm)

#Total radiation in the material
I_AM15_  = np.array(spectrum['Global tilt  W*m-2*nm-1'])
P_inc = (integrate.simps(I_AM15_) / 10000) * 1000   # mW / cm²     # P_inc = 100
