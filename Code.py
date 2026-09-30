print("=======================================================")
print("      STORE INVENTORY AND STOCK MANAGEMENT SYSTEM      ")
print("=======================================================")

input_user = input("Enter employee name: ")
input_pass = input("Enter your password: ")

auth = False

manager_credentials = open("Credentials.txt")
for line in manager_credentials:
    credentials = line.strip().split(",")
    saved_username = credentials[0]
    saved_password = credentials[1]

    if input_user.lower() == saved_username.lower() and input_pass == saved_password:
                auth = True
                print(f"Login Successful! Welcome {input_user.capitalize()}")
                break   

manager_credentials.close() 
    
if auth:
    while True:
                print("-----------------------------------")
                print("       SELECT DESIRED ACTION       ")
                print("-----------------------------------")
                print("1. Check groceries stock")
                print("2. Check electronics stock")
                print("3. Check clothes stock")
                print("4. Check sports equipments stock")
                print("5. Exit System")

                choice = input("Enter option (1-5): ")
                if choice == "1":
                    category_filename = "Groceries.txt"
                    category_name = "GROCERIES"
                elif choice == "2":
                    category_filename = "Electronics.txt"
                    category_name = "ELECTRONICS"
                elif choice == "3":
                    category_filename = "Clothes.txt"
                    category_name = "CLOTHES"
                elif choice == "4":
                    category_filename = "Sports Equipments.txt"
                    category_name = "SPORTS EQUIPMENTS"
                elif choice == "5":
                    print("-" * 60)
                    print("\nLogged out...Thank You for using our Stock Management System\n")
                    print("-" * 60)
                    break
                else:
                    print("Invalid choice! Please select any action from 1 to 5")
                    continue

                if choice in ["1" , "2" , "3" , "4"]:
                    print(f"\n=== {category_name} STOCK LIST ===")
                    inventory_file = open(category_filename, "r")
                    for line in inventory_file:
                        item_data = line.strip().split(",")
                        item_name = item_data[0]
                        quantity = int(item_data[1])
                        price = item_data[2]
                        print(f"Name of item: {item_name}")
                        print(f"Price per unit: {price}")
                        print(f"Available quantity in stock: {quantity} ")
                        print("" * 35)
                    inventory_file.close()
                    n = input("To check stock of other products enter 'C' or To exit enter 'E': ")
                    if n.lower()=="c":
                         continue
                    elif n.lower()=="e":
                        print("Logged out...Thank You for using our stock management system")
                        break
                    else:
                        print('Invalid command! Closing program')
                        print("Thank you for using our Stock Management System")
                        break
else:
    invalid = ("Invalid credentials")
    print(f"\n{invalid}")
    print("Access denied".center(len(invalid)))