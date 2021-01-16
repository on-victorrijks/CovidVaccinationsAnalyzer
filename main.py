import matplotlib.pyplot as plt
from math import *

# load populations
data = open("populations.txt", "r")
lines = data.readlines()
lines = [line.strip() for line in lines]
populations = {}
for line in lines:
    data = line.split(',')
    name = data[0]
    val = data[1]
    populations[name] = val


data = open("data.txt", "r")
lines = data.readlines()
lines = [line.strip() for line in lines]
names = lines[0].split(',')

def generateContainer():
    global names
    temp = {}
    for name in names:
        temp[name] = None
    return temp

c_data = []
for line in lines:
    temp = generateContainer()
    tempLine = line.split(',')
    for i,key in enumerate(temp.keys()):
        temp[key] = tempLine[i]
    c_data.append(temp)

countries = {}
for line in c_data:
    country = line['location']
    if country not in countries:
        countries[country] = []
    countries[country].append(line)



paths = {
    'date':{},
    'totalVaccinations':{},
    'dailyVaccinationsPercentage':{},
}


for countryName in countries:

    country = countries[countryName]
    paths['date'][countryName],paths['totalVaccinations'][countryName],paths['dailyVaccinationsPercentage'][countryName] = [],[],[]

    for dataEntryIndex,dateEntry in enumerate(country):
        date = dateEntry['date']
        try:
            totalVaccinations = int(dateEntry['total_vaccinations'])
        except:
            totalVaccinations = 0
        try:
            dailyVaccinationsPercentage = int(dateEntry['daily_vaccinations_per_million'])/1000000
        except:
            dailyVaccinationsPercentage = 0
        
        paths['date'][countryName].append(date)
        paths['totalVaccinations'][countryName].append(totalVaccinations)
        paths['dailyVaccinationsPercentage'][countryName].append(dailyVaccinationsPercentage)


countriesNames = []
print('Enter the index of the country you want to plot')
for i,countryName in enumerate(countries):
    countriesNames.append(countryName)
    print('{}: {}'.format(i,countryName))

selectedCountryIndex = int(input('index: '))
selectedCountryName = countriesNames[selectedCountryIndex]


pop = int(populations[selectedCountryName])
totalVaccinations = plt.plot(paths['date'][selectedCountryName], paths['totalVaccinations'][selectedCountryName])
dailyVaccinationsPercentage = plt.plot(paths['date'][selectedCountryName], [k*pop for k in paths['dailyVaccinationsPercentage'][selectedCountryName]])
plt.show()
