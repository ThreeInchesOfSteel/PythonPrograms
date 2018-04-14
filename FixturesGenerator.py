import random

teams = ["Aberdeen", "Celtic", "Dundee", "Hamilton", "Hearts", "Hibs", "Kilmarnock", "Motherwell" , "Partick Thistle", "Rangers" , "Ross County", "St Johnstone"]

smallteams = ["Aberdeen", "Celtic", "Hearts", "Rangers"]

fixtures = []

for a in range(0,len(teams)-1):
	for b in range(a+1,len(teams)):
		fixtures.append(teams[a] + " v " + teams[b])
		fixtures.append(teams[b] + " v " + teams[a])

randfixtures = random.sample(fixtures, len(fixtures))
print("\n".join(randfixtures))
