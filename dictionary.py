heroes = ["srk", "salman", "amir"]

hero_bunch = {
  "srk" : 20,
  "salman" : 40,
  "amir" : 50
}

for hero_label in hero_bunch:
  print(hero_label)

for hero_label in hero_bunch.values():
  print(hero_label)

hero_bunch["akshay"] = 60
print(hero_bunch)

hero_bunch["salman"] = 80
print(hero_bunch)

for hero_label,hero_val in hero_bunch.items():
  print(hero_label+" " + str(hero_val))

print(hero_bunch["srk"])

total = hero_bunch["srk"] + hero_bunch["salman"]
print(total)

#output
#srk
#salman
#amir
#20
#40
#50
#{'srk': 20, 'salman': 40, 'amir': 50, 'akshay': 60}
#{'srk': 20, 'salman': 80, 'amir': 50, 'akshay': 60}
#srk 20
#salman 80
#amir 50
#akshay 60
#100
