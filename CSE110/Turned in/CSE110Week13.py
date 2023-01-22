import math
temperature = float(input('What is the temperature?: '))
f_or_c = input('Fahrenheit or Celsius? (F/C): ')

if f_or_c == 'F' or 'C':
    for index in range(5,61,5):
        if f_or_c.capitalize() == 'F':
            wind_chill_f = 35.47 + (0.621 * temperature) - (35.75 * (index ** 0.16)) + (0.4275 * temperature * (index ** 0.16))
            print(f'At temperature {temperature:.2f}F, and a wind speed of {index} mph, the wind chill is: {wind_chill_f:.2f}F')
        elif f_or_c.capitalize() == 'C':
            c_to_f = (temperature * 1.8) + 32
            wind_chill_c = 35.47 + (0.621 * c_to_f) - (35.75 * (index ** 0.16)) + (0.4275 * c_to_f * (index ** 0.16))
            print(f'At the temperature {c_to_f:.2f}F, and a wind speed of {index} mph, the wind chills is: {wind_chill_c:.2f}F')

