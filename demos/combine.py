import random

def length(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

print 'First names:', length('names.txt') + 1
print 'Last names:', length('last.txt') + 1
print 'Cities:', length('cities.txt') + 1
print 'Team names:', length('teams.txt') + 1
print 'Positions:', length('positions.txt') + 1

go = raw_input('')
while go == '':
  n = random.randint(0,length('names.txt'))
  l = random.randint(0,length('last.txt'))
  c = random.randint(0,length('cities.txt'))
  t = random.randint(0,length('teams.txt'))
  p = random.randint(0,length('positions.txt'))
  r = open('names.txt')
  first = r.readlines()
  a = open('last.txt')
  last = a.readlines()
  s = open('cities.txt')
  cities = s.readlines()
  e = open('teams.txt')
  teams = e.readlines()
  o = open('positions.txt')
  posi = o.readlines()
  first[:] = [line.rstrip('\n') for line in first]
  last[:] = [line.rstrip('\n') for line in last]
  cities[:] = [line.rstrip('\n') for line in cities]
  teams[:] = [line.rstrip('\n') for line in teams]
  posi[:] = [line.rstrip('\n') for line in posi]
  print first[n], last[l]+',' ,posi[p], 'on the' ,cities[c], teams[t]
  go = raw_input('')
