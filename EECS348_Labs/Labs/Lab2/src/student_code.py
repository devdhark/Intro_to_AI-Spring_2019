import common
def astar_search(map):
	found = False
  	frontier = []
	path = []
	g = 0
	for i in range(common.constants.MAP_HEIGHT):
    		path = path + [[0]*common.constants.MAP_WIDTH]
	for i in range(common.constants.MAP_WIDTH):
                for j in range(common.constants.MAP_HEIGHT):
                        path[j][i] = 0
	start_node = find_start(map)
	goal_node = find_goal(map)
	if (start_node == False) or (goal_node == False):
		found = False
		return found
	node = start_node
	frontier.append(node)
	while frontier:
		f_min = 10000
		for n in frontier:
			g = 0
			m = path[n[0]][n[1]]
			while m != 0:
				m = path[m[0]][m[1]]
				g = g + 1
			f = g + mann_dist(n, goal_node)
			if f < f_min:
				f_min = f
				next_node = n
			elif f == f_min:
				if n[1] < next_node[1]:
					next_node = n
				elif n[1] == next_node[1]:
					if n[0] < next_node[0]:
						next_node = n
		node = next_node
		if goal(map, node) == True:
			map[node[0]][node[1]] = 4
			found = True
			break
		map[node[0]][node[1]] = 4
		for n in expand(map, node):
			frontier.append(n)
			path[n[0]][n[1]] = node
		count = 0
		for n in frontier:
			if n == next_node:
				frontier.pop(count)
			count = count + 1
	if found == False:
		return False
	path_node = goal_node
	while path[path_node[0]][path_node[1]] != 0:
		map[path_node[0]][path_node[1]] = 5
		path_node = path[path_node[0]][path_node[1]]
	map[start_node[0]][start_node[1]] = 5
	return found

def find_start(map):
	for i in range(common.constants.MAP_WIDTH):
		for j in range(common.constants.MAP_HEIGHT):
			if map[j][i] == 2:
				return (j,i)
	return False

def find_goal(map):
	for i in range(common.constants.MAP_WIDTH):
		for j in range(common.constants.MAP_HEIGHT):
			if map[j][i] == 3:
				return (j,i)
	return False

def goal(map, node):
	if map[node[0]][node[1]] == 3:
		return True
	else:
		return False

def expand(map, node):
	neighbor = []
	if (node[1]+1) in range(common.constants.MAP_WIDTH) and (map[node[0]][node[1]+1] in [0,3]):
		neighbor.append((node[0], node[1]+1))
	if (node[0]+1) in range(common.constants.MAP_HEIGHT) and (map[node[0]+1][node[1]] in [0,3]):
		neighbor.append((node[0]+1, node[1]))
	if (node[1]-1) in range(common.constants.MAP_WIDTH) and (map[node[0]][node[1]-1] in [0,3]):
		neighbor.append((node[0], node[1]-1))
	if (node[0]-1) in range(common.constants.MAP_HEIGHT) and (map[node[0]-1][node[1]] in [0,3]):
		neighbor.append((node[0]-1, node[1]))
	return neighbor

def mann_dist(node, goal_node):
	mann_dist = abs(goal_node[0] - node[0]) + abs(goal_node[1] - node[1])
	return mann_dist
