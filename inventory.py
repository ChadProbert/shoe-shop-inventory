from tabulate import tabulate


# initializing and binding the variables
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # method to get the cost of a shoe
    def get_cost(self):
        return self.cost

    # method to get the quantity of a shoe
    def get_quantity(self):
        return self.quantity

    # method to get the full details of a shoe
    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"


# empty list to store the shoe objects
shoe_list = []


# function to read the shoe data from the file
def read_shoes_data():
    try:
        with open("./inventory.txt", "r") as open_file:
            read_file = open_file.readlines()
            # loops through each line in the inventory.txt file
            for line in read_file:
                # skips the first line of the file
                if line.startswith("Country"):
                    continue
                # removes the newline character
                line = line.strip().split(",")
                country = line[0]
                code = line[1]
                product = line[2]
                cost = line[3]
                quantity = line[4]
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

        # response to the user
        print("\n✅ Shoes data read successfully.\n")
    except:
        print("\n🔴 Error reading file.\n")


# allows a user to create a new shoe in the inventory
def capture_shoes():
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

    # write the new shoe data to the file
    try:
        with open("./inventory.txt", "a") as file:
            file.write(
                f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}"
            )
        print("\n✅ New shoe data added to the inventory.\n")
    except:
        print("\n🔴 Error updating inventory.\n")


# allows a user to view all the shoes in the inventory
def view_all():
    # will run if the shoe_list is empty or if the user has not read the shoe data yet
    if len(shoe_list) == 0:
        print(
            "\n🔴 No shoes found. Please ensure that you have read the shoe data first. \n"
        )
    else:
        shoe_data = []
        for shoe in shoe_list:
            shoe_data.append(
                [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
            )
        # needed to use single quotes for the headers to work inside an f-string
        print(
            f"\n {tabulate(shoe_data, headers=['Country', 'Code', 'Product', 'Cost (ZAR)', 'Quantity'])}\n"
        )


# allows a user to add to the quantity of the shoe with the lowest quantity value
def re_stock():
    if len(shoe_list) == 0:
        print(
            "\n🔴 No shoes found. Please ensure that you have read the shoe data first.\n"
        )
        return 

    # captures the shoe name and value with the lowest quantity
    lowest_quantity = int(shoe_list[0].get_quantity())
    lowest_quantity_shoe = shoe_list[0]

    for shoe in shoe_list:
        if int(shoe.get_quantity()) < lowest_quantity:
            lowest_quantity = int(shoe.get_quantity())
            lowest_quantity_shoe = shoe

    print(
        f"\nLowest quantity - {lowest_quantity_shoe.product}: {lowest_quantity} pairs\n"
    )

    add_selection = input("Do you want to add to the quantity of this shoe? (y/n): ")
    # if user wants to add to the lowest quantity shoe
    if add_selection.lower() == "y":
        add_quantity = input("Enter the quantity to add: ")

        for shoe in shoe_list:
            if shoe.get_quantity() == str(lowest_quantity):
                # adds the user input quantity to the current quantity
                shoe.quantity = str(int(shoe.quantity) + int(add_quantity))
                print(f"\n✅ Updated quantity: {shoe.get_quantity()}\n")
                break

        # write the updated data back to the file
        try:
            with open("./inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    file.write(
                        f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                    )
            print("\n✅ Inventory file updated successfully.\n")
        except:
            print("\n🔴 Error updating inventory file.\n")
    else:
        print("\nQuantity not updated.\n")


# allows a user to search for a shoe by code
def search_shoe():
    if len(shoe_list) == 0:
        print(
            "\n🔴 No shoes found. Please ensure that you have read the shoe data first.\n"
        )
        return

    shoe_to_find = input("Enter shoe code: ")
    found = False
    for shoe in shoe_list:
        if shoe_to_find == shoe.code:
            print(f"\n✅ {shoe}\n")
            found = True
            break
    if not found:
        print("\n🔴 Shoe not found on our system.\n")


# displays the value of each shoe in the inventory
def value_per_item():
    if len(shoe_list) == 0:
        print(
            "\n🔴 No shoes found. Please ensure that you have read the shoe data first.\n"
        )
        return

    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"Shoe: {shoe.product}\nValue: R{value}\n")


# displays the shoe with the highest quantity to the user
def highest_qty():
    if len(shoe_list) == 0:
        print(
            "\n🔴 No shoes found. Please ensure that you have read the shoe data first.\n"
        )
        return

    highest_quantity = shoe_list[0].get_quantity()
    highest_quantity_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.get_quantity() > highest_quantity:
            highest_quantity = shoe.get_quantity()
            highest_quantity_shoe = shoe

    print(f"\nThe shoe with the highest quantity is: {highest_quantity_shoe}\n")


# menu
while True:
    print("1. Read shoes data")
    print("2. Capture shoes")
    print("3. View all")
    print("4. Re-stock")
    print("5. Search shoe")
    print("6. Value per item")
    print("7. Highest quantity")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Goodbye! 👋")
        break
    # error handling for if the user enters doesn't enter one of the menu option's numbers
    else:
        print("\n🔴 Invalid input. Try again.\n")

"""
References:
https://pypi.org/project/tabulate/
"""
