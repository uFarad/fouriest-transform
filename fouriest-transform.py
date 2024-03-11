import argparse

parser = argparse.ArgumentParser("Transforms a number to a radix in which is has the most fours.")
parser.add_argument("number", type=int, help="Starting number")
parser.add_argument("radix", type=int, help="Starting radix/base")

args = parser.parse_args()

print(args.number)
print(args.radix)