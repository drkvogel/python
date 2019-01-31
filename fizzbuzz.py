
def get_word(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

numbers = range(1, 5)
sequence = []

for n in numbers[:-1]:
    sequence.append(get_word(n) + ',')
sequence.append(get_word(numbers[-1]))
print('range: ', enumerate(numbers))

print('numbers[-1]: ', numbers[-1])

sequence = ''.join(sequence)

print(sequence)
		
    


class Solution:

	def __new__(self, N, M):
		#
		# Some work here; return type and arguments should be according to the problem's requirements
		#
		
		# sequence = None
		
			# if n % 3 == 0 and n % 5 == 0:
			# 	print('FizzBuzz', end='')
			# elif n % 3 == 0:
			# 	print('Fizz', end='')
			# elif n % 5 == 0:
			# 	print('Buzz', end='')
			# else:
			# 	print(n, end='')
		
		def get_word(n):
			if n % 3 == 0 and n % 5 == 0:
				return 'FizzBuzz'
			elif n % 3 == 0:
				return 'Fizz'
			elif n % 5 == 0:
				return 'Buzz'
			else:
				return str(n)

		numbers = range(N, M+1)
		sequence = []
		
		for n in numbers[:-1]:
			sequence.append(get_word(n) + ',')
		sequence.append(get_word(numbers[-1]))
		
		sequence = ''.join(sequence)

		return sequence
		

import unittest

class SolutionMethods(unittest.TestCase):
	##
	## /!\ Unit Tests are optional but highly recommended /!\
	##
	# First Example
	##
	#def test_example(self):
	#	self.assertEqual("this is an example", "this is an example")

	##
	# Second Example
	##
	#def test_run(self):
	#	self.assertEqual(Solution(parameters), "expected_output")
	
	def test_1(self):
		self.assertEqual(Solution(1,5), "1,2,Fizz,4,Buzz")

	def test_2(self):
		self.assertEqual(Solution(5,15), "Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz")

	def test_3(self):
		self.assertEqual(Solution(99, 999), "Fizz,Buzz,101,Fizz,103,104,FizzBuzz,106,107,Fizz,109,Buzz,Fizz,112,113,Fizz,Buzz,116,Fizz,118,119,FizzBuzz,121,122,Fizz,124,Buzz,Fizz,127,128,Fizz,Buzz,131,Fizz,133,134,FizzBuzz,136,137,Fizz,139,Buzz,Fizz,142,143,Fizz,Buzz,146,Fizz,148,149,FizzBuzz,151,152,Fizz,154,Buzz,Fizz,157,158,Fizz,Buzz,161,Fizz,163,164,FizzBuzz,166,167,Fizz,169,Buzz,Fizz,172,173,Fizz,Buzz,176,Fizz,178,179,FizzBuzz,181,182,Fizz,184,Buzz,Fizz,187,188,Fizz,Buzz,191,Fizz,193,194,FizzBuzz,196,197,Fizz,199,Buzz,Fizz,202,203,Fizz,Buzz,206,Fizz,208,209,FizzBuzz,211,212,Fizz,214,Buzz,Fizz,217,218,Fizz,Buzz,221,Fizz,223,224,FizzBuzz,226,227,Fizz,229,Buzz,Fizz,232,233,Fizz,Buzz,236,Fizz,238,239,FizzBuzz,241,242,Fizz,244,Buzz,Fizz,247,248,Fizz,Buzz,251,Fizz,253,254,FizzBuzz,256,257,Fizz,259,Buzz,Fizz,262,263,Fizz,Buzz,266,Fizz,268,269,FizzBuzz,271,272,Fizz,274,Buzz,Fizz,277,278,Fizz,Buzz,281,Fizz,283,284,FizzBuzz,286,287,Fizz,289,Buzz,Fizz,292,293,Fizz,Buzz,296,Fizz,298,299,FizzBuzz,301,302,Fizz,304,Buzz,Fizz,307,308,Fizz,Buzz,311,Fizz,313,314,FizzBuzz,316,317,Fizz,319,Buzz,Fizz,322,323,Fizz,Buzz,326,Fizz,328,329,FizzBuzz,331,332,Fizz,334,Buzz,Fizz,337,338,Fizz,Buzz,341,Fizz,343,344,FizzBuzz,346,347,Fizz,349,Buzz,Fizz,352,353,Fizz,Buzz,356,Fizz,358,359,FizzBuzz,361,362,Fizz,364,Buzz,Fizz,367,368,Fizz,Buzz,371,Fizz,373,374,FizzBuzz,376,377,Fizz,379,Buzz,Fizz,382,383,Fizz,Buzz,386,Fizz,388,389,FizzBuzz,391,392,Fizz,394,Buzz,Fizz,397,398,Fizz,Buzz,401,Fizz,403,404,FizzBuzz,406,407,Fizz,409,Buzz,Fizz,412,413,Fizz,Buzz,416,Fizz,418,419,FizzBuzz,421,422,Fizz,424,Buzz,Fizz,427,428,Fizz,Buzz,431,Fizz,433,434,FizzBuzz,436,437,Fizz,439,Buzz,Fizz,442,443,Fizz,Buzz,446,Fizz,448,449,FizzBuzz,451,452,Fizz,454,Buzz,Fizz,457,458,Fizz,Buzz,461,Fizz,463,464,FizzBuzz,466,467,Fizz,469,Buzz,Fizz,472,473,Fizz,Buzz,476,Fizz,478,479,FizzBuzz,481,482,Fizz,484,Buzz,Fizz,487,488,Fizz,Buzz,491,Fizz,493,494,FizzBuzz,496,497,Fizz,499,Buzz,Fizz,502,503,Fizz,Buzz,506,Fizz,508,509,FizzBuzz,511,512,Fizz,514,Buzz,Fizz,517,518,Fizz,Buzz,521,Fizz,523,524,FizzBuzz,526,527,Fizz,529,Buzz,Fizz,532,533,Fizz,Buzz,536,Fizz,538,539,FizzBuzz,541,542,Fizz,544,Buzz,Fizz,547,548,Fizz,Buzz,551,Fizz,553,554,FizzBuzz,556,557,Fizz,559,Buzz,Fizz,562,563,Fizz,Buzz,566,Fizz,568,569,FizzBuzz,571,572,Fizz,574,Buzz,Fizz,577,578,Fizz,Buzz,581,Fizz,583,584,FizzBuzz,586,587,Fizz,589,Buzz,Fizz,592,593,Fizz,Buzz,596,Fizz,598,599,FizzBuzz,601,602,Fizz,604,Buzz,Fizz,607,608,Fizz,Buzz,611,Fizz,613,614,FizzBuzz,616,617,Fizz,619,Buzz,Fizz,622,623,Fizz,Buzz,626,Fizz,628,629,FizzBuzz,631,632,Fizz,634,Buzz,Fizz,637,638,Fizz,Buzz,641,Fizz,643,644,FizzBuzz,646,647,Fizz,649,Buzz,Fizz,652,653,Fizz,Buzz,656,Fizz,658,659,FizzBuzz,661,662,Fizz,664,Buzz,Fizz,667,668,Fizz,Buzz,671,Fizz,673,674,FizzBuzz,676,677,Fizz,679,Buzz,Fizz,682,683,Fizz,Buzz,686,Fizz,688,689,FizzBuzz,691,692,Fizz,694,Buzz,Fizz,697,698,Fizz,Buzz,701,Fizz,703,704,FizzBuzz,706,707,Fizz,709,Buzz,Fizz,712,713,Fizz,Buzz,716,Fizz,718,719,FizzBuzz,721,722,Fizz,724,Buzz,Fizz,727,728,Fizz,Buzz,731,Fizz,733,734,FizzBuzz,736,737,Fizz,739,Buzz,Fizz,742,743,Fizz,Buzz,746,Fizz,748,749,FizzBuzz,751,752,Fizz,754,Buzz,Fizz,757,758,Fizz,Buzz,761,Fizz,763,764,FizzBuzz,766,767,Fizz,769,Buzz,Fizz,772,773,Fizz,Buzz,776,Fizz,778,779,FizzBuzz,781,782,Fizz,784,Buzz,Fizz,787,788,Fizz,Buzz,791,Fizz,793,794,FizzBuzz,796,797,Fizz,799,Buzz,Fizz,802,803,Fizz,Buzz,806,Fizz,808,809,FizzBuzz,811,812,Fizz,814,Buzz,Fizz,817,818,Fizz,Buzz,821,Fizz,823,824,FizzBuzz,826,827,Fizz,829,Buzz,Fizz,832,833,Fizz,Buzz,836,Fizz,838,839,FizzBuzz,841,842,Fizz,844,Buzz,Fizz,847,848,Fizz,Buzz,851,Fizz,853,854,FizzBuzz,856,857,Fizz,859,Buzz,Fizz,862,863,Fizz,Buzz,866,Fizz,868,869,FizzBuzz,871,872,Fizz,874,Buzz,Fizz,877,878,Fizz,Buzz,881,Fizz,883,884,FizzBuzz,886,887,Fizz,889,Buzz,Fizz,892,893,Fizz,Buzz,896,Fizz,898,899,FizzBuzz,901,902,Fizz,904,Buzz,Fizz,907,908,Fizz,Buzz,911,Fizz,913,914,FizzBuzz,916,917,Fizz,919,Buzz,Fizz,922,923,Fizz,Buzz,926,Fizz,928,929,FizzBuzz,931,932,Fizz,934,Buzz,Fizz,937,938,Fizz,Buzz,941,Fizz,943,944,FizzBuzz,946,947,Fizz,949,Buzz,Fizz,952,953,Fizz,Buzz,956,Fizz,958,959,FizzBuzz,961,962,Fizz,964,Buzz,Fizz,967,968,Fizz,Buzz,971,Fizz,973,974,FizzBuzz,976,977,Fizz,979,Buzz,Fizz,982,983,Fizz,Buzz,986,Fizz,988,989,FizzBuzz,991,992,Fizz,994,Buzz,Fizz,997,998,Fizz")

	def test_4(self):
		self.assertEqual(Solution(4, 5), "4,Buzz")

	# def test_5(self):
	# 	self.assertEqual(Solution(), "")


if __name__ == "__main__":
	unittest.main()


# >Challenge Completed January 27th, 2019 at 11:57am
# >You have completed the FizzBuzz challenge and scored 100%.
# >Your String, Data Structures, Python, Q&A / Unit Testing, Q&A / Testing TDD profile tags have been updated.