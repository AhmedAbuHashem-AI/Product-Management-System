# =================================================================
# Product Management System
# A simple console-based application to manage a list of products
# with features: CRUD, reporting, sorting, and advanced queries.
# =================================================================

def read_products():
    """" Read products from 'products.txt' and return list of (name, price)."""
    products = []
    try:
        with open("products.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                price = int(data[1])
                products.append((name, price))
    except FileNotFoundError:
        print("File not found.")
    return products


def write_products(products):
    """"Write list of products to 'products.txt'."""
    with open("products.txt", "w") as file:
        for name, price in products:
            file.write(name + "," + str(price) + "\n")


def show_products():
    products = read_products()
    print("\nProducts List:")
    for name, price in products:
        print(name, price)


def add_product():
    name = input("Enter product name:")
    try:
        price = int(input("Enter product price:"))
    except:
        print("Invalid price")
        return
    with open("products.txt", "a") as file:
        file.write(name + "," + str(price) + "\n")
    print("Product added.")


def delete_product():
    products = read_products()
    delete_name = input("Enter product name to delete:")
    new_products = []
    found = False
    for name, price in products:
        if name.lower() != delete_name.lower():
            new_products.append((name, price))
        else:
            found = True
    write_products(new_products)
    if found:
        print("Product deleted.")
    else:
        print("Product not found.")


def update_product():
    products = read_products()
    update_name = input("Enter product name to update:")
    try:
        new_price = int(input("Enter product new price:"))
    except:
        print("Invalid price.")
        return
    found = False
    for i in range(len(products)):
        name, price = products[i]
        if name.lower() == update_name.lower():
            products[i] = (name, new_price)
            found = True
    write_products(products)
    if found:
        print("Product updated.")
    else:
        print("Product not found.")


def create_report():
    """" Generate statistics report and save to 'report.txt'."""
    products = read_products()
    total = 0
    for name, price in products:
        total += price
    count = len(products)
    if count == 0:
        print("No products.")
        return
    average = total / count
    expensive = 0
    for name, price in products:
        if price > 1800:
            expensive += 1
    max_product = max(products, key=lambda x: x[1])
    min_product = min(products, key=lambda x: x[1])

    with open("report.txt", "w") as file:
        file.write("Number of products:" + str(count) + "\n")
        file.write("Total price:" + str(total) + "\n")
        file.write("Average price:" + str(average) + "\n")
        file.write("Most expensive:" + max_product[0] + "\n")
        file.write("Cheapest:" + min_product[0] + "\n")
        file.write("Expensive products count:" + str(expensive) + "\n")
    print("Report created in 'report.txt'.")


def search_product():
    products = read_products()
    search_name = input("Enter product name:")
    found = False
    for name, price in products:
        if name.lower() == search_name.lower():
            print("Found:", name, price)
            found = True
    if not found:
        print("Product not found.")


def report_advanced():
    """"Advanced report: search + top 3 expensive + top 3 cheapest."""
    search_name = input("Enter product name to search:")
    products = read_products()
    if not products:
        print("No products found.")
        return
    found = False
    with open("advanced_report.txt", "w") as file:
        file.write("=== SEARCH RESULT ===\n")
        for name, price in products:
            if name.lower() == search_name.lower():
                file.write(name + "," + str(price) + "\n")
                found = True
        if not found:
            file.write("Product not found\n")

        # Sort descending for top expensive
        products.sort(key=lambda x: x[1], reverse=True)
        file.write("\n=== TOP 3 EXPENSIVE ===\n")
        for name, price in products[:3]:
            file.write(name + "," + str(price) + "\n")

        # Sort ascending for cheapest
        products.sort(key=lambda x: x[1])
        file.write("\n=== TOP 3 CHEAPEST ===\n")
        for name, price in products[:3]:
            file.write(name + "," + str(price) + "\n")
    print("Advanced report saved to 'Advanced_report.txt'.")


def sort_products():
    """"Sort products ascending ( cheapest first) and save back to original file."""
    products = read_products()
    products.sort(key=lambda x: x[1])
    write_products(products)
    print("Products sorted from cheapest to most expensive and saved.")


def sort_ascending_file():
    """"Save sorted ascending list to 'sorted_asc.txt' without changing original."""
    products = read_products()
    products.sort(key=lambda x: x[1])
    with open("sorted_asc.txt", "w") as file:
        for name, price in products:
            file.write(name + "," + str(price) + "\n")
    print("Sorted ascending saved to 'sorted_asc.txt'.")


def sort_descending_file():
    """"Save sorted descending list to 'sorted-desc.txt' without changing original."""
    products = read_products()
    products.sort(key=lambda x: x[1], reverse=True)
    with open("sorted_desc.txt", "w") as file:
        for name, price in products:
            file.write(name + "," + str(price) + "\n")
    print("Sorted descending saved to 'sorted_desc.txt'.")


def top_3_expensive():
    products = read_products()
    products.sort(key=lambda x: x[1], reverse=True)
    print("Top 3 expensive products:")
    for product in products[:3]:
        print(product)


def top_3_cheapest():
    products = read_products()
    products.sort(key=lambda x: x[1])
    print("Top 3 cheapest products:")
    for product in products[:3]:
        print(product)


def sum_top_3():
    products = read_products()
    products.sort(key=lambda x: x[1], reverse=True)
    total = 0
    for name, price in products[:3]:
        total += price
    print("Sum of top 3 expensive products:" , total)


def main():
    while True:
        print("\nMenu")
        print("1- Show products")
        print("2- Add product")
        print("3- Delette product")
        print("4- Update product")
        print("5- Create report (statistrics)")
        print("6- Search product")
        print("7- Sort products (save to file)")
        print("8- Top 3 expensive")
        print("9- Top 3 cheapest")
        print("10- Sum top 3 expensive")
        print("11- Advanced report (search + top lists)")
        print("12- Save sorted ascending to file")
        print("13- Save sorted descending to file")
        print("0- Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            create_report()
        elif choice == "6":
            search_product()
        elif choice == "7":
            sort_products()
        elif choice == "8":
            top_3_expensive()
        elif choice == "9":
            top_3_cheapest()
        elif choice == "10":
            sum_top_3()
        elif choice == "11":
            report_advanced()
        elif choice == "12":
            sort_ascending_file()
        elif choice == "13":
            sort_descending_file()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()