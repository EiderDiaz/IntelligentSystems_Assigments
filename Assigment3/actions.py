
def actions(state):
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

    print(agent)
    print(treasure)
    print(movable)
    print(obstacles)

    print(movable_objects)
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

def checkObject(agent, objects, direction):
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

def checkPushPull(agent, movable_objects, obstacles, direction, movement):
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


state1 = (('A', (1,1)), ('T', (1,2)), ('O',((1,3),(2,1)))) #Should return 4 Moves
print(actions(state1))