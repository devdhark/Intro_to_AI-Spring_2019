import common
def df_search(map):
	found = False
	start_node = find_start(map)
	map[start_node[0]][start_node[1]] = 4
	found = DFS(map, start_node)
	return found

def DFS(map, node):
	if goal(map, node) == True:
		map[node[0]][node[1]] = 4
		map[node[0]][node[1]] = 5
		return True
	map[node[0]][node[1]] = 4
	for n in expand(map, node):
		if DFS(map, n) != False:
			map[node[0]][node[1]] = 5
			return True
	return False

def bf_search(map):
	found = False
	queue = []
	path = []
	for x in range(common.constants.MAP_HEIGHT):
    		path = path + [[0]*common.constants.MAP_WIDTH]
	for i in range(common.constants.MAP_WIDTH):
                for j in range(common.constants.MAP_HEIGHT):
                        path[j][i] = 0
	start_node = find_start(map)
	node = start_node
	queue.append(node)
	while queue:
		node = queue[0]
		if goal(map, node) == True:
                                map[node[0]][node[1]] = 4
                                found = True
				goal_node = [node[0], node[1]]
				break
		map[node[0]][node[1]] = 4
		for n in expand(map, node):
			queue.append(n)
			path[n[0]][n[1]] = node
		queue.pop(0)
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
