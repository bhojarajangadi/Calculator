import sys

a = int(sys.argv[1]) if len(sys.argv) > 1 else 0
b = int(sys.argv[2]) if len(sys.argv) > 2 else 0
c = int(sys.argv[3]) if len(sys.argv) > 3 else 0

print("Addition:", a + b + c)
print("subtraction:", a - b)