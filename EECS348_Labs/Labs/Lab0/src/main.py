import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

msg=student_code.get_msg()
if msg!="hello world!":
	print("Message received: "+msg+"(" + bcolors.RED + "Fail" + bcolors.NORMAL +")")
	exit(1)
else:
	print("Message received: "+msg+"(" + bcolors.GREEN + "Success" + bcolors.NORMAL +")")
	exit(0)
