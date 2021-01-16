import matplotlib.pyplot as plt


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



USA = countries['United States']
diffUSA = []
vpd = []
for i,_ in enumerate(USA):
    if i > 0:
        lI = i-1
        nbVaccines = _['daily_vaccinations_per_million']
        lastVaccines = USA[lI]['daily_vaccinations_per_million']
        if '' not in [nbVaccines,lastVaccines]:
            vpd.append(int(lastVaccines))
            dif = (int(nbVaccines)-int(lastVaccines))/int(nbVaccines)*1000
            diffUSA.append(dif)

USA = countries['Belgium']
diffBE = []
vpd = []
for i,_ in enumerate(USA):
    if i > 0:
        lI = i-1
        nbVaccines = _['daily_vaccinations_per_million']
        lastVaccines = USA[lI]['daily_vaccinations_per_million']
        if '' not in [nbVaccines,lastVaccines]:
            vpd.append(int(lastVaccines))
            dif = (int(nbVaccines)-int(lastVaccines))/int(nbVaccines)*1000
            diffBE.append(dif)


plt.plot(diffUSA)
plt.plot(diffBE)
plt.ylabel('USA vaccine p million')
plt.show()