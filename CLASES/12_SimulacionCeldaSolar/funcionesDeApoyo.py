"""
Este archivo contiene las funciones necesarias para realizar la simulacion
las funciones están descritas en SimulationSolarCell.pdf
"""

from constantesFisicas import *
from EspectroSolar import *


# Built-in potential  -------------------------------------------------------------------------
def Vbi(Egn, Egp, chin, chip, Nd, Na, Ncn, Ncp, Nvn, Nvp, nin, nip):  # Built-in Potential
    delta_gap = abs(Egn - Egp)
    delta_ec  = abs(chip - chin)
    delta_ev  = delta_gap - delta_ec
    A = (delta_ec - delta_ev) / 2
    B = Kb * T * np.log(Nd * Na / (nin * nip))
    C = 0.5 * Kb * T * np.log(Ncp * Nvn / (Ncn * Nvp))
    return A + B + C

# Depletion region xn y xp --------------------------------------------------------------------
def region(a, b, epsn, epsp, Nd, Na, Vbi, V):
    A = 2 * epsp * epsn * eps_0 * a * (Vbi - V) * 100
    B = q * b * (epsn * Nd + epsp * Na)
    return (A / B) ** 0.5

# Photocurrent densities ----------------------------------------------------------------------
def dJp(sp, Lp, Dp, wn, xn, alpha1, Ref, Trans):
    cte1 = sp * Lp / Dp
    cte2 = wn - xn
    angulo = (wn - xn) / Lp
    A = q * photon_flux * (1 - Ref) * Trans * alpha1 * Lp
    B = ((alpha1 ** 2) * (Lp ** 2) ) - 1
    C = cte1 + (alpha1 * Lp)
    D = np.exp(- (alpha1 * cte2))
    E = ( cte1 * np.cosh(angulo) ) + np.sinh(angulo)
    F = ( cte1 * np.sinh(angulo) ) + np.cosh(angulo)
    G = alpha1 * Lp * np.exp( - alpha1 * cte2)
    return (A / B) *  ( ((C - D * E) / F) - G)  

def dJn(sn, Ln, Dn, wp, xp, alpha2, wn, alpha1, Ref, Trans):
    cte1 = sn * Ln / Dn
    cte2 = wp - xp
    angulo = (wp - xp) / Ln    
    A = q * photon_flux * (1 - Ref) * Trans * alpha2 * Ln
    B = np.exp(-(alpha1 * wn + alpha2 * xp))
    C = ((alpha2 ** 2) * (Ln ** 2)) - 1
    D = alpha2 * Ln
    E = cte1 * (np.cosh(angulo) - np.exp( - alpha2 * cte2 ) )
    F = np.sinh(angulo) 
    G = alpha2 * Ln * np.exp(- alpha2 * cte2)
    H = cte1 * np.sinh(angulo)
    I = np.cosh(angulo)
    return (A * B / C) * (D - ( (E + F + G ) / (H + I) ))

def dJscr(xn, xp, wn, alpha1, alpha2 , Ref, Trans):
    A = q * photon_flux * (1 - Ref) * Trans * np.exp( - alpha1 * (wn - xn))
    B = 1 - np.exp( - alpha1 * xn)
    C = np.exp( - alpha1 * xn) * (1 - np.exp(- alpha2 * xp))
    return A * (B + C)

def Jph(dj_n, dj_p, dj_scr):
  return integrate.simps(dj_p + dj_n + dj_scr)


# Saturation current density J0, J0p y J0n ----------------------------------------------------
def J0pn(D, pn0, L, s, w, x): 
    A = q * D * pn0 / L
    B = s * L / D
    ang = (w - x) / L
    return A * (B * np.cosh(ang) + np.sinh(ang) ) / (B * np.sinh(ang) + np.cosh(ang))
def J0(j0_n, j0_p):
  return j0_n + j0_p

# Saturation current density J00 --------------------------------------------------------------
def J00(xn, xp, nin, nip, Lp, Ln, Dp, Dn):   
    taop = (Lp ** 2) / Dp
    taon = (Ln ** 2) / Dn
    return q * ( (xn * nin / taop) + (xp * nip / taon))

# Dark current density ------------------------------------------------------------------------
def Jdark(j_0, j_00, v):
    return (j_0 * (np.exp(v / (Kb * T)) - 1)) + (j_00 * (np.exp(v / (2 * Kb * T)) - 1))