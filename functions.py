from classes import Product, Catalogue
import sys

def get_catalogue():
    file = open("./catalogue.txt")
    content = file.read()
    file.close()
    content_list = content.split("\n")
    catalogue = Catalogue()
    file = open("./sales.txt")
    content = file.read()
    file.close()
    if len(content) == 0:
        catalogue.sales = 0.00
    else:
        catalogue.sales = float(content.strip())
    for product in content_list:
        product_data = product.split(",")
        if len(product_data) == 5:
            name = product_data[0].strip()
            description = product_data[1].strip()
            price = float(product_data[2].strip())
            quantity = int(product_data[3].strip())
            UPC = product_data[4].strip()
            catalogue.dict[UPC] = Product(name, description, price, quantity, UPC)
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

def update_product(product_list):
    file = open("./catalogue.txt", "w")
    content = "\n".join(product_list)
    file.write(content)
    file.close()

def update_sales(catalogue):
    file = open("./sales.txt", "w")
    content = catalogue.sales
    file.write(str(content))
    file.close()

def sales_mode(catalogue, product_list, mode = "Sales"):
    sys.stdout.flush()
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Sales Mode\n")
    sys.stdout.write("Scan UPC of Sales Item\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sale_total = 0.0
    while mode == "Sales":
        line = sys.stdin.readline().strip()
        if line.upper() == "INV":
            mode = "INV"
        elif line.upper() == "RMV":
            mode = "RMV"
        elif line.upper() == "EXIT":
            mode = "Exit"
        elif line.upper() == "HELP":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Sales Mode\n')
            sys.stdout.write("Scan UPC of Sales Item\n")
            sys.stdout.write('Type "INV" to enter Inventory Management Mode\n')
            sys.stdout.write('Type "RMV" to enter Product Removal Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            if line not in catalogue.dict:
                sys.stdout.flush()
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                sys.stdout.write("Invalid Input - Type HELP to add new UPC or see valid commands\n")
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                sys.stdout.flush()
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                sys.stdout.write(f"Input: {line}\n")
                catalogue.dict[line].quantity -= 1
                sys.stdout.write(f"{catalogue.dict[line]}\n")
                sale_total += catalogue.dict[line].price
                catalogue.sales += catalogue.dict[line].price
                for product in product_list:
                    if line in product:
                        new_product = f"{catalogue.dict[line].name}, {catalogue.dict[line].description}, {catalogue.dict[line].price}, {catalogue.dict[line].quantity}, {catalogue.dict[line].UPC}"
                        product_list[product_list.index(product)] = new_product
                        break
                update_product(product_list)
                update_sales(catalogue)
                if catalogue.dict[line].quantity < 0:
                    catalogue.dict[line].is_flagged = True
                    sys.stdout.write(f"Item flagged - Quantity below zero")
                sys.stdout.write(f"Sale Total: {sale_total}\n")
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            
    if mode == "INV":
        inv_mode(catalogue, product_list)
    if mode == "RMV":
        rmv_mode(catalogue, product_list)
    if mode == "Exit":
        exit_mode()
def inv_mode(catalogue, product_list, mode = "INV"):
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
        sales_mode(catalogue, product_list)
    if mode == "RMV":
        rmv_mode(catalogue, product_list)
    if mode == "Exit":
        exit_mode()
def rmv_mode(catalogue, product_list, mode = "RMV"):
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
        sales_mode(catalogue, product_list)
    if mode == "INV":
        inv_mode(catalogue, product_list)
    if mode == "Exit":
        exit_mode()
def exit_mode(mode = "Exit"):
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Exiting Program\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.exit
