import argparse

#Constants for min and max radix
RADIX_MIN = 5
RADIX_MAX = 16

#Initiliaze array for four counts
fours = [0] * (RADIX_MAX + 1)
results = [0] * (RADIX_MAX + 1)

#Argument handling
parser = argparse.ArgumentParser("Transforms a number to a radix in which is has the most fours.")
parser.add_argument("number", help="Starting number")
parser.add_argument("radix", type=int, help="Starting radix/base")

args = parser.parse_args()

#Convert starting number to base 10 int
number_start = int(str(args.number), args.radix)

#Iterate through all valid radices
for radix in range(RADIX_MIN, RADIX_MAX + 1):
	number = number_start
	
	if number == 0:
		result = '0'
		fours[radix] = 0
	else:
		result = ''
		while number > 0:
			remainder = number % radix
			if remainder == 15:
				result = 'F' + result
			elif remainder == 14:
				result = 'E' + result
			elif remainder == 13:
				result = 'D' + result
			elif remainder == 12:
				result = 'C' + result
			elif remainder == 11:
				result = 'B' + result
			elif remainder == 10:
				result = 'A' + result
			else:
				result = str(remainder) + result
			number //= radix
		
		fours[radix] = result.count('4')
	
	results[radix] = result
	print("Base\t", radix, "\tFours\t", fours[radix], "\tResult\t", result)

winner = fours.index(max(fours))
print("\nWinner:\nBase\t", winner, "\tFours\t", fours[winner], "\tNumber\t", results[winner])
