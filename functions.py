from classes import Product, Catalogue
import sys
import datetime

def get_catalogue():
    file = open("./catalogue.txt")
    content = file.read()
    file.close()
    content_list = content.split("\n")
    catalogue = Catalogue()
    file = open("./total_sales.txt")
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
            if catalogue.dict[UPC].quantity < 10:
                catalogue.dict[UPC].is_low = True
            if catalogue.dict[UPC].quantity <= 0:
                catalogue.dict[UPC].is_out = True
    return catalogue, content_list

def remove_product(UPC, product_list, catalogue):
    for item in product_list:
        if UPC in item:
            index = product_list.index(item)
    product_list.pop(index)
    del catalogue.dict[UPC]
    file = open("./catalogue.txt", "w")
    content = "\n".join(product_list)
    file.write(content)
    file.close()

def add_product(name, description, price, quantity, UPC, product_list, catalogue, is_low, is_out):
    product_list.append(f"{name}, {description}, {price}, {quantity}, {UPC}")
    catalogue.dict[UPC] = Product(name, description, price, quantity, UPC)
    catalogue.dict[UPC].is_low = is_low
    catalogue.dict[UPC].is_out = is_out
    file = open("./catalogue.txt", "a")
    content = f"\n{name}, {description}, {price}, {quantity}, {UPC}"
    file.write(content)
    file.close()

def update_product(product_list, catalogue, old_UPC, new_UPC = None):
    for product in product_list:
        if old_UPC in product:
            index = product_list.index(product)
            break
    if new_UPC == None:
        product = catalogue.dict[old_UPC]
    else:
        product = catalogue.dict[new_UPC]
    product_list[index] = f"{product.name}, {product.description}, {product.price}, {product.quantity}, {product.UPC}"
    update_catalogue(product_list)

def update_catalogue(product_list):
    file = open("./catalogue.txt", "w")
    content = "\n".join(product_list)
    file.write(content)
    file.close()

def update_sales(catalogue):
    file = open("./total_sales.txt", "w")
    content = catalogue.sales
    file.write(str(content))
    file.close()

def update_sales_log(sale_total):
    now = datetime.datetime.now()
    file = open("./sales_log.txt", "a")
    content = f"\n{sale_total:.2f} - {now}"
    file.write(content)
    file.close()

