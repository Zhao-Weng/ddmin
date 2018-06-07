from __future__ import print_function


def bubble_sort(collection):

    length = len(collection)
    for i in range(length):
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection


if __name__ == '__main__':
    #try:
        #raw_input          # Python 2
    #except NameError:
        #raw_input = input  # Python 3

    #user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    user_input = "1,3,2,5,4"
    unsorted = [int(item) for item in user_input.split(',')]
    a = 1
    a = a / 0
    #print(bubble_sort(unsorted))
