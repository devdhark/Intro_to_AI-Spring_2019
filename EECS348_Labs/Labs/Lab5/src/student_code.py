import common
import copy

def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	for i in range(6):
		for j in range(6):
			if map[i][j] == 1:
				start = (i,j)
	temp_values = []
	old_values = copy.deepcopy(values)
	gamma = 1 - discount_per_cycle
	for m in range(6):
		for n in range(6):
			values[m][n] = 0
			if map[m][n] == 1:
				values[m][n] = 0
			if map[m][n] == 2:
				values[m][n] = delivery_fee
			elif map[m][n] == 3:
				values[m][n] = -dronerepair_cost
	for i in range(8):
    		temp_values = temp_values + [[0]*8]
	while convergence(old_values, values):
		old_values = copy.deepcopy(values)
		for m in range(1,7):
			for n in range(1,7):
				for i in range(1,7):
					temp_values[0][i] = values[0][i-1]
					temp_values[7][i] = values[5][i-1]
					temp_values[i][0] = values[i-1][0]
					temp_values[i][7] = values[i-1][5]
					for j in range(1,7):
						temp_values[i][j] = values[i-1][j-1]
				# South with special propulsion OFF
				go1 = -battery_drop_cost + gamma * (0.7 * temp_values[m+1][n] + 0.15 * temp_values[m][n-1] + 0.15 * temp_values[m][n+1])
				# West with special propulsion OFF
				go2 = -battery_drop_cost + gamma * (0.7 * temp_values[m][n-1] + 0.15 * temp_values[m+1][n] + 0.15 * temp_values[m-1][n])
				# North with special propulsion OFF
				go3 = -battery_drop_cost + gamma * (0.7 * temp_values[m-1][n] + 0.15 * temp_values[m][n+1] + 0.15 * temp_values[m][n-1])
				# East with special propulsion OFF
				go4 = -battery_drop_cost + gamma * (0.7 * temp_values[m][n+1] + 0.15 * temp_values[m+1][n] + 0.15 * temp_values[m-1][n])
				# South with special propulsion ON
				go5 = 2 * (-battery_drop_cost) + gamma * (0.8 * temp_values[m+1][n] + 0.10 * temp_values[m][n-1] + 0.10 * temp_values[m][n+1])
				# West with special propulsion ON
				go6 = 2 * (-battery_drop_cost) + gamma * (0.8 * temp_values[m][n-1] + 0.10 * temp_values[m+1][n] + 0.10 * temp_values[m-1][n])
				# North with special propulsion ON
				go7 = 2 * (-battery_drop_cost) + gamma * (0.8 * temp_values[m-1][n] + 0.10 * temp_values[m][n+1] + 0.10 * temp_values[m][n-1])
				# East with special propulsion ON
				go8 = 2 * (-battery_drop_cost) + gamma * (0.8 * temp_values[m][n+1] + 0.10 * temp_values[m+1][n] + 0.10 * temp_values[m-1][n])
				for i in range(6):
					for j in range(6):
						values[i][j] = temp_values[i+1][j+1]
				go = [go1, go2, go3, go4, go5, go6, go7, go8]
				if map[m-1][n-1] not in [2,3]:
					max = -100000000
					for i in range(8):
						if go[i] > max:
							max = go[i]
							action = i + 1
					values[m-1][n-1] = max
					policies[m-1][n-1] = action
	return values[start[0]][start[1]]

def convergence(old_values, values):
	sum = 0
	total = 0
	for i in range(6):
		for j in range(6):
			sum = sum + abs(values[i][j] - old_values[i][j])
			total = total + abs(values[i][j])
	error = (1.0*sum)/total
	if error < 0.0001:
		return 0
	return 1
