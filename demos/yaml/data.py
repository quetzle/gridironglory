import yaml

with open('teams.yaml') as t:
    tm = yaml.load(t)
def findteam(team):
    name = doc[team]['name']
    return name

q = raw_input('')
print findteam(q)
