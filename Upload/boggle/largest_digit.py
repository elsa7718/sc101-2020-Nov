"""
File: largest_digit.py
Name: Elsa
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	fruits=[('azc',4,3),('aszx',4,3),('azdx',4,3),('azvx',4,3)]
	name=[fruits[0][0],fruits[1][0],fruits[2][0],fruits[3][0]]

	print(name)
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:a random integrate
	:return: the largest digit in the number
	"""
	n = abs(n)
	if n < 10:  # n should be a number with single digit
		return n
	else:
		digit = (n % 10) # the remainder of n divided by 10
		#find_largest_digit(n // 10) # recursion deduct the digits
		return max(digit, find_largest_digit(n // 10))



if __name__ == '__main__':
	main()
