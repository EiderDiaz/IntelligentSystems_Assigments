from search import *
from agents import*
import time

#Create hte things that can be on the boards
class Tpiece(Thing):
    pass

class Mobs(Thing):
    pass

class Oobs(Thing):
    pass

class Board(Environment):
    #Create an environment like last assignment, mainly to add things to it and create a percept to formulate initial states
    pass

class PSA(SimpleProblemSolvingAgentProgram):
    def __call__(self, board, search_method): #Added search method to the agent call to change it easily for experiments
        self.percept = board.things #percept will just be the list of objects in the board environment
        self.search_method = search_method

        self.state = self.update_state(self.percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq.append(self.search(problem))
            #This was originally self.seq = blabla in AIMA which obviously gives an error when trying to pop it later, corrected now
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, percept): #from board.things it builds a tuple of tuples to represent the initial state
        state = {'M': [], 'O': []} #Easier to build the state as a dict

        for p in percept:
            if isinstance(p, Agent):
                state['A'] = p.location
            elif isinstance(p, Tpiece):
                state['T'] = p.location
            elif isinstance(p, Mobs):
                state['M'].append(p.location)
            elif isinstance(p, Oobs):
                state['O'].append(p.location)

        #Assembling the state into a tuple of tuple, this is necessary because tuples are hashable and graph algorithms
        #need hashable types to add to the explored set
        temp = {}
        temp['A'] = state['A']
        temp['T'] = state['T']
        temp['M'] = tuple(state['M'])
        temp['O'] = tuple(state['O'])

        state = []
        for k in temp.items():
            state.append(k)

        state = tuple(state)
        return state

    def formulate_goal(self, state): #For the PushnPull problem with 'X' in (5, 5) there are always 2 possible goal states
        goal = [(('A', (4,5)), ('T', (5,5))), (('A', (5,4)), ('T', (5,5)))]
        return goal

    def formulate_problem(self, state, goal): #create a problem object with the initial state and goal state
        problem = PushnPull(state, goal)
        return problem

    def search(self, problem): #Uses some search algorithm included in AIMA to solve the problem
        return self.search_method(problem)

