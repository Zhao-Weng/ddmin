
import time


class InfiniteLoopException(Exception):
	pass

if __name__ == '__main__':
	start = time.time()
	i = 1
	y = 1
	if (i == 1):
		y += 2

	while (True):
		i = 1
		end = time.time()
		if (end - start > 5):
			#raise InfiniteLoopException("infinite Loop")
			raise InfiniteLoopException()

