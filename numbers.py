

def zero(*args):
	if len(args) == 0:
		return '0'
	else:
		return eval('0' + args[0])
	 

def one(*args):
	if len(args) == 0:
		return '1'
	else:
		return eval('1' + args[0])

def two(*args):
	if len(args) == 0:
		return '2'
	else:
		return eval('2' + args[0])

def three(*args):
	if len(args) == 0:
		return '3'
	else:
		return eval('3' + args[0])

def four(*args):
	if len(args) == 0:
		return '4'
	else:
		return eval('4' + args[0])

def five(*args):
	if len(args) == 0:
		return '5'
	else:
		return eval('5' + args[0])

def six(*args):
	if len(args) == 0:
		return '6'
	else:
		return eval('6' + args[0])

def seven(*args):
	if len(args) == 0:
		return '7'
	else:
		return eval('7' + args[0])

def eight(*args):
	if len(args) == 0:
		return '8'
	else:
		return eval('8' + args[0])

def nine(*args):
	if len(args) == 0:
		return '9'
	else:
		return eval('9' + args[0])

def plus(x):    #your code here
	return f'+{x}'

def minus(x):    #your code here
	return f'-{x}'

def times(x):    #your code here
	return f'*{x}'

def divided_by(x):    #your code here
	return f'/{x}'


# Validar con los siguientes ejemplos
print(four(times(five()))) # imprime 20
print(one(plus(eight()))) # imprime 9
print(seven(minus(three()))) # imprime 4
print(nine(divided_by(three()))) # imprime 3

