import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

print 'Cities:', file_len('cities.txt') + 1
print 'Team names:', file_len('teams.txt') + 1

go = raw_input('')
while go == '':
  c = random.randint(0,file_len('cities.txt'))
  t = random.randint(0,file_len('teams.txt'))
  s = open('cities.txt')
  cities = s.readlines()
  e = open('teams.txt')
  teams = e.readlines()
  cities[:] = [line.rstrip('\n') for line in cities]
  teams[:] = [line.rstrip('\n') for line in teams]
  print cities[c],teams[t]
  go = raw_input('')
