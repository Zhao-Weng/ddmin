import sys
import re
import pdb
from testcase.infiniteLoop import InfiniteLoopException

class Result:
    Pass = 1
    Fail = 2
    Unresolved = 3


class BreakoutException(Exception):
	def __init__(self, message):
		self.message = message


def Minimize(data, f):
	if (f([]) == Result.Fail):
		return []
	if (f(data) == Result.Pass):
		raise ValueError('ddmin: function must fail on data')
	return ddmin(data, f, 2)




def ddmin(data, f, granularity):
	while (len(data) >= 2):
		try:
	
			subsets = makeSubsets(data, granularity)
			# pdb.set_trace()
			for subset in subsets:
				#print(subset)
				if (f(subset) == Result.Fail):
					data = subset
					granularity = 2
					raise BreakoutException('continue while loop')
			b = [0 for i in range(len(data))]
			for i in range(len(subsets)):
				complement = makeComplement(subsets, i, b[:0])
				if (f(complement) == Result.Fail):
					granularity -= 1
					if (granularity < 2):
						granularity = 2
					data = complement
					raise BreakoutException('continue while loop')
			if (granularity == len(data)):
				return data
			granularity *= 2
			if (granularity > len(data)):
				granularity = len(data)
			# print('granunarity: {0}\n'.format(granularity))
		except BreakoutException:
			# print('granunarity: {0}\n'.format(granularity))
			pass
	return data

'''
Given the number of pieces to cut into and the origianl set, 
MakeSubsets will output an array of subset with each subset's size equal to 
lowerbound of length of the orignal set divided by number of pieces. 

'''
def makeSubsets(s, n):
	ret = []
	while(n > 0):
		i = len(s) // n
		copyS = s
		s = copyS[i:]
		ret.append(copyS[:i])
		n -= 1      # bug!!!
	# print('ret is:{0}\n'.format(ret))
	return ret


def makeComplement(subsets, n, b):
	for i in range(len(subsets)):
		s = subsets[i]
		if (i == n):
			continue
		b += s
	# print('b is:{0}\n'.format(b))
	return b


def f(d):
	seen1, seen2, seen3 = False, False, False
	for v in d:
		if (v == 1):
			seen1 = True
		if (v == 7):
			seen2 = True
		if (v == 8):
			seen3 = True
	if (seen1 and seen2 and seen3):
		return Result.Fail
	else:
		return Result.Pass


def ExampleMinimize():
	data = [1, 2, 3, 4, 5, 6, 7, 8]
	m = Minimize(data, f)
	print(m)



def ddmin(data, granularity):
    while (len(data) >= 2):
        try:
            subsets = findSubsets(data, granularity)
            for subset in subsets:
                print("Testing Subsets")
                print(subset)
                if (executeTest(subset) == Result.Fail):
                    data = subset
                    granularity = 2
                    raise BreakoutException('continue while loop')
            for i in range(len(subsets)):
                complement = findComplement(subsets, i)
                print("Testing Complement")
                print(complement)
                if (executeTest(complement) == Result.Fail):
                    granularity -= 1
                    if (granularity < 2):
                        granularity = 2
                    data = complement
                    raise BreakoutException('continue while loop')
            if (granularity == len(data)):
                return data
            granularity *= 2
            if (granularity > len(data)):
                granularity = len(data)
        except BreakoutException:
            pass
    return data


def findSubsets(set, n):
    ret = []
    while(n > 0):
        i = len(set) // n
        copy = set
        set = copy[i:]
        ret.append("".join(copy[:i]))
        n -= 1
    return ret


def findComplement(subsets, n):
    b = []
    for i in range(len(subsets)):
        s = subsets[i]
        if (i == n):
            continue
        b.append(s)
    # print('b is:{0}\n'.format(b))
    return "".join(b)


def startDdmin():


	filename = sys.argv[1]
	f = open(filename, "r")
	code = ''.join(f.readlines())
	print(findMin(code))


def findMin(data):
	if (executeTest('') == Result.Fail):
		print("trivial failure")
		return []
	try:
		# print(data)
		exec(data)
	except Exception as e:
		ex = sys.exc_info()[0]
		# pdb.set_trace()
		# 
		if (str(ex) == "<class '__main__.InfiniteLoopException'>"):
			# (ex is StopIteration) or (ex is OverflowError) or (ex is FloatingPointError) or (ex is ZeroDivisionError) or
			# (ex is AssertionError) or (ex is AttributeError) or (ex is IndexError) or (ex is KeyError) or (ex is UnboundLocalError) or
			# or (ex is NotImplementedError)
			
			setGlobal(ex)
			return ddmin(data, 2)
		else:
			raise Exception('unsupported error')
	raise Exception('function must fail')
    


def executeTest(code):
    # arguments = "t.py".encode('utf-8')
    # filename = "handleInput.py"
    # result = subprocess.run(["python", filename, "t.py"], stderr=subprocess.PIPE)
    # print(result.stdout.decode('utf-8'))
	try:
		#print(code)

		exec(code)

	except Exception:
		ex = sys.exc_info()[0]
		if (str(ex) == stre):
			print("Designated Err Detected. Catch")
			return Result.Fail
		try:
			exec(code)


		except SyntaxError as e1:
			print("Syntax Err Detected. Ignored")
			#print(e1)
			return Result.Unresolved

		except e as e2:
			print("Designated Err Detected. Catch")
			return Result.Fail
		except NameError as e3:
			print("Name Err Detected. Ignored")
			# print(e3)
			return Result.Unresolved
		except ModuleNotFoundError as e4:
			print("ModuleNotFound Err Detected. Ignored")
			# print(e4)
			return Result.Unresolved
		except TypeError as e5:
			print("Type Err Detected. Ignored")
			#print(e5)
			return Result.Unresolved
		except ImportError as e6:
			print("Import Err Detected. Ignored")
			#print(e6)
			return Result.Unresolved
		print("Pass")
	return Result.Pass

def setGlobal(ex):
    global e, stre
    e = ex
    stre = str(e)
    print("Catching "+ str(ex))


if __name__ == '__main__':
	startDdmin()



