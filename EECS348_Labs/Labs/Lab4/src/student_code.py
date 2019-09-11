import common

class variables:
	counter=0

def sudoku_backtracking(sudoku):
	variables.counter = 0
	recursive_backtracking(sudoku)
	return variables.counter

def recursive_backtracking(assignment):
	if complete(assignment):
		return assignment
	next_pos = find_pos(assignment)
	for n in [1,2,3,4,5,6,7,8,9]:
		variables.counter += 1
		if constraints(assignment, next_pos, n):
			assignment[next_pos[0]][next_pos[1]] = n
			result = recursive_backtracking(assignment)
			if result != 0:
				return result
			assignment[next_pos[0]][next_pos[1]] = 0
	return 0

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	recursive_forwardchecking(sudoku)
	return variables.counter

def recursive_forwardchecking(assignment):
	if complete(assignment):
		return assignment
	next_pos = find_pos(assignment)
	for value in domain(assignment, next_pos):
		variables.counter += 1
		if constraints(assignment, next_pos, value):
			assignment[next_pos[0]][next_pos[1]] = value
			result = recursive_forwardchecking(assignment)
			if result != 0:
				return result
			assignment[next_pos[0]][next_pos[1]] = 0
	return 0

def domain(assignment, next_pos):
	new_domain = []
	for value in [1,2,3,4,5,6,7,8,9]:
		if constraints(assignment, next_pos, value):
			new_domain.append(value)
	return new_domain

def sudoku_mrv(sudoku):
	variables.counter = 0
	recursive_mrv(sudoku)
	return variables.counter

def recursive_mrv(assignment):
	if complete(assignment):
		return assignment
	next_pos = find_most_const_domain(assignment)
	for value in domain(assignment, next_pos):
		variables.counter += 1
		if constraints(assignment, next_pos, value):
			assignment[next_pos[0]][next_pos[1]] = value
			result = recursive_mrv(assignment)
			if result != 0:
				return result
			assignment[next_pos[0]][next_pos[1]] = 0
	return 0

def find_most_const_domain(assignment):
	most_const_domain = [1,2,3,4,5,6,7,8,9]
	for i in range(9):
		for j in range(9):
			if assignment[i][j] == 0:
				check_domain = domain(assignment, (i,j))
				if len(check_domain) < len(most_const_domain):
					most_const_domain = list(check_domain)
					position = (i,j)
	return position

def complete(assignment):
	if any(0 in sublist for sublist in assignment):
		return 0
	return 1

def constraints(assignment, next_pos, value):
	if value in assignment[next_pos[0]]:	# row constraint
		return 0
	for i in assignment:	# column constraint
		if i[next_pos[1]] == value:
			return 0
	if next_pos[0] in [0,1,2]:
		x = 0
	elif next_pos[0] in [3,4,5]:
		x = 3
	elif next_pos[0] in [6,7,8]:
		x = 6
	if next_pos[1] in [0,1,2]:
		y = 0
	elif next_pos[1] in [3,4,5]:
		y = 3
	elif next_pos[1] in [6,7,8]:
		y = 6
	for i in [x, x+1, x+2]:		# box constraint
		for j in [y, y+1, y+2]:
			if assignment[i][j] == value:
				return 0
	return 1

def find_pos(assignment):
	for i in range(9):
		for j in range(9):
			if assignment[i][j] == 0:
				return (i,j)
