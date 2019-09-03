def in_goal_state(state, goal):
	state = dict(state)
	agent = ('A', state['A'])
	treasure = ('T', state['T'])

	for g in goal:
		g_agent = g[0]
		g_treasure = g[1]
		if g_agent == agent and g_treasure == treasure:
			return True
	return False

state = (('A', (5,4)), ('T', (5,5)), ('M', (3,3)))
goal = [(('A', (4,5)), ('T', (5,5))), (('A', (5,4)), ('T', (5,5)))]
print(in_goal_state(state,goal))