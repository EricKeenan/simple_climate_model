import numpy as np
import numba
from numba import jit

# Stefan-Boltzmann Constant
sigma = 5.67e-8

@jit(nopython=True)
def temperature_to_flux(temperature):
	return sigma * np.power(temperature, 4)

@jit(nopython=True)
def flux_to_temperature(flux):
	return np.power(flux / sigma, 0.25)
