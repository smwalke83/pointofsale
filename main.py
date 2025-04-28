import sys
from classes import Product, Catalogue

sys.stdout.write("Hello World\n")

'''
for line in sys.stdin:
    if "q" == line.rstrip():
        break
    sys.stdout.write(f"Input: {line}")
    # print statement aslo works
print("Exit")
'''

def print_to_stderr(a):
    print(a, file = sys.stderr)

print_to_stderr("Hello World")