class PushnPull(Problem):
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        possible_actions = []
        state = dict(state)
        agent = state['A']
        treasure = state['T']
        movable = []
        obstacles = []
        movable_objects = []

        if 'M' in state:
            movable = state['M']
        if 'O' in state:
            obstacles =  list(state['O'])

        movable_objects.append(treasure)
        for m in movable:
            movable_objects.append(m)

        # Booleans for movable objects
        movable_up = checkObject(agent, movable_objects, 'up')
        movable_down = checkObject(agent, movable_objects, 'down')
        movable_left = checkObject(agent, movable_objects, 'left')
        movable_right= checkObject(agent, movable_objects, 'right')

        # Booleans for non movable objects
        obstacle_up = checkObject(agent, obstacles, 'up')
        obstacle_down = checkObject(agent, obstacles, 'down')
        obstacle_left = checkObject(agent, obstacles, 'left')
        obstacle_right = checkObject(agent, obstacles, 'right')

        # Booleans for empty spaces for push/pull
        can_push_up = checkPushPull(agent, movable_objects, obstacles, 'up', 'push')
        can_push_down = checkPushPull(agent, movable_objects, obstacles, 'down', 'push')
        can_push_left = checkPushPull(agent, movable_objects, obstacles, 'left', 'push')
        can_push_right = checkPushPull(agent, movable_objects, obstacles, 'right', 'push')

        can_pull_up = checkPushPull(agent, movable_objects, obstacles, 'up', 'pull')
        can_pull_down = checkPushPull(agent, movable_objects, obstacles, 'down', 'pull')
        can_pull_left = checkPushPull(agent, movable_objects, obstacles, 'left', 'pull')
        can_pull_right = checkPushPull(agent, movable_objects, obstacles, 'right', 'pull')

        # Check Agent's MOVES
        if agent[0] > 1 and not movable_up and not obstacle_up:
            possible_actions.append('moveUp')

        if agent[0] < 5 and not movable_down and not obstacle_down:
            possible_actions.append('moveDown')

        if agent[1] > 1 and not movable_left and not obstacle_left:
            possible_actions.append('moveLeft')

        if agent[1] < 5 and not movable_right and not obstacle_right:
            possible_actions.append('moveRight')

        # Check Agent's PUSHES
        if agent[0] > 2 and movable_up and can_push_up:
            possible_actions.append('pushUp')

        if agent[0] < 4 and movable_down and can_push_down:
            possible_actions.append('pushDown')

        if agent[1] > 2 and movable_left and can_push_left:
            possible_actions.append('pushLeft')

        if agent[1] < 4 and movable_right and can_push_right:
            possible_actions.append('pushRight')

        # Check Agent's PULLS
        if agent[0] > 1 and movable_down and can_pull_up:
            possible_actions.append('pullUp')

        if agent[0] < 5 and movable_up and can_pull_down:
            possible_actions.append('pullDown')

        if agent[1] > 1 and movable_right and can_pull_left:
            possible_actions.append('pullLeft')

        if agent[1] < 5 and movable_left and can_pull_right:
            possible_actions.append('pullRight')

        return possible_actions

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        temp = dict(state)
        #converting the state temporarily to a dictionary makes it easier to manip the data, example: {'A': (1,1), 'T': (5, 5)}

        if action == "pushRight":
            out = []
            for i in temp['M']:
                if temp['A'][0] == i[0] and temp['A'][1] + 1 == i[1]:
                    out.append((i[0], i[1] + 1))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] == temp['T'][0] and temp['A'][1] + 1 == temp['T'][1]:
                temp['T'] = (temp['T'][0], temp['T'][1] + 1)
            temp['A'] = (temp['A'][0], temp['A'][1] + 1)

        elif action == "pushLeft":
            out = []
            for i in temp['M']:
                if temp['A'][0] == i[0] and temp['A'][1] - 1 == i[1]:
                    out.append((i[0], i[1] - 1))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] == temp['T'][0] and temp['A'][1] - 1 == temp['T'][1]:
                temp['T'] = (temp['T'][0], temp['T'][1] - 1)
            temp['A'] = (temp['A'][0], temp['A'][1] - 1)

        elif action == "pushUp":
            out = []
            for i in temp['M']:
                if temp['A'][0] - 1 == i[0] and temp['A'][1] == i[1]:
                    out.append((i[0] - 1, i[1]))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] - 1 == temp['T'][0] and temp['A'][1] == temp['T'][1]:
                temp['T'] = (temp['T'][0] - 1, temp['T'][1])
            temp['A'] = (temp['A'][0] - 1, temp['A'][1])

        elif action == "pushDown":
            out = []
            for i in temp['M']:
                if temp['A'][0] + 1 == i[0] and temp['A'][1] == i[1]:
                    out.append((i[0] + 1, i[1]))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] + 1 == temp['T'][0] and temp['A'][1] == temp['T'][1]:
                temp['T'] = (temp['T'][0] + 1, temp['T'][1])
            temp['A'] = (temp['A'][0] + 1, temp['A'][1])

        elif action == "pullRight":
            out = []
            for i in temp['M']:
                if temp['A'][0] == i[0] and temp['A'][1] - 1 == i[1]:
                    out.append((i[0], i[1] + 1))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] == temp['T'][0] and temp['A'][1] - 1 == temp['T'][1]:
                temp['T'] = (temp['T'][0], temp['T'][1] + 1)
            temp['A'] = (temp['A'][0], temp['A'][1] + 1)

        elif action == "pullLeft":
            out = []
            for i in temp['M']:
                if temp['A'][0] == i[0] and temp['A'][1] + 1 == i[1]:
                    out.append((i[0], i[1] - 1))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] == temp['T'][0] and temp['A'][1] + 1 == temp['T'][1]:
                temp['T'] = (temp['T'][0], temp['T'][1] - 1)
            temp['A'] = (temp['A'][0], temp['A'][1] - 1)

        elif action == "pullUp":
            out = []
            for i in temp['M']:
                if temp['A'][0] + 1 == i[0] and temp['A'][1] == i[1]:
                    out.append((i[0] - 1, i[1]))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] + 1 == temp['T'][0] and temp['A'][1] == temp['T'][1]:
                temp['T'] = (temp['T'][0] - 1, temp['T'][1])
            temp['A'] = (temp['A'][0] - 1, temp['A'][1])

        elif action == "pullDown":
            out = []
            for i in temp['M']:
                if temp['A'][0] - 1 == i[0] and temp['A'][1] == i[1]:
                    out.append((i[0] + 1, i[1]))
                else:
                    out.append((i[0], i[1]))
            temp['M'] = out
            if temp['A'][0] - 1 == temp['T'][0] and temp['A'][1] == temp['T'][1]:
                temp['T'] = (temp['T'][0] + 1, temp['T'][1])
            temp['A'] = (temp['A'][0] + 1, temp['A'][1])

        else:
            if action == 'moveRight':
                temp['A'] = (temp['A'][0], temp['A'][1] + 1)
            elif action == 'moveLeft':
                temp['A'] = (temp['A'][0], temp['A'][1] - 1)
            elif action == 'moveUp':
                temp['A'] = (temp['A'][0] - 1, temp['A'][1])
            elif action == 'moveDown':
                temp['A'] = (temp['A'][0] + 1, temp['A'][1])

        #This next block simply builds a proper tuple formatted state from the edited dictionary
        out = {}
        out['A'] = temp['A']
        out['T'] = temp['T']
        out['M'] = tuple(temp['M'])
        out['O'] = temp['O']

        result = []
        for k in out.items():
            result.append(k)

        result = tuple(result)
        return result


    def goal_test(self, state):
        state = dict(state)
        agent = ('A', state['A'])
        piece = ('T', state['T'])

        for g in self.goal:
            g_agent = g[0]
            g_piece = g[1]
            if g_agent == agent and g_piece == piece:
                return True
        return False

