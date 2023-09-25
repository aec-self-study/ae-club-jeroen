# calc.py
import argparse
 
parser = argparse.ArgumentParser(description = "CLI Calculator.")
 
subparsers = parser.add_subparsers(help = "sub-command help", dest="command")
 
add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

sub = subparsers.add_parser("sub", help = "subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

div = subparsers.add_parser("div", help = "divide integers")
div.add_argument("ints_div", nargs=2, type=int)

def aec_subtract(ints_to_sub):
  arg_1 = ints_to_sub[0]
  arg_2 = ints_to_sub[1]
  our_sub = arg_1 - arg_2
  if our_sub < 0:
    our_sub = 0
  print(f"The subtracted result is {our_sub}")
  return our_sub

def aec_divide(ints_div):
    try:
        our_div = ints_div[0] / ints_div[1]
        print(f"the divide of values is: {our_div}")
        return our_div
    except ZeroDivisionError:
        print(f"cannot divide {ints_div[0]} by {ints_div[1]}.")



if __name__ == '__main__':
    args = parser.parse_args()
    
    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == "sub":
        aec_subtract(args.ints_to_sub)

    if args.command == "div":
        aec_divide(args.ints_div)
        # try:
        #     our_div = args.ints_div[0] / args.ints_div[1]
        #     print(f"the divide of values is: {our_div}")
        
        # except ZeroDivisionError:
        #     print(f"cannot divide {args.ints_div[0]} by {args.ints_div[1]}.")