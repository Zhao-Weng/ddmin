import pdb


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

'''
Given the number of pieces to cut into, array of subsets, and specific index of the subsets array which should be skipped, 
makeComplement will output the complement subset with the specified subset left out from the original subsets.

'''
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

from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):
    pass

if __name__ == '__main__':
	# ExampleMinimize()
	x = DoAdd42(4)


