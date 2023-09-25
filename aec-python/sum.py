# sum.py
import argparse
 
parser = argparse.ArgumentParser(description = "sum two integers")
parser.add_argument("ints_to_sum", nargs=2, type=int)
args = parser.parse_args()
our_sum = sum(args.ints_to_sum)
print(f"The sum of values is {our_sum}")