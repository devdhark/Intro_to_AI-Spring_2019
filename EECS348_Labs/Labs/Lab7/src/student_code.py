import common
import math

def detect_slope_intercept(image):
	line = common.Line()
	m_values = [x * 0.01 for x in range(-1000, 1000)]
	votes = common.init_space(2000, 2000)
	hough = common.init_space(2000, 2000)
	for i in range(2000):
		for j in range(2000):
			hough[i][j] = (0, 0)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			pixel = (image[0][y][x], image[1][y][x], image[2][y][x])
			if pixel == (0, 0, 0):
				i = 0
				for m in m_values:
					b = -x*m + y
					if b >= -1000 and b < 1000:
						votes[i][int(b) + 1000] = votes[i][int(b) + 1000] + 1
						hough[i][int(b) + 1000] = (m,b)
					i = i + 1
	max_votes = votes[0][0]
	for m in range(2000):
		for b in range(2000):
			if votes[m][b] >= max_votes:
				max_votes = votes[m][b]
				max_m = hough[m][b][0]
				max_b = hough[m][b][1]
	line.m = max_m
	line.b = max_b
	return line

def detect_normal(image):
	line=common.Line()
	pi = 3.14
	theta_values = [pi*(x/1800.0) for x in range(0, 1800)]
	votes = common.init_space(2000, 2000)
	hough = common.init_space(2000, 2000)
	for i in range(1800):
		for j in range(1800):
			hough[i][j] = (0, 0)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			pixel = (image[0][y][x], image[1][y][x], image[2][y][x])
			if pixel == (0, 0, 0):
				i = 0
				for theta in theta_values:
					r = x*math.cos(theta) + y*math.sin(theta)
					if r >= -900 and r < 900:
						votes[i][int(r) + 900] = votes[i][int(r) + 900] + 1
						hough[i][int(r) + 900] = (theta, r)
					i = i + 1
	max_votes = votes[0][0]
	for theta in range(1800):
		for r in range(1800):
			if votes[theta][r] > max_votes:
				max_votes = votes[theta][r]
				max_theta = hough[theta][r][0]
				max_r = hough[theta][r][1]
	line.r = max_r
	line.theta = max_theta
	return line

def detect_circles(image):
	r = 30
	votes = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			pixel = (image[0][y][x], image[1][y][x], image[2][y][x])
			if background(y,x,image) == False:
				neighbouring_pixels = [(image[0][y][x-1], image[1][y][x-1], image[2][y][x-1]),
				 						(image[0][y][x+1], image[1][y][x+1], image[2][y][x+1]),
										(image[0][y-1][x], image[1][y-1][x], image[2][y-1][x]),
										(image[0][y+1][x], image[1][y+1][x], image[2][y+1][x]),
										(image[0][y-1][x-1], image[1][y-1][x-1], image[2][y-1][x-1]),
				 						(image[0][y+1][x+1], image[1][y+1][x+1], image[2][y+1][x+1]),
										(image[0][y-1][x-1], image[1][y-1][x-1], image[2][y-1][x-1]),
										(image[0][y+1][x+1], image[1][y+1][x+1], image[2][y+1][x+1])]
				if (255, 255, 255) in neighbouring_pixels:
					for i in range(y-r, y+r):
						for j in range(x-r, x+r):
							if background(i,j,image)==False and ((y-i)*(y-i) + (x-j)*(x-j) == 900):
								votes[i][j] = votes[i][j] + 1
								# print("test")
	max_votes = votes[0][0]
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if votes[y][x] > max_votes:
				max_votes = votes[y][x]
	count = 0
	for rows in votes:
		for value in rows:
			if value == max_votes:
				count = count + 1
	return count

def background(y,x,image):
	if y<0 or y>common.constants.HEIGHT-1 or x<0 or x>common.constants.WIDTH-1:
		return True
	elif (image[0][y][x], image[1][y][x], image[2][y][x]) == (255, 255, 255):
		return True
	return False
