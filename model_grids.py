import numpy as np
import utilities as util
import numba
from numba import jit

def get_grids(t0, tf): 
	# Build 1x1 degree across the entire planet

	# Build time vector
	time = util.construct_timeseries(t0, tf)

	# Build spatial grids
	lat_max = 90
	lat_min = -90
	lat_n = lat_max - lat_min + 1

	lon_max = 360
	lon_min = 0
	lon_n = lon_max - lon_min + 1
	
	X = np.linspace(lon_min, lon_max, num=lon_n)
	Y = np.linspace(lat_min, lat_max, num=lat_n)
	
	lon, lat = np.meshgrid(X, Y)

	# Retrun time vector and spatial grids
	return time, lon, lat

