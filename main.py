from matplotlib import pyplot as plt

def generateFibonacci(n: int):
	fibs = []

	for i in range(0, n + 1):
		if i == 0 or i == 1: fibs.append(1)
		else: fibs.append(fibs[-1] + fibs[-2])

	return fibs


if __name__ == '__main__':
	nums = generateFibonacci(30)

	plt.scatter(
		[i for i in range(1, len(nums) + 1)],
		nums,
		c = '#000000',
	)

	plt.grid()
	plt.show()