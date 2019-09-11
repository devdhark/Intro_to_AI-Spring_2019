import common

def minmax_tictactoe(board, turn):
	if turn == common.constants.X:
		utility = max_value(board, turn)
		if utility == 1:
			return common.constants.X
		elif utility == 0:
			return common.constants.NONE
		elif utility == -1:
			return common.constants.O
	elif turn == common.constants.O:
		utility = min_value(board, turn)
		if utility == 1:
			return common.constants.X
		elif utility == 0:
			return common.constants.NONE
		elif utility == -1:
			return common.constants.O
	return common.constants.NONE

def max_value(state, turn):
	v = -10000
	status = common.game_status(state)
	if status == common.constants.X:
		return 1
	elif (common.constants.NONE not in state and status == common.constants.NONE):
		return 0
	elif status == common.constants.O:
		return -1
	for successor in expand(state, turn):
		v = max(v, min_value(successor, common.constants.O))
	return v

def min_value(state, turn):
	v = 10000
	status = common.game_status(state)
	if status == common.constants.X:
		return 1
	elif (common.constants.NONE not in state and status == common.constants.NONE):
		return 0
	elif status == common.constants.O:
		return -1
	for successor in expand(state, turn):
		v = min(v, max_value(successor, common.constants.X))
	return v

def abprun_tictactoe(board, turn):
	alpha = -1
	beta = 1
	if turn == common.constants.X:
		utility = abmax_value(board, turn, alpha, beta)
		if utility == 1:
			return common.constants.X
		elif utility == 0:
			return common.constants.NONE
		elif utility == -1:
			return common.constants.O
	elif turn == common.constants.O:
		utility = abmin_value(board, turn, alpha, beta)
		if utility == 1:
			return common.constants.X
		elif utility == 0:
			return common.constants.NONE
		elif utility == -1:
			return common.constants.O
	return common.constants.NONE

def abmax_value(state, turn, alpha, beta):
	v = -10000
	status = common.game_status(state)
	if status == common.constants.X:
		return 1
	if (common.constants.NONE not in state and status == common.constants.NONE):
		return 0
	if status == common.constants.O:
		return -1
	for successor in expand(state, turn):
		v = max(v, abmin_value(successor, common.constants.O, alpha, beta))
		if v >= beta:
			return v
		alpha = max(alpha, v)
	return v

def abmin_value(state, turn, alpha, beta):
	v = 10000
	status = common.game_status(state)
	if status == common.constants.X:
		return 1
	if (common.constants.NONE not in state and status == common.constants.NONE):
		return 0
	if status == common.constants.O:
		return -1
	for successor in expand(state, turn):
		v = min(v, abmax_value(successor, common.constants.X, alpha, beta))
		if v <= alpha:
			return v
		beta = min(beta, v)
	return v

def expand(board, turn):
	possible_states = []
	position = 0
	for n in board:
		state = list(board)
		if n == common.constants.NONE:
			if turn == common.constants.X:
				state[position] = common.constants.X
			if turn == common.constants.O:
				state[position] = common.constants.O
			possible_states.append(state)
		position = position + 1
	return possible_states
