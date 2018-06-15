import sys
import re
import pdb
import time
import os
from argparse import ArgumentParser
from optparse import OptionParser
from testcase.infiniteLoop import InfiniteLoopException

class Result:
    Pass = 1
    Fail = 2
    Unresolved = 3


class BreakoutException(Exception):
	def __init__(self, message):
		self.message = message


###########################################
# array input minimization

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
			granularity *= 2     # can try different values to divide into different pieces
			if (granularity > len(data)):
				granularity = len(data)
		except BreakoutException:
			pass
	return data


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



#####################################################
# python program testcase minimization

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
    return "".join(b)


def executeTest(code):
    # arguments = "t.py".encode('utf-8')
    # filename = "handleInput.py"
    # result = subprocess.run(["python", filename, "t.py"], stderr=subprocess.PIPE)
    # print(result.stdout.decode('utf-8'))
	try:
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
		if ((str(ex) == "<class '__main__.InfiniteLoopException'>") or
			(ex is StopIteration) or (ex is OverflowError) or (ex is FloatingPointError) or (ex is ZeroDivisionError) or
			(ex is AssertionError) or (ex is AttributeError) or (ex is IndexError) or (ex is KeyError) or (ex is UnboundLocalError) or
			 (ex is NotImplementedError)):
			
			setGlobal(ex)
			return ddmin(data, 2)
		else:
			raise Exception('unsupported error')
	raise Exception('function must fail')


def startDdmin():
	filename = sys.argv[1]
	f = open(filename, "r")
	code = ''.join(f.readlines())
	print(findMin(code))


def startDdmin_r(args):
    file_path = args[0]
    # create a new file
    f_tmp = open("tmp.py", "w")
    f_file = open(file_path, "r")

    file_path_array = file_path.split("/")
    file_path_pre = "/".join(file_path_array[0:-1])
    
    customized_module_imported = []

    for line in f_file:
        keywords = line.split(" ")
        is_module = False
        for module_imported in customized_module_imported:
          if line.find(module_imported + ".") > 0:
              f_tmp.write(line.replace(module_imported + ".", ""))
              is_module = True
              break
        if is_module:
          continue

        if keywords[0] == "import" and os.path.isfile(file_path_pre + "/" + keywords[1][0:-1] + ".py"):
            # read the code, whether there is import of local module, copy into new file
            library_path = file_path_pre + "/" + keywords[1][0:-1] + ".py"
            customized_module_imported.append(keywords[1][0:-1])
            f_tmp.write(open(library_path, "r").read())
        else:
            f_tmp.write(line)
    f_tmp.close()
    with open('tmp.py', 'r') as myfile:
        code = myfile.read()
    os.remove("tmp.py")
    m = findMin(code)
    print(m)


def setGlobal(ex):
    global e, stre
    e = ex
    stre = str(e)
    print("Catching "+ str(ex))


if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-r", action="store_true", dest="recursive")
	(options, args) = parser.parse_args()

    # print options
	if args == []:
		print ("Usage: python ddmin.py [-r] filepath")
		exit()
	start = time.time()
	if options.recursive:
		startDdmin_r(args)
	else:
		startDdmin()
	end = time.time()
	print("Time elapsed: "+str(end-start))