def sales_mode(catalogue, product_list, mode = "Sales"):
    sys.stdout.flush()
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Sales Mode\n")
    sys.stdout.write("Scan UPC of Sales Item\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("Commands are not case sensitive\n")
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sale_total = 0.0
    sale_list = []
    while mode == "Sales":
        line = sys.stdin.readline().strip()
        if line.upper() == "INV":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write("Transaction Cancelled\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sale_total = 0.0
            sale_list = [] 
            mode = "INV"
        elif line.upper() == "RMV":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write("Transaction Cancelled\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sale_total = 0.0
            sale_list = []
            mode = "RMV"
        elif line.upper() == "EXIT":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write("Transaction Cancelled\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sale_total = 0.0
            sale_list = []
            mode = "Exit"
        elif line.upper() == "HELP":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Sales Mode\n')
            sys.stdout.write("Scan UPC of Sales Item\n")
            sys.stdout.write('Type "CLOSE" to end the current transaction\n')
            sys.stdout.write('Type "CANCEL" to cancel the current transaction\n')
            sys.stdout.write('Type "INV" to enter Inventory Management Mode\n')
            sys.stdout.write('Type "RMV" to enter Product Removal Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("Commands are not case sensitive\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif line.upper() == "CLOSE":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            for item in sale_list:
                catalogue.dict[item.UPC].quantity -= 1
                for product in product_list:
                    if item.UPC in product:
                        new_product = f"{catalogue.dict[item.UPC].name}, {catalogue.dict[item.UPC].description}, {catalogue.dict[item.UPC].price}, {catalogue.dict[item.UPC].quantity}, {catalogue.dict[item.UPC].UPC}"
                        product_list[product_list.index(product)] = new_product
                        break
                if catalogue.dict[item.UPC].quantity < 10:
                    catalogue.dict[item.UPC].is_low = True
                    sys.stdout.write(f"Item flagged - Quantity below 10\n")
                if catalogue.dict[item.UPC].quantity <= 0:
                    catalogue.dict[item.UPC].is_out = True
                    sys.stdout.write(f"Item flagged - Zero or below quantity\n")
            update_catalogue(product_list)
            catalogue.sales += sale_total
            update_sales(catalogue)
            sys.stdout.write(f"Transaction closed. Sale total: {sale_total:.2f}\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            update_sales_log(sale_total)
            sale_total = 0.0
            sale_list = []
        elif line.upper() == "CANCEL":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write("Transaction cancelled.\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sale_total = 0.0
            sale_list = []
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
                sys.stdout.write(f"{catalogue.dict[line]}\n")
                sale_total += catalogue.dict[line].price
                sale_list.append(catalogue.dict[line])
                sys.stdout.write(f"Sale Total: {sale_total:.2f}\n")
                sys.stdout.write("Type CLOSE to end the current transaction\n")
                sys.stdout.write("Type CANCEL to cancel the current transaction\n")
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if mode == "INV":
        inv_mode(catalogue, product_list)
    if mode == "RMV":
        rmv_mode(catalogue, product_list)
    if mode == "Exit":
        exit_mode()
def inv_mode(catalogue, product_list, mode = "INV"):
    sys.stdout.flush()
    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    sys.stdout.write("Entering Inventory Management Mode\n")
    sys.stdout.write("Scan UPC of existing item OR Search for item\n")
    sys.stdout.write("Type ADD to create new item\n")
    sys.stdout.write("Type FLAGS to see low quantity items\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("Commands are not case sensitive\n")
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
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write('Currently in Inventory Managment Mode\n')
            sys.stdout.write("Scan UPC or search for existing item\n")
            sys.stdout.write('Type "ADD" to add new product\n')
            sys.stdout.write('Type "FLAGS" to see low quantity items\n')
            sys.stdout.write('Type "SALES" to enter Sales Mode\n')
            sys.stdout.write('Type "RMV" to enter Product Removal Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("Commands are not case sensitive\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif line.upper() == "FLAGS":
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            flag_list = []
            for key in catalogue.dict:
                if catalogue.dict[key].is_low or catalogue.dict[key].is_out:
                    flag_list.append(catalogue.dict[key])
            flag_string = ""
            for item in flag_list:
                flag_string += f"Item: {item.name} Quantity: {item.quantity} UPC: {item.UPC}\n"
            sys.stdout.write("Flagged Items:\n")
            sys.stdout.write(f"{flag_string}\n")
            sys.stdout.write("Enter UPC or search item to update quantities\n")
            sys.stdout.write("Enter HELP for more options\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        elif line.upper() == "ADD":
            add = True
            sys.stdout.flush()
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            sys.stdout.write("Adding new item\n")
            while add == True:
                name = True
                sys.stdout.write("Enter Item Name\n")
                while name == True:
                    item_name = sys.stdin.readline().strip()
                    name = False
                description = True
                sys.stdout.write("Enter Item Description\n")
                while description == True:
                    item_description = sys.stdin.readline().strip()
                    description = False
                price = True
                sys.stdout.write("Enter Item Price\n")
                while price == True:
                    item_price = None
                    line = sys.stdin.readline().strip()
                    try:
                        item_price = float(line)
                    except Exception:
                        sys.stdout.write("Invalid Price - Please enter a numerical price value without dollar signs\n")
                        sys.stdout.write("Enter Item Price\n")
                    if item_price is not None:
                        price = False
                quantity = True
                sys.stdout.write("Enter Item Quantity\n")
                while quantity == True:
                    item_quantity = None
                    line = sys.stdin.readline().strip()
                    try:
                        item_quantity = int(line)
                    except Exception:
                        sys.stdout.write("Invalid Input - Quantity must be an integer\n")
                        sys.stdout.write("Enter Item Quantity\n")
                    if item_quantity is not None:
                        if item_quantity < 10:
                            is_low = True
                        else:
                            is_low = False
                        if item_quantity <= 0:
                            is_out = True
                        else:
                            is_out = False
                        quantity = False
                UPC = True
                sys.stdout.write("Enter Item UPC\n")
                while UPC == True:
                    item_UPC = sys.stdin.readline().strip()
                    if item_UPC not in catalogue.dict:
                        UPC = False
                    else:
                        sys.stdout.write("Invalid UPC - UPC matches existing item; UPCs must be unique\n")
                add_product(item_name, item_description, item_price, item_quantity, item_UPC, product_list, catalogue, is_low, is_out)
                sys.stdout.write(f"Product added: {catalogue.dict[item_UPC]}\n")
                add = False
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            if line in catalogue.dict:
                alter = True
                UPC = line
                sys.stdout.flush()
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                sys.stdout.write(f"Product found: {catalogue.dict[UPC]}\n")
                sys.stdout.write("What would you like to change?\n")
                sys.stdout.write('"N" = Item Name, "D" = Item Description, "P" = Item Price, "Q" = Item Quantity, "UPC" = UPC, "NONE" = Exit\n')
                while alter == True:
                    line = sys.stdin.readline().strip()
                    if line.upper() == "N":
                        name = True
                        sys.stdout.write("Enter New Name\n")
                        while name == True:
                            line = sys.stdin.readline().strip()
                            catalogue.dict[UPC].name = line
                            sys.stdout.write("Name Changed\n")
                            update_product(product_list, catalogue, UPC)
                            name = False
                        alter = False
                    elif line.upper() == "D":
                        description = True
                        sys.stdout.write("Enter New Description\n")
                        while description == True:
                            line = sys.stdin.readline().strip()
                            catalogue.dict[UPC].description = line
                            sys.stdout.write("Description Changed\n")
                            update_product(product_list, catalogue, UPC)
                            description = False
                        alter = False
                    elif line.upper() == "P":
                        price = True
                        sys.stdout.write("Enter New Price\n")
                        while price == True:
                            new_price = None
                            line = sys.stdin.readline().strip()
                            try:
                                new_price = float(line)
                            except Exception:
                                sys.stdout.write("Invalid Price - Please enter a numerical price value without dollar signs\n")
                                sys.stdout.write("Enter New Price\n")
                            if new_price is not None:
                                catalogue.dict[UPC].price = new_price
                                sys.stdout.write("Price Changed\n")
                                update_product(product_list, catalogue, UPC)
                                price = False
                        alter = False
                    elif line.upper() == "Q":
                        quantity = True
                        sys.stdout.write("Enter New Quantity\n")
                        while quantity == True:
                            new_quantity = None
                            line = sys.stdin.readline().strip()
                            try:
                                new_quantity = int(line)
                            except Exception:
                                sys.stdout.write("Invalid Input - Quantity must be an integer\n")
                                sys.stdout.write("Enter New Quantity\n")
                            if new_quantity is not None:
                                catalogue.dict[UPC].quantity = new_quantity
                                if new_quantity >= 10:
                                    catalogue.dict[UPC].is_low = False
                                else:
                                    catalogue.dict[UPC].is_low = True
                                if new_quantity > 0:
                                    catalogue.dict[UPC].is_out = False
                                else:
                                    catalogue.dict[UPC].is_out = True
                                sys.stdout.write("Quantity Changed\n")
                                update_product(product_list, catalogue, UPC)
                                quantity = False
                        alter = False
                    elif line.upper() == "UPC":
                        UPC_alter = True
                        sys.stdout.write("Enter New UPC\n")
                        while UPC_alter == True:
                            line = sys.stdin.readline().strip()
                            catalogue.dict[UPC].UPC = line
                            sys.stdout.write("UPC Changed\n")
                            update_product(product_list, catalogue, UPC, new_UPC = line)
                            UPC_alter = False
                        alter = False
                    elif line.upper() == "NONE":
                        sys.stdout.write("Nothing Changed\n")
                        alter = False
                    else:
                        sys.stdout.write("Invalid Input\n")
                        sys.stdout.write("What would you like to change?\n")
                        sys.stdout.write('"N" = Item Name, "D" = Item Description, "P" = Item Price, "Q" = Item Quantity, "UPC" = UPC\n, "NONE" = Exit')
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                search_list = []
                for product in product_list:
                    if line.lower() in product.lower():
                        search_list.append(product)
                if len(search_list) > 0:
                    sys.stdout.flush()
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    result_string = ""
                    for result in search_list:
                        result_string += result + "\n"
                    sys.stdout.write(f"Products found (Name, Description, Price, Quantity, UPC):\n{result_string}\n")
                    sys.stdout.write("Please enter UPC of item to alter\n")
                    sys.stdout.write("Type HELP for more options\n")
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                else:
                    sys.stdout.flush()
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    sys.stdout.write("Invalid Input - Type HELP for valid commands\n")
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
    sys.stdout.write("Scan UPC of item to remove OR Search for item\n")
    sys.stdout.write("Type HELP for options\n")
    sys.stdout.write("Commands are not case sensitive\n")
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
            sys.stdout.write("Scan UPC of item to remove OR Search for item\n")
            sys.stdout.write('Type "SALES" to enter Sales Mode\n')
            sys.stdout.write('Type "INV" to enter Inventory Management Mode\n')
            sys.stdout.write('Type "EXIT" to exit program\n')
            sys.stdout.write("Commands are not case sensitive\n")
            sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        else:
            if line not in catalogue.dict:
                search_list = []
                for product in product_list:
                    if line.lower() in product.lower():
                        search_list.append(product)
                if len(search_list) > 0:
                    sys.stdout.flush()
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    result_string = ""
                    for result in search_list:
                        result_string += result + "\n"
                    sys.stdout.write(f"Products found (Name, Description, Price, Quantity, UPC):\n{result_string}\n")
                    sys.stdout.write("Please enter UPC of item to remove\n")
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                else:
                    sys.stdout.flush()
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    sys.stdout.write("Invalid Input - Type HELP for valid commands\n")
                    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            else:
                deleting = True
                UPC = line
                sys.stdout.flush()
                sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                sys.stdout.write(f"Delete Product: {catalogue.dict[UPC]}?\n")
                sys.stdout.write('Type "Y" for yes or "N" for no\n')
                while deleting == True:
                    line = sys.stdin.readline().strip()
                    if line.upper() == "Y":
                        remove_product(UPC, product_list, catalogue)
                        sys.stdout.write("Removed product from catalogue\n")
                        deleting = False
                    elif line.upper() == "N":
                        sys.stdout.write("Product not removed\n")
                        deleting = False
                    else:
                        sys.stdout.write('Invalid input - Please enter "Y" for yes or "N" for no\n')
                        sys.stdout.write(f"Delete Product: {catalogue.dict[UPC]}?\n")
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
