from __future__ import annotations
from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

conversion = {"M": 1000000,
              "B": 1000000000}

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def damage_update(damages):
    res = []
    for record in damages:
        if record == "Damages not recorded":
            res.append(record)
        else:
            res.append(float(record[:-1]) * conversion[record[-1]])
    return res

print(damages)
print("\n")
damages_updated = damage_update(damages)


# write your construct hurricane dictionary function here:
def hurricanes_by_name(names, months, years, winds, areas, damages, deaths):
    res = {}
    for i, name in enumerate(names):
        dict = {'Name': name,
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Winds': winds[i],
                'Areas Affected': areas[i],
                'Damage': damages[i],
                'Deaths': deaths[i]
                }
        res[name] = dict
    return res

# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(names, months, years, winds, areas, damages, deaths):
    res = {}
    for i, year in enumerate(years):
        dict = {'Name': names[i],
                'Month': months[i],
                'Year': years[i],
                'Max Sustained Winds': winds[i],
                'Areas Affected': areas[i],
                'Damage': damages[i],
                'Deaths': deaths[i]
                }
        try:
            res[year].append(dict)
        except KeyError:
            res[year] = [dict]
    return res


hurricanes_name = hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)
hurricanes_year = hurricanes_by_year(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)

# print(hurricanes_year[1932])

# write your count affected areas function here:
def hurricane_count_by_area(areas):
    res = defaultdict(int)
    for hurricane in areas:
        for area in hurricane:
            res[area] += 1
    return res

hurricane_area_count = hurricane_count_by_area(areas_affected)

# write your find most affected area function here:
def area_most_affected(a_count):
    area = max(a_count, key=a_count.get)
    return area, a_count[area]

area, count = area_most_affected(hurricane_area_count)
print(f"The most affected area was {area} with {count} hurricanes.")

# write your greatest number of deaths function here:

def deadliest(canes):
    max_mortality = 0
    max_mort_cane = 'None'
    # print(canes)
    for key, value in canes.items():
        if value['Deaths'] > max_mortality:
            max_mortality = value['Deaths']
            max_mort_cane = key
    print(canes[max_mort_cane])

    return max_mort_cane, max_mortality

print(deadliest(hurricanes_name))


# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mort_scale(canes):
    res = defaultdict(list)
    for name, value in canes.items():
        for scale, deaths in reversed(mortality_scale.items()):
            if value['Deaths'] > deaths:
                res[scale].append(name)
                break
    return res

hurricanes_by_mortality = mort_scale(hurricanes_name)


# write your greatest damage function here:

def greatest_damage(canes):
    most_damage = 0
    max_damage_cane = 'None'
    for key, value in canes.items():
        if isinstance(value['Damage'], float):
            if value['Damage'] > most_damage:
                most_damage = value['Damage']
                max_damage_cane = key

    return max_damage_cane, most_damage

print(greatest_damage(hurricanes_name))

# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def dam_scale(canes):
    res = defaultdict(list)
    for name, value in canes.items():
        if isinstance(value['Damage'], float):
            for scale, damage in reversed(damage_scale.items()):
                if value['Damage'] > damage:
                    res[scale].append(name)
                    break
        else:
            res[0].append(name)
    return res

hurricanes_by_damage = dam_scale(hurricanes_name)

print(hurricanes_by_damage)