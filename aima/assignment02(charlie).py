from agents import *
from random import *


class Treasure1(Thing):
    pass


class Treasure2(Thing):
    pass


class DisposTool(Thing):
    pass


class ReuseTool(Thing):
    pass


class Island(Environment):
    def __init__(self, width=7, height=7):
        super(Island, self).__init__()

        self.width = width
        self.height = height
        # Sets iteration start and end (no walls).
        # self.x_start, self.y_start = (0, 0)
        # self.x_end, self.y_end = (self.width, self.height)

    def percept(self, agent):
        '''prints & return a list of things that are in our agent's location'''
        percepts = []
        locations = []
        # locations = self.getLocations(agent.location)
        # TODO: implement 'getLocations function
        for i in range(1,7):
            for j in range(1,7):
                locations.append([i,j])

        for location in locations:
            things = self.list_things_at(location)
            for thing in things:
                percepts.append(thing)
        print(percepts)
        return percepts

    def execute_action(self, agent, action):
        '''changes the state of the environment based on what the agent does.'''
        # TODO: check for walls and boundaries
        if action == 'moveRandom':
            direction = randint(1, 4)
            print("Hunter: Moved random")
            if direction == 1:
                action = 'moveRight'
            elif direction == 2:
                action = 'moveLeft'
            elif direction == 3:
                action = 'moveUp'
            elif direction == 4:
                action = 'moveDown'

        if action == 'moveRight':
            if agent.location[0] < 6:
                wallswalls = self.list_things_at([agent.location[0]+1, agent.location[1]], tclass=Wall)
                agent.moveRight()
                agent.performance -= 1
            else:
                agent.performance -= 5
        elif action == 'moveLeft':
            if agent.location[0] > 1:
                agent.moveLeft()
                agent.performance -= 1
            else:
                agent.performance -= 5
        elif action == 'MoveUp':
            if agent.location[1] > 1:
                agent.moveUp()
                agent.performance -= 1
            else:
                agent.performance -= 5
        elif action == 'moveDown':
            if agent.location[1] < 6:
                agent.moveDown()
                agent.performance -= 1
            else:
                agent.performance -= 5
        elif action == "Greuse":
            items = self.list_things_at(agent.location, tclass=ReuseTool)
            if len(items) != 0:
                if agent.greuse(items[0]):  #
                    self.delete_thing(items[0])  #
                    agent.holding.append('H')
        elif action == "Gdispos":
            agent.gdispos()
            items = self.list_things_at(agent.location, tclass=DisposTool)
            if len(items) != 0:
                if agent.gdispos(items[0]):  #
                    self.delete_thing(items[0])  # D
                    agent.holding.append('h')
        elif action == "GTreasure1":
            items = self.list_things_at(agent.location, tclass=Treasure1)
            if len(items) != 0:
                if agent.gTreasure1(items[0]):  # Grab Treasure 1
                    # TODO: add to performance
                    agent.performance += 20
                    self.delete_thing(items[0])  # Delete it from the Island after.
        elif action == "GTreasure2":
            items = self.list_things_at(agent.location, tclass=Treasure2)
            if len(items) != 0:
                if agent.gTreasure2(items[0]):  # Grab Treasure2
                    agent.performance += 40
                    agent.holding.remove('h')
                    self.delete_thing(items[0])  # Delete it from the Island after.
        elif action == "NoOp":
            pass

    def is_done(self):
        '''By default, we're done when we can't find a live agent,
        but to prevent killing our cute dog, we will or it with when there is no more food or water'''
        no_edibles = not any(isinstance(thing, Treasure1) or isinstance(thing, DisposTool) or isinstance(thing, ReuseTool) or isinstance(thing, Treasure2) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles


class ReflexHunter(Agent):

    def moveRight(self):
        self.location[0] += 1
        print("Hunter: Moved Right to {}.".format(self.location))

    def moveLeft(self):
        self.location[0] -= 1
        print("Hunter: Moved Left to {}.".format(self.location))

    def moveUp(self):
        self.location[1] -= 1
        print("Hunter: Moved Up to {}.".format(self.location))

    def moveDown(self):
        self.location[1] += 1
        print("Hunter: Moved Down to {}.".format(self.location))

    def greuse(self, thing):
        '''returns True upon success or False otherwise'''
        if isinstance(thing, ReuseTool):
            print("Hunter: Grabbed Reusable Tool at {}.".format(self.location))
            return True
        return False

    def gdispos(self, thing = None):
        ''' returns True upon success or False otherwise'''
        if isinstance(thing, DisposTool):
            print("Hunter: Grabbed Disposable Tool at {}.".format(self.location))
            return True
        return False

    def gTreasure1(self, thing):
        ''' returns True upon success or False otherwise'''
        if isinstance(thing, Treasure1):
            print("Hunter: Grabbed Treasure1 at {}.".format(self.location))
            return True
        return False

    def gTreasure2(self, thing):
        ''' returns True upon success or False otherwise'''
        if isinstance(thing, Treasure2):
            print("Hunter: Grabbed Treasure2 at {}.".format(self.location))
            return True
        return False


def program(percepts):
    '''Returns an action based on it's percepts'''
    print("AGENT PERFORMANCE: " + str(charlie.performance))
    print("INVENTORY: " + str(charlie.holding))

    actionTaken = False
    for p in percepts:
        # Grab actions for when agent is in same location
        if actionTaken:
            break
        in_location = charlie.location == p.location
        if isinstance(p, Treasure1) and inInventory('H'):
            if in_location:
                actionTaken = True
                return 'GTreasure1'
            else:
                moveTo = getDirection(charlie.location, p.location)
                actionTaken = True
                return moveTo
        elif isinstance(p, Treasure2) and inInventory('h'):
            if in_location:
                actionTaken = True
                return 'GTreasure2'
            else:
                moveTo = getDirection(charlie.location, p.location)
                actionTaken = True
                return moveTo
        elif isinstance(p, DisposTool):
            if in_location:
                actionTaken = True
                return 'Gdispos'
            else:
                moveTo = getDirection(charlie.location, p.location)
                actionTaken = True
                return moveTo
        elif isinstance(p, ReuseTool):
            if in_location:
                actionTaken = True
                return 'Greuse'
            else:
                moveTo = getDirection(charlie.location, p.location)
                actionTaken = True
                return moveTo

    if not actionTaken:
        return 'moveRandom'


def inInventory(tool):
    for hold in charlie.holding:
        if hold == tool:
            return True
    return False

def getDirection(origin, goal):
    if origin[0] < goal[0]:
        return 'moveRight'
    elif origin[0] > goal[0]:
        return 'moveLeft'
    elif origin [1] > goal[1]:
        return 'moveUp'
    else:
        return 'moveDown'

island = Island()
charlie = ReflexHunter(program)
treasure1 = Treasure1()
treasure2 = Treasure2()
dispos = DisposTool()
reusable = ReuseTool()
reusable2 = ReuseTool()
wall = Wall()

island.add_thing(charlie, [1,1])
charlie.performance = 50
island.add_thing(treasure1, [3,4])
island.add_thing(reusable, [6,6])
island.add_thing(reusable2, [1,3])
island.add_thing(treasure2, [5,4])
island.add_thing(dispos, [1,2])

island.run(20)