import sys
import re


class Result:
    Pass = 1
    Fail = 2
    Unresolved = 3


class BreakoutException(Exception):
    def __init__(self, message):
        self.message = message


def Minimize(data, f):
    if (f('') == Result.Fail):
        print("Here")
        return []
    if (f(data) == Result.Pass):
        raise ValueError('ddmin: function must fail on data')
    return ddmin(data, f, 2)


def ddmin(data, f, granularity):
    #whole = data
    #length = len(data)
    while (len(data) >= 2):
        try:
            subsets = makeSubsets(data, granularity)
            # pdb.set_trace()
            for subset in subsets:
                print("Testing Subsets")
                print(subset)
                if (f(subset) == Result.Fail):
                    data = subset
                    granularity = 2
                    raise BreakoutException('continue while loop')
            for i in range(len(subsets)):
                complement = makeComplement(subsets, i)
                print("Testing Complement")
                print(complement)
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


def makeSubsets(s, n):
    ret = []
    while(n > 0):
        i = len(s) // n
        copyS = s
        s = copyS[i:]
        ret.append("".join(copyS[:i]))
        n -= 1
    return ret



def makeComplement(subsets, n):
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


def f(d):
    a = executetest(d)
    #seen1, seen2, seen3 = False, False, False
    #for v in d:
        #if (v == 1):
            #seen1 = True
        #if (v == 7):
            #seen2 = True
       # if (v == 8):
            #seen3 = True
    #if (seen1 and seen2 and seen3):
        #return Result.Fail
    #else:
        #return Result.Pass
    return a

#??????????
def ExampleMinimize():
    code = "".join(handleInput())

    #data = [1, 2, 3, 4, 5, 6, 7, 8]
    m = Minimize(code, f)
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

def executetest(code):
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
    except ZeroDivisionError as e2:
        return Result.Fail
    except NameError as e3:
        print("Name Err Detected. Ignored")
        # print(e3)
        return Result.Unresolved

    return Result.Pass


if __name__ == '__main__':
    ExampleMinimize()


