"""
Este archivo es el archivo principal que integra todos los archivos

Aqui se encuentra  la funcion simulacion()
la cual integra todas las funciones para operarlas
esta funcion recibe un voltaje
y retorna la corriente producida por la celda (j_cell)
"""

from PropiedadesMaterialN import *
from PropiedadesMaterialP import *
from funcionesDeApoyo import *


def simulation(voltage):        #this function return j_cell of the solar cell
    # Built-in potential --------------------------------------------------------------
    V_bi = Vbi(Eg_n, Eg_p, chi_n, chi_p, N_d, N_a, Nc_n, Nc_p, Nv_n, Nv_p, ni_n, ni_p)

    # Depletion region ----------------------------------------------------------------
    x_n = region(N_a, N_d, eps_n, eps_p, N_d, N_a, V_bi, voltage )
    x_p = region(N_d, N_a, eps_n, eps_p, N_d, N_a, V_bi, voltage )

    if x_n > w_n:  # Condition in case the depletion region exceeds the width of the material
        x_n = w_n
        x_p = w_n * (N_d / N_a)

    # Photocurrent --------------------------------------------------------------------
    dj_p    =  dJp(s_p, L_p, D_p, w_n, x_n, alpha_1, Ref, Trans)
    dj_n    =  dJn(s_n, L_n, D_n, w_p, x_p, alpha_2, w_n, alpha_1, Ref, Trans)  
    dj_scr  =  dJscr(x_n, x_p, w_n, alpha_1, alpha_2 , Ref, Trans)
    j_ph    =  Jph(dj_n, dj_p, dj_scr)
    # Saturation current density J0 ---------------------------------------------------
    j0_p    =  J0pn(D_p, p_0, L_p, s_p, w_n, x_n)
    j0_n    =  J0pn(D_n, n_0, L_n, s_n, w_p, x_p)
    j_0     =  J0(j0_n, j0_p)
    # Saturation current density J00 --------------------------------------------------
    j_00    =  J00(x_n, x_p, ni_n, ni_p, L_p, L_n, D_p, D_n)
    # Dark current density ------------------------------------------------------------
    j_dark  =  Jdark(j_0, j_00, voltage)
    # Cell current density ------------------------------------------------------------
    j_cell  =  j_ph - j_dark
    return j_cell

# ========================Mi primera celda simulada========================
voltage = 0.5  #Voltios
j_celda = simulation(voltage)   #densidad de corriente que produce celda
pot_celda = voltage * j_celda   #densidad de potencia electrica producida por la celda

print("voltaje: ", voltage)
print("densidad de corriente: ", j_celda)
print("densidad de potencia: ", pot_celda)


# =======================Simulacion variando el voltaje====================

