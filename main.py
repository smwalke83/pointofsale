from classes import Product, Catalogue
from functions import get_catalogue, sales_mode

def main():
    catalogue, product_list = get_catalogue()
    sales_mode(catalogue, product_list)

main()




