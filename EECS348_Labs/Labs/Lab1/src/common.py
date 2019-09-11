class constants:
	MAP_WIDTH  = 10
	MAP_HEIGHT = 12


def print_map(map):
	print()
	for y in range(0,constants.MAP_HEIGHT):
		v=""
		for x in range(0,constants.MAP_HEIGHT):
			v+=str(map[y][x]);
		printf(v)

def set_map(map, data):
	for y in range(0,constants.MAP_HEIGHT):
		for x in range(0,constants.MAP_WIDTH):
			map[y][x]=int(data[y*constants.MAP_WIDTH+x])

def init_map():
	return [[0 for x in range(constants.MAP_WIDTH)] for x in range(constants.MAP_HEIGHT)]

