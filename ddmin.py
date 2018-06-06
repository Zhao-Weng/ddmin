import sys
import re


class Result:
    Pass = 1
    Fail = 2
    Unresolved = 3


class BreakoutException(Exception):
    def __init__(self, message):
        self.message = message


def findMin(data):
    if (executeTest('') == Result.Fail):
        print("Here")
        return []
    try:
        exec(data)
    except:
        ex = sys.exc_info()[0]
        #eturn ddmin(data, 2, e)
        if (ex is ArithmeticError) or (ex is OverflowError) or (ex is FloatingPointError) or (ex is ZeroDivisionError) or (ex is AssertionError) or (ex is AttributeError) or (ex is IndexError) or (ex is KeyError):
            setGlobal(ex)
            return ddmin(data, 2)
        else:
            raise ValueError('Unsupported Err.')
    raise ValueError('function must fail')


def ddmin(data, granularity):
    #whole = data
    #length = len(data)
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
            # print('granunarity: {0}\n'.format(granularity))
        except BreakoutException:
            # print('granunarity: {0}\n'.format(granularity))
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
    #s = subsets[n]
    #r = re.sub(s, '', data)
    #return r
    #s = list(subsets[n])
    #l = len(data)
    #i = 0
    #j = 0
    #re = []
    #while(j < l):
        #print(i)
        #if i == len(s):
            #re.append(data[j])
            #j += 1
            #continue
        #if (s[i] != data[j]):
            #re.append(data[j])
            #j += 1
        #else:
            #j += 1
            #i += 1

    #return "".join(re)

#??????????
def startDdmin():
    code = "".join(handleInput())

    m = findMin(code)
    print(m)

def handleInput():
    filename = sys.argv[1]
    if filename is not None:
        c = 1
        f = open(filename, "r")
        char = f.read(1)
        sub = []
        while char:
            sub.append(char)
            char = f.read(1)
            c += 1
        #print(sub)
        #print(c)
        f.close()
    return sub

def executeTest(code):
    # arguments = "t.py".encode('utf-8')
    # filename = "handleInput.py"
    # result = subprocess.run(["python", filename, "t.py"], stderr=subprocess.PIPE)
    # print(result.stdout.decode('utf-8'))
    try:
        #print(code)
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
    global e
    e = ex
    print("Catching "+ str(ex))

if __name__ == '__main__':
    startDdmin()