#These are custom additional functions we use to facilitate our tasks

def checkPushPull(agent, movable_objects, obstacles, direction, movement): #used in problem.actions()
    location = list(agent)

    if direction == 'up':
        if movement == 'push':
            location[0] -= 2
        elif movement == 'pull':
            location[0] -= 1
    elif direction == 'down':
        if movement == 'push':
            location[0] += 2
        elif movement == 'pull':
            location[0] += 1
    elif direction == 'left':
        if movement == 'push':
            location[1] -= 2
        elif movement == 'pull':
            location[1] -= 1
    else:
        if movement == 'push':
            location[1] += 2
        elif movement == 'pull':
            location[1] += 1

    if location[0] > 5 or location[0] < 1 or location[1] > 5 or location[1] < 1:
        return False

    for ob in obstacles:
        if tuple(location) == ob:
            return False

    for mo in movable_objects:
        if tuple(location) == mo:
            return False
    return True

def checkObject(agent, objects, direction): #Used in problem.actions()
    location = list(agent)

    if direction == 'up':
        location[0] -= 1
    elif direction == 'down':
        location[0] += 1
    elif direction == 'left':
        location[1] -= 1
    else:
        location[1] += 1

    if location[0] > 5 or location[0] < 1 or location[1] > 5 or location[1] < 1:
        return False

    for ob in objects:
        if tuple(location) == ob:
            return True

    return False

