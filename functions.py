from classes import Product, Catalogue
import sys

def get_catalogue():
    file = open("./catalogue.txt")
    content = file.read()
    file.close()
    content_list = content.split("\n")
    catalogue = Catalogue()
    for product in content_list:
        product_data = product.split(",")
        if len(product_data) == 5:
            catalogue.dict[product_data[4].strip()] = Product(product_data[0].strip(), product_data[1].strip(), product_data[2].strip(), product_data[3].strip(), product_data[4].strip())
    return catalogue, content_list

def remove_product(UPC, catalogue_list, catalogue):
    for item in catalogue_list:
        if UPC in item:
            index = catalogue_list.index(item)
    catalogue_list.pop(index)
    del catalogue.dict[UPC]
    file = open("./catalogue.txt", "w")
    content = "\n".join(catalogue_list)
    file.write(content)
    file.close()

def add_product(name, description, price, quantity, UPC, catalogue_list, catalogue):
    catalogue_list.append(f"{name}, {description}, {price}, {quantity}, {UPC}")
    catalogue.dict[UPC] = Product(name, description, price, quantity, UPC)
    file = open("./catalogue.txt", "a")
    content = f"\n{name}, {description}, {price}, {quantity}, {UPC}"
    file.write(content)
    file.close()

def sales_mode(mode = "Sales"):
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Sales Mode\n")
    sys.stdout.write("Scan UPC of Sales Item\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    while mode == "Sales":
        line = sys.stdin.readline().strip()
        if line.upper() == "INV":
            mode = "INV"
        elif line.upper() == "RMV":
            mode = "RMV"
        elif line.upper() == "EXIT":
            mode = "Exit"
        elif line.upper() == "HELP":
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Sales Mode\n')
            sys.stdout.write("Scan UPC of Sales Item\n")
            sys.stdout.write('Type "INV" to enter Inventory Management Mode\n')
            sys.stdout.write('Type "RMV" to enter Product Removal Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            #need to write the proper code here
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write(f"Input: {line}\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if mode == "INV":
        inv_mode()
    if mode == "RMV":
        rmv_mode()
    if mode == "Exit":
        exit_mode()
def inv_mode(mode = "INV"):
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Inventory Management Mode\n")
    sys.stdout.write("Scan UPC to enter new item or change existing item\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    while mode == "INV":
        line = sys.stdin.readline().strip()
        if line.upper() == "SALES":
            mode = "Sales"
        elif line.upper() == "RMV":
            mode = "RMV"
        elif line.upper() == "EXIT":
            mode = "Exit"
        elif line.upper() == "HELP":
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Inventory Managment Mode\n')
            sys.stdout.write("Scan UPC to enter new item or change existing item\n")
            sys.stdout.write('Type "SALES" to enter Sales Mode\n')
            sys.stdout.write('Type "RMV" to enter Product Removal Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            #need to write the proper code here
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Input: {line}")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if mode == "Sales":
        sales_mode()
    if mode == "RMV":
        rmv_mode()
    if mode == "Exit":
        exit_mode()
def rmv_mode(mode = "RMV"):
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Product Removal Mode\n")
    sys.stdout.write("Scan UPC of item to remove\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    while mode == "RMV":
        line = sys.stdin.readline().strip()
        if line.upper() == "INV":
            mode = "INV"
        elif line.upper() == "SALES":
            mode = "Sales"
        elif line.upper() == "EXIT":
            mode = "Exit"
        elif line.upper() == "HELP":
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Product Removal Mode\n')
            sys.stdout.write("Scan UPC of item to remove\n")
            sys.stdout.write('Type "SALES" to enter Sales Mode\n')
            sys.stdout.write('Type "INV" to enter Inventory Management Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            #need to write the proper code here
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Input: {line}")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if mode == "Sales":
        sales_mode()
    if mode == "INV":
        inv_mode()
    if mode == "Exit":
        exit_mode()
def exit_mode(mode = "Exit"):
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Exiting Program\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.exit
