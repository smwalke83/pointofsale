# pointofsale
This was created as my first personal python coding project. I will continue to improve the program as I learn; I am certain there is much to improve upon.

This is a basic Point of Sale system. When you run the program it builds a product catalogue from the catlogue.txt document. It will then enter sales mode. In sales mode, product UPCs can be scanned and they will be added to a transaction. When you complete a transaction, the sale total will be added to the sales_log document. You can complete a transaction by following the CLI prompts. 

By typing commands provided in the CLI prompts, you can switch to Inventory Management Mode and Product Removal Mode. Here you can find items by UPC or by searching. When you search for a product, a list will be returned with all products containing the contents of your search. 

When items are sold or altered, the catalogue.txt document is updated as well. This way, the product catalogue will always stay up to date while running the program. If the catalogue is altered outide of the program, it will be updated when the program runs again.

Type HELP at any time (commands are not case sensitive) to see what commands are available to you.