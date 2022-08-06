import sys
if len(sys.argv) != 2:
 sys.exit("Missing command-line argument")
try:
 double = int(sys.argv[1]) * 2
 print(double)
except:
 sys.exit("Command-line argument is not a number")
