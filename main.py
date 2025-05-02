import sys, os
from classes import Product, Catalogue
from functions import get_catalogue, remove_product, add_product, sales_mode, inv_mode, rmv_mode, exit_mode

def main():
    catalogue, product_list = get_catalogue()
    mode = "Sales"
    sales_mode()

main()




#below is testing how things will work. The plan is to open the catalogue file on starting the program and create the catalogue out of the file.
#The structure will be something like: each line is one product, containing all of the class data separated by commas. After seperating the file into lines, iterate each line
    #and create a product to add to the catalogue. When a new item is scanned in, it will be added to the list and the catalogue file can be appended to or rewritten.
'''


for line in sys.stdin:
    if "q" == line.rstrip():
        break
    sys.stdout.write(f"Input: {line}")
    # print statement aslo works
print("Exit")
'''