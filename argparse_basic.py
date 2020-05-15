import argparse

parser=argparse.ArgumentParser()
parser.add_argument("base",help="Base of triangle")
parser.add_argument("height",help="Height of triangle")
arg=parser.parse_args()
print("The area of the triangle is: "+str((float(arg.base)*float(arg.height))/2))

