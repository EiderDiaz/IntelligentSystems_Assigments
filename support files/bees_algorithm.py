# CLEVER ALGORITHM: Bees Algorithm
# Author: Santiago E. Conant-Pablos, October 6, 2015

import numpy as np
import matplotlib.pyplot as plt

def objective_function(vector):
    """returns value of function to optimize"""
    return sum(vector**2)

def random_vector(minmax):
    """generate a bounded random aproximation to the solution"""
    return minmax[:,0] + (minmax[:,1] - minmax[:,0]) * np.random.random(len(minmax))

def create_random_bee(search_space):
    """create a random bee position"""
    return {'vector' : random_vector(search_space)}

def create_neigh_bee(site, patch_size, search_space):
    """create a bee inside a neighborhood"""
    vector = []
    for i,v in enumerate(site):
        v = v + np.random.random() * patch_size if np.random.random() < 0.5 \
            else v - np.random.random() * patch_size
        if v < search_space[i][0]: v = search_space[i][0]
        if v > search_space[i][1]: v = search_space[i][1]
        vector.append(v)
    return {'vector' : np.array(vector, float)}

def search_neigh(parent, neigh_size, patch_size, search_space):
    """search inside the neighborhood of a site"""
    neigh = []
    for i in range(neigh_size):
        bee = create_neigh_bee(parent['vector'], patch_size, search_space)
        bee['fitness'] = objective_function(bee['vector'])
        neigh.append(bee)
    neigh.sort(key=lambda b: b['fitness'])
    return neigh[0]

def create_scout_bees(search_space, num_scouts):
    """creates scout bees for new sites"""
    return [create_random_bee(search_space) for i in range(num_scouts)]

def bees_algorithm(max_gens, search_space, num_bees, num_sites,
                   elite_sites, patch_size, patch_dec, e_bees, o_bees):
    """implements the Bees algorithm"""
    best = None
    pop = [create_random_bee(search_space) for i in range(num_bees)]
    xp, yp = [], []
    
    for gen in range(max_gens):
        for bee in range(num_bees):
            pop[bee]['fitness'] = objective_function(pop[bee]['vector'])
            xp.append(pop[bee]['vector'][0])
            yp.append(pop[bee]['vector'][1])
        pop.sort(key = lambda b: b['fitness'])
        if not best or pop[0]['fitness'] < best['fitness']:
            best = pop[0]
        next_gen = []
        for i,parent in enumerate(pop[:num_sites]):
            neigh_size = e_bees if i < elite_sites else o_bees
            next_gen.append(search_neigh(parent, neigh_size, patch_size,
                                         search_space))
        scouts = create_scout_bees(search_space, num_bees - num_sites)
        pop = next_gen + scouts
        patch_size = patch_size * patch_dec
        print(" > it=%d, patch_size=%g, f=%g" % (gen+1,patch_size,best['fitness']))
        
    plt.axis([search_space[0,0], search_space[0,1],
              search_space[1,0], search_space[1,1]])
    plt.plot(xp, yp, 'ro', [best['vector'][0]],[best['vector'][1]], 'bs')
    
    return best

# problem configuration
problem_size = 2 # number of variables
search_space = np.array([[-5, +5] for i in range(problem_size)],float) # domains
# algorithm configuration
max_gens = 100 # maximun number of generations
num_bees = 45
num_sites = 3
elite_sites = 1
patch_size = 3.0
patch_dec = 0.95 # decrease of patch size in each generation
e_bees = 7    # number of elite bees
o_bees = 2    # number of other bees
# execute the algorithm
best = bees_algorithm(max_gens, search_space, num_bees, num_sites,
                      elite_sites, patch_size, patch_dec, e_bees, o_bees)
print("Done.\nBest Solution: f=%g, v=%s" % (best['fitness'], best['vector']))
plt.show()


