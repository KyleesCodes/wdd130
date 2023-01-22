import csv
lowest = 1000
lowestYear = 0
lowestCountry = ''
highest = 1
highestYear = 0
highestCountry = ''
average = 0
yearsLen = 0
lowestChoice = 1000
lowestChoiceCountry = ''
highestChoice = 1
highestChoiceCountry = ''
yearLow = 2023
yearHigh = 0

user_year = int(input('Enter the year of interest: '))

with open("life-expectancy.csv") as life_expectancy_file:
    csv_reader = csv.reader(life_expectancy_file, delimiter=',')
    next(csv_reader)
    for line in life_expectancy_file:
        line = line.strip()
        parts = line.split(',')
        name = parts[0]
        year = int(parts[2])
        life = float(parts[3])
        if lowest > life:
            lowest = life
            lowestYear = year
            lowestCountry = name
        if highest < life:
            highest = life
            highestYear = year
            highestCountry = name
        if user_year == year:
            average = average + life
            yearsLen = yearsLen + 1
            if lowestChoice > life:
                lowestChoice = life
                lowestChoiceCountry = name
            if highestChoice < life:
                highestChoice = life
                highestChoiceCountry = name
        if yearLow > year:
            yearLow = year
        if yearHigh < year:
            yearHigh = year

if user_year >= yearLow and user_year <= yearHigh:
    average = average / yearsLen

    print('')
    print(f'The overall smallest life expectancy is: {lowest} from {lowestCountry} in {lowestYear}')
    print(f'The overall largest life expectancy is: {highest} from {highestCountry} in {highestYear}')
    print('')
    print(f'For the year {user_year}:')
    print(f'The average life expectancy across all countries was: {average:.2f}')
    print(f'The smallest life expectancy was: {lowestChoice} in {lowestChoiceCountry}')
    print(f'The largest life expectancy was: {highestChoice} in {highestChoiceCountry}')
    print('')

else:
    print(f'Sorry, but year {user_year} is not in our data. Please try again with a year between years {yearLow} and {yearHigh}. Thank you!')