from operator import attrgetter

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    def __repr__(self):
        return repr((self.name,self.population,self.area))

countries = [Country('Banglades', 1000, 100),
             Country('China', 2000, 200),
             Country('USA', 3000, 300)]

countries.append(Country('Russia', 5000, 600))
print(countries[0:1]) # [('Banglades', 1000, '100')]
print(countries) # [('Banglades', 1000, '100'), ('China', 2000, '200'), ('USA', 3000, '300'), ('Russia', 5000, '600')]

print('===========')
countries.sort(key=attrgetter('population'))
print(countries) # [('Banglades', 1000, 100), ('China', 2000, 200), ('USA', 3000, 300), ('Russia', 5000, 600)]

print('===========')
countries.sort(key=attrgetter('population'), reverse=True)
print(countries) # [('Russia', 5000, 600), ('USA', 3000, 300), ('China', 2000, 200), ('Banglades', 1000, 100)]

print('===========')
print(max(countries, key=attrgetter('population'))) # ('Russia', 5000, 600)
print(min(countries, key=attrgetter('population'))) # ('Banglades', 1000, 100)
print(max(countries, key=attrgetter('area'))) # ('Russia', 5000, 600)
print('===========')
print(countries) # [('Russia', 5000, 600), ('USA', 3000, 300), ('China', 2000, 200), ('Banglades', 1000, 100)]
