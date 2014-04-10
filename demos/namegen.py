import random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i

print 'First names:', file_len('names.txt') + 1
print 'Last names:', file_len('last.txt') + 1

go = raw_input('')
while go == '':
  n = random.randint(0,file_len('names.txt'))
  l = random.randint(0,file_len('last.txt'))
  r = open('names.txt')
  first = r.readlines()
  a = open('last.txt')
  last = a.readlines()
  first[:] = [line.rstrip('\n') for line in first]
  last[:] = [line.rstrip('\n') for line in last]
  print first[n],last[l]
  go = raw_input('')