def printStepsStatesMatrix(search_result): #Graphically represent state changes and actions during solving a board of PushnPull
    if search_result == None:
        return None

    array_states = search_result.path()
    array_actions = search_result.solution()
    step=-1

    for state in array_states:
        step += 1
        print("<STEP" + str(step) + ">")
        print("state: " + str(state.state))
        temp = dict(state.state)

        for i in range(1, 8):
            for j in range(1, 8):
                if i == 1:
                    if j == 1:
                        print('+ ', end = '')
                    elif j == 7:
                        print('+')
                    else:
                        print(str(j - 1) + ' ', end = '')

                elif i == 7:
                    if j == 1:
                        print('+ ', end = '')
                    elif j == 7:
                        print('+')
                    else:
                        print(str(j - 1) + ' ', end = '')

                else:
                    if j == 1:
                        print(str(i - 1) + ' ', end = '')
                    elif j == 7:
                        print(str(i - 1))
                    else:
                        if temp['A'] == (i - 1, j - 1):
                            print('A ', end = '')
                        elif temp['T'] == (i - 1, j - 1):
                            print('T ', end = '')
                        elif [locus for locus in list(temp['M']) if locus == (i - 1, j - 1)]:
                            print('M ', end = '')
                        elif [locus for locus in list(temp['O']) if locus == (i - 1, j - 1)]:
                            print('O ', end = '')
                        elif i == 6 and j == 6:
                            print('X ', end = '')
                        else:
                            print('- ', end = '')

        if step == len(array_actions):
            break
        else:
            print("action: " + str(array_actions[step]) + "\n")

#This cell creates all the example boards in the assignment for later solving

board1 = Board()
t_1 = Tpiece()
mike_1 = PSA()
board1.add_thing(mike_1, (1, 1))
board1.add_thing(t_1, (5, 2))

board2 = Board()
m1_2 = Mobs()
m2_2 = Mobs()
m3_2 = Mobs()
o1_2 = Oobs()
o2_2 = Oobs()
t_2 = Tpiece()
mike_2 = PSA()
board2.add_thing(mike_2, (5, 1))
board2.add_thing(t_2, (2, 3))
board2.add_thing(m1_2, (3, 2))
board2.add_thing(m2_2, (3, 3))
board2.add_thing(m3_2, (3, 4))
board2.add_thing(o1_2, (3, 1))
board2.add_thing(o2_2, (3, 5))

board3 = Board()
mike_3 = PSA()
t_3 = Tpiece()
m1_3 = Mobs()
o1_3 = Oobs()
o2_3 = Oobs()
o3_3 = Oobs()
o4_3 = Oobs()
board3.add_thing(mike_3, (1, 5))
board3.add_thing(t_3, (2, 3))
board3.add_thing(m1_3, (3, 3))
board3.add_thing(o1_3, (3, 1))
board3.add_thing(o2_3, (3, 2))
board3.add_thing(o3_3, (3, 4))
board3.add_thing(o4_3, (3, 5))


board4 = Board()
mike_4 = PSA()
t_4 = Tpiece()
m1_4 = Mobs()
m2_4 = Mobs()
o1_4 = Oobs()
o2_4 = Oobs()
o3_4 = Oobs()
o4_4 = Oobs()
board4.add_thing(mike_4, (1, 1))
board4.add_thing(t_4, (2, 4))
board4.add_thing(m1_4, (2, 3))
board4.add_thing(m2_4, (3, 2))
board4.add_thing(o1_4, (3, 1))
board4.add_thing(o2_4, (3, 3))
board4.add_thing(o3_4, (4, 4))
board4.add_thing(o4_4, (4, 5))

#Board 1 solved by BFS graph search
start = time.time()
BFS_graph_board1 = mike_1(board1, breadth_first_search)
end = time.time()
printStepsStatesMatrix(BFS_graph_board1)
BFS_graph_board1_time = end - start
print("\n" + str(BFS_graph_board1_time) + " seconds to solve")

#Board2 solved by BFS graph search
start = time.time()
BFS_graph_board2 = mike_2(board2, breadth_first_search)
end = time.time()
printStepsStatesMatrix(BFS_graph_board2)
BFS_graph_board2_time = end - start
print("\n" + str(DLS_graph_board2_time) + " seconds to solve")

#Board3 solved by BFS graph search
start = time.time()
BFS_graph_board3 = mike_3(board3, breadth_first_search)
end = time.time()
printStepsStatesMatrix(BFS_graph_board3)
BFS_graph_board3_time = end - start
print("\n" + str(BFS_graph_board3_time) + " seconds to solve")

#Board4 solved by BFS graph search
start = time.time()
BFS_graph_board4 = mike_4(board4, breadth_first_search)
end = time.time()
printStepsStatesMatrix(BFS_graph_board4)
BFS_graph_board4_time = end - start
