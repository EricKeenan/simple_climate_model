import numpy as np
import pandas as pd
import numba
from numba import jit

@jit(nopython=True)
def K_to_C(Kelvin):
	# Convert from Kelvin to Celsius 
	return Kelvin - 273.15

@jit(nopython=True)
def C_to_K(Celsius):
	# Convert from Celsius to Kelvin
	return Celsius + 273.15

#@jit(nopython=True)
def construct_timeseries(t0, tf):
	# Construct time series
	return np.linspace(t0, tf, num=365*24)



