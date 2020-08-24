import math
import numpy as np
import stefan_boltzmann as sb
import numba
from numba import jit

# Constants
S = 1361 # Solar constant (W/m^2)
albedo = 0.3 # Global average albedo
atm_eps = 0.77 # Atmospheric emissivity 
hours_in_day = 24 # 24 hours in a day
days_in_year = 365 # 365 days in a year
earth_tilt = 23.5 * math.pi / 180 # Earth is tilted 23.5 degrees from the plane of its orbit around the sun
time_indices = 1000

def get_iswr(time, lon, lat): 
	# Calculate incoming shortwave radiation at the surface

	# Initialize arrays
	# iswr = np.zeros([lon.shape[0], lon.shape[1], len(time)])
	iswr = np.zeros([lon.shape[0], lon.shape[1], time_indices])


	# Geographic conversions 
	lat_radians = lat * math.pi / 180
	lon_radians = lon * math.pi / 180

	# Calculate net short wave radiation at the surface. (Still need to account for seasons!)
	# for time_index in range(0, len(time)):
	for time_index in range(0, time_indices):
		hour = np.fmod(time_index, 24) # 0 corresponds to midnight, 12 is noon

		# Time of day factor (tdf), accounts for diurnal solar radiation cycle
		tdf = -np.cos(hour * math.pi / 12 + lon_radians) 
		tdf[tdf < 0] = 0

		# Time of year factor (tyr), accounts for seasons
		sub_year = time[time_index] - int(time[time_index])
		# sub_year = time[time_index]
		tyr = np.cos(sub_year * 2 * math.pi)

		# Calculate surface energy balance
		iswr[:,:,time_index] = S * np.cos(lat_radians + earth_tilt * tyr) * (1 - albedo) * tdf
		iswr[iswr[:,:,time_index] < 0] = 0


	return iswr

@jit(nopython=True)
def get_temperature(iswr):
	# Calculate temperature from incoming shortwave radiation
	flux = iswr / ( 1 - atm_eps / 2)
	return sb.flux_to_temperature(flux)







