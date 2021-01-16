data = open("population_by_country_2020.csv", "r")
lines = data.readlines()
lines = [line.strip() for line in lines]


f = open("populations.txt", "a")
for line in lines:
    data = line.split(',')
    name = data[0]
    pop2020 = data[1]
    f.write(str(name)+','+str(pop2020)+'\n')
f.close()
