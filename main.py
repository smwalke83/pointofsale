import sys, os
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

#get file contents
file = open("./catalogue.txt")
content = file.read()
file.close()
print(content)
#convert contents to list
content_list = content.split("\n")
print(content_list)

content_list[0] = "Hola, Hola, Hola"
content_list.append("Goodbye, Goodbye, Goodbye")
print(content_list)
#rewrite file with updated list
file = open("./catalogue.txt", "w")
content = "\n".join(content_list)
file.write(content)
