import unittest
import stefan_boltzmann as sb

def main():
	test_stefan_boltzmann()
	if __name__ != "__main__":
		print("Passed all tests! ")

def test_stefan_boltzmann(): 
	assert sb.flux_to_temperature(1) >= 0, "flux_to_temperature() retuned a negative temperature, but Kelvin are always postive."

if __name__ == "__main__":
	main()
	print("Passed all tests! ")