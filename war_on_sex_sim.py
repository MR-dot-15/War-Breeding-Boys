from random import choices
import matplotlib.pyplot as plt

# counter of some sort
t = 0

# parental generation
males_act = 10
males_nact = 10
females = 20
distrib = [[10, 10, 20]]

# f_1 generation
# assmp-1: every couple begets 3 children
# assmp-2: the activated genes increases the chance
# of having a male/ female child to 0.6
# 0: male, 1: female 

while(t<10):
    
    # simulating growth 
    males_act_progeny = choices([0,1], [0.6, 0.4], k = 3 * distrib[t][0])
    males_nact_progeny = choices([0,1], [0.4, 0.6], k = 3 * distrib[t][1])
    cum_females = distrib[t][2] + males_act_progeny.count(1) + males_nact_progeny.count(1)
    new_distrib = [distrib[t][0] + males_act_progeny.count(0), distrib[t][1] + males_nact_progeny.count(0), cum_females]

    # natural death
    new_distrib[0] -= int(0.3 * new_distrib[0])
    new_distrib[1] -= int(0.3 * new_distrib[1])
    new_distrib[2] -= int(0.3 * new_distrib[2])

    distrib.append(new_distrib)
    t += 1
    # print(distrib)
    population = sum(new_distrib)

# effect of war
# assmp-3: 50% of the population has died
# assmp-4: died males: females = 9:1
# assmp-5: died males_act: males_nact = 6:4
# as families with fewer sons may not let their sons go to the war
died_indv = choices([0,1], [0.9, 0.1], k = population//2)
died_males_act = int(died_indv.count(0) * 0.6)
died_males_nact = int(died_indv.count(0) * 0.4)
altered_distrib = [distrib[t][0] - died_males_act, distrib[t][1] - died_males_nact, distrib[t][2] - died_indv.count(1)]
distrib.append(altered_distrib)
t = 11

while(t<15):
    
    # simulating growth 
    males_act_progeny = choices([0,1], [0.6, 0.4], k = 3 * distrib[t][0])
    males_nact_progeny = choices([0,1], [0.4, 0.6], k = 3 * distrib[t][1])
    cum_females = distrib[t][2] + males_act_progeny.count(1) + males_nact_progeny.count(1)
    new_distrib = [distrib[t][0] + males_act_progeny.count(0), distrib[t][1] + males_nact_progeny.count(0), cum_females]

    # natural death
    new_distrib[0] -= int(0.3 * new_distrib[0])
    new_distrib[1] -= int(0.3 * new_distrib[1])
    new_distrib[2] -= int(0.3 * new_distrib[2])

    distrib.append(new_distrib)
    t += 1
    # print(distrib)
    population = sum(new_distrib)

plt.plot([i+1 for i in range(15)], [distrib[i][0] + distrib[i][1] for i in range(15)], color = 'r', label = 'Males')
plt.plot([i+1 for i in range(15)], [distrib[i][2] for i in range(15)], color = 'b', label = 'Females')
plt.xlabel('Something simlar to time')
plt.ylabel('Frequency')
plt.legend()
plt.show()