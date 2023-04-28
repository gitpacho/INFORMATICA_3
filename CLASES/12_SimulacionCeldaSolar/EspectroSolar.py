"""
Este archivo contiene:                
               * Radiacion solar I_AM15 
               * Flujo fotonico de la radiacion solar N_0
"""

from constantesFisicas import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as integrate
from scipy.interpolate import interp1d
import warnings


#Download the solar spectrum
spectrum = pd.read_csv('CLASES/12_SimulacionCeldaSolar/12_data.csv', header=0, delimiter=';', decimal = ",")

#We choose the AM1.5G spectrum
lamb  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1107.0), 'Wvlgth nm'])  # nm
I_AM15  = np.array(spectrum.loc[(spectrum['Wvlgth nm'] <= 1107.0), 'Global tilt  W*m-2*nm-1'])
photon_flux = I_AM15 * lamb / (q * 1240) / 10000   # 1 / (cm² * nm)   #esta es la variable de interes

#Total radiation in the material
I_AM15_  = np.array(spectrum['Global tilt  W*m-2*nm-1'])
P_inc = (integrate.simps(I_AM15_) / 10000) * 1000   # mW / cm²     # P_inc = 100   #Esta es el flujo fotonico proveniente del sol
