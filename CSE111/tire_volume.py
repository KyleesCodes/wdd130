import math
from datetime import datetime

print('> python tire_volume.py')

tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
print('')
volume = (math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000
print(f'The approximate volume is {volume:.2f} liters')

with open("volumes.txt", "at") as volumes_file:
    y_or_n = input('Do you want to buy these tires? Y or N: ')
    print('')
    if y_or_n.capitalize() == 'Y':
        phone = input('Thank you for your purchase! What is your phone number?: ')
        print('')
        print(f'The number you have entered is {phone}. Thank you for your purchase!')
        print(phone, file=volumes_file)
    elif y_or_n.capitalize() == 'N':
        print('Thank you for shopping with us! Have a great day.')
    else:
        print('Invalid answer. Please try again.')
    current_date_and_time = datetime.now()
    print('')
    print(f"{current_date_and_time:%Y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}", file=volumes_file)
