import struct, array
import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def readBmp(filename):
	image=[common.init_space(480,640) for x in range(3)]
	with open(filename, 'rb') as fd:
		header = fd.read(54)
		for y in range(479,-1,-1):
			row = list(bytearray(fd.read(640 * 3)))
			#print row
			for x in range(640):
				index=x*3
				#print row[index + 0]
				image[2][y][x]= row[index + 0]
				image[1][y][x]= row[index + 1]
				image[0][y][x]= row[index + 2]
	return image
	
def between(v, l, u):
	return v>=l and v <= u

def similar(v, c, m):
	return between(v,c-m,c+m)

def check_slopeintercept ( title, filename, m_gold, b_gold):
	success=True
	image=readBmp(filename)
	line = student_code.detect_slope_intercept(image)
	print(title + " slope intercept results:")
	if (similar (line.m,m_gold,.1)):
		print("m: " + str(line.m) + " (" + bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		print("m: " + str(line.m) + " (" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") expected "+ str(m_gold))
		success = False

	if (similar(line.b,b_gold,3)):
		print("b: " + str(line.b) + " (" + bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		print("b: " + str(line.b) + " (" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") expected "+ str(b_gold))
		success = False
	print 
	return success

def check_normal ( title, filename, t_gold, r_gold):
	success=True
	image=readBmp(filename)
	line = student_code.detect_normal(image)
	print(title + " normal intercept results:")
	if (similar (line.theta,t_gold,.1)):
		print("theta: " + str(line.theta) + " (" + bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		print("theta: " + str(line.theta) + " (" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") expected "+ str(t_gold))
		success = False

	if (similar(line.r,r_gold,3)):
		print("r: " + str(line.r) + " (" + bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		print("r: " + str(line.r) + " (" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") expected "+ str(r_gold))
		success = False
	print 
	return success

def check_circles ( title, filename, c_gold):
	success=True
	image=readBmp(filename)
	circles = student_code.detect_circles(image)
	print(title + " normal intercept results:")
	if (circles==c_gold):
		print("detected: " + str(circles) + " (" + bcolors.GREEN + "SUCCESS" + bcolors.NORMAL + ")")
	else:
		print("detected: " + str(circles) + " (" + bcolors.RED + "FAIL" + bcolors.NORMAL + ") expected "+ str(c_gold))
		success = False
	print 
	return success


	
all_passed = True

all_passed = check_slopeintercept("Line 1","Labs/Lab7/line1.bmp",-.6953,403.7019) and all_passed
all_passed = check_slopeintercept("Line 2","Labs/Lab7/line2.bmp", -1.5157,551.7759) and all_passed	
all_passed = check_slopeintercept("Line 3","Labs/Lab7/line3.bmp",.3352,29.5148) and all_passed
all_passed = check_slopeintercept("Line 4","Labs/Lab7/line4.bmp",.7253,28.5143) and all_passed

all_passed = check_normal("Line 5","Labs/Lab7/line5.bmp",0.0768,337.1482) & all_passed
all_passed = check_normal("Line 6","Labs/Lab7/line6.bmp",0.0017,553.2833) & all_passed
all_passed = check_normal("Line 7","Labs/Lab7/line7.bmp",3.1295,-125.5159) & all_passed
all_passed = check_normal("Line 8","Labs/Lab7/line8.bmp",0.0244,212.1952) & all_passed

all_passed = check_circles("Circles 1","Labs/Lab7/circles1.bmp",7) & all_passed
all_passed = check_circles("Circles 2","Labs/Lab7/circles2.bmp",5) & all_passed
all_passed = check_circles("Circles 3","Labs/Lab7/circles3.bmp",9) & all_passed
all_passed = check_circles("Circles 4","Labs/Lab7/circles4.bmp",6) & all_passed

if all_passed:
	exit(0)
else:
	exit(1)
