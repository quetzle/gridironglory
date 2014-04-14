import random

team1 = {'off': 76, 'def': 64, 'st': 85}
team2 = {'off': 82, 'def': 71, 'st': 78}

chance1 = team1['off']*.475 + team1['def']*.475 + team1['st']*.05
chance2 = team2['off']*.475 + team2['def']*.475 + team2['st']*.05
both = chance1 + chance2
run = raw_input('> ')
while run == '':
    o = random.uniform(0, both)
    print o
    if o < chance1:
        print 'team1 wins'
    else:
        print 'team2 wins'
    run = raw_input('> ')
