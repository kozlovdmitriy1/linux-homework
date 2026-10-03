#!/usr/bin/python3
import sys
temperature_c = float(sys.argv[1])
temperature_f = temperature_c*1.8+32
temperature_k = temperature_c + 273.15
print(f'{temperature_f:.1f}°F, {temperature_k:.2f} K')
