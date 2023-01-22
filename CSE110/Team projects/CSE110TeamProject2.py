import math


print ('Welcome to the velocity calculator. Please enter the following:')

mass = float(input('Mass (in kg): '))
gravity_acceleration = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
fluid_density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross_sectional_area = float(input('Cross sectional area (in m^2): '))
drag_constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

inner_value = 1/2 * fluid_density * cross_sectional_area * drag_constant

velocity = math.sqrt (mass * gravity_acceleration /  (1/2 * fluid_density * cross_sectional_area * drag_constant)) * ( 1 - math.exp ( ( - math.sqrt (mass * gravity_acceleration * ( 1/2 * fluid_density * cross_sectional_area * drag_constant ) ) / mass ) * time ) )


print (f'\nThe inner value of c is: {inner_value:.3f}')
print (f'\nThe velocity after {time} seconds is: {velocity:.3f} m/s')

