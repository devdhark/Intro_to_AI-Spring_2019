import common

def part_one_classifier(data_train,data_test):
	converge = False
	w = [0, 0, 0]
	while not converge:
		converge = True
		for X in data_train:
			classifier = w[0]*X[0] + w[1]*X[1] + w[2]
			if classifier >= 0:
				label = 1
			else:
				label = 0
			if label == X[2]:
				pass
			else:
				converge = False
				if classifier < 0:
					w[0] = w[0] + X[0]
					w[1] = w[1] + X[1]
					w[2] = w[2] + 1
				else:
					w[0] = w[0] - X[0]
					w[1] = w[1] - X[1]
					w[2] = w[2] - 1
	i = 0
	for X in data_test:
		classifier = w[0]*X[0] + w[1]*X[1] + w[2]
		if classifier >= 0:
			data_test[i][2] = 1
		else:
			data_test[i][2] = 0
		i = i + 1
	return

def part_two_classifier(data_train,data_test):
	converge =  False
	weight = []
	for i in range(9):
		weight = weight + [[0]*3]
	classifier = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	margin = .05
	lr = .25
	errors = len(data_train)
	while errors > len(data_train) * margin:
		errors = 0
		for X in data_train:
			i = 0
			for w in weight:
				# print(w)
				classifier[i] = w[0]*X[0] + w[1]*X[1] + w[2]
				i = i + 1
			max = classifier[0]
			p = 0
			winner = 0
			for j in classifier:
				if j > max:
					max = j
					winner = p
				p = p + 1
			if winner == X[2]:
				pass
			else:
				errors+=1
				weight[int(X[2])][0] += X[0] * lr
				weight[int(X[2])][1] += X[1] * lr
				weight[int(X[2])][2] += 1 * lr
				weight[winner][0] += -X[0] * lr
				weight[winner][1] += -X[1] * lr
				weight[winner][2] += -1 * lr
	count = 0
	for X in data_test:
		i = 0
		for w in weight:
			classifier[i] = w[0]*X[0] + w[1]*X[1] + w[2]
			i = i + 1
		max = classifier[0]
		p = 0
		winner = 0
		for j in classifier:
			if j > max:
				max = j
				winner = p
			p = p + 1
		data_test[count][2] = winner
		count = count + 1
	return
