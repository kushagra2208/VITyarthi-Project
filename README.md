 Store Inventory and Stock Management System

A small command-line program, written in Python, that lets a store employee log in and check how much stock the store has in each product category. It is a read-only viewer: it shows what is in stock, its price and its quantity, but it doesn't change anything.

I built it as my project for the VITyarthi *Build Your Own Project* course at VIT Bhopal.

 What it does

1. Asks for an employee name and password.
2. Checks them against a text file of saved credentials. If they don't match, it says "Access denied" and stops.
3. If they match, it greets you by name and shows a menu with four categories (groceries, electronics, clothes, sports equipments) and an exit option.
4. Prints every item in the category you pick: name, price per unit and quantity in stock.
5. Asks whether you want to check another category (`C`) or leave (`E`).

If you type something that isn't on the menu, it tells you and shows the menu again instead of crashing.

 Running it

You need Python 3 installed. That's all; the program uses no extra libraries.

1. Download or clone this repository.
2. Keep `Code.py` and all the `.txt` files in the **same folder**. The program opens them by name, so it has to be run from that folder.
3. Open a terminal in that folder and run:


python Code.py


 The data files

All the data lives in plain text files, one record per line, with the fields separated by commas. You can open them in Notepad and edit them, no code changes needed.

| File | Each line looks like |
|---|---|
| `Credentials.txt` | `username,password` |
| `Groceries.txt` | `item name,quantity,price` |
| `Electronics.txt` | `item name,quantity,price` |
| `Clothes.txt` | `item name,quantity,price` |
| `Sports Equipments.txt` | `item name,quantity,price` |

Example, from `Clothes.txt`:


Cotton T-shirt,60,499
Denim Jeans,35,2499
Winter Jacket,18,2999
Cotton Shirts,22,1999


Example, from `Credentials.txt` (this is demo data, use your own):


Rahul,pass123


Things to watch out for when editing these files:

- The order matters. Stock lines are always name, then quantity, then price.
- The quantity has to be a whole number.
- Don't leave blank lines in the middle or at the end of a file (see the limitations below).
- File names are spelled exactly as in the table, including `Sports Equipments.txt` with the extra "s". On Linux and macOS, capital letters matter in file names too.

 A sample run


=======================================================
      STORE INVENTORY AND STOCK MANAGEMENT SYSTEM
=======================================================
Enter employee name: Rahul
Enter your password: pass123
Login Successful! Welcome Rahul
-----------------------------------
       SELECT DESIRED ACTION
-----------------------------------
1. Check groceries stock
2. Check electronics stock
3. Check clothes stock
4. Check sports equipments stock
5. Exit System
Enter option (1-5): 3

=== CLOTHES STOCK LIST ===
Name of item: Cotton T-shirt
Price per unit: 499
Available quantity in stock: 60

Name of item: Denim Jeans
Price per unit: 2499
Available quantity in stock: 35



To check stock of other products enter 'C' or To exit enter 'E': E
Logged out...Thank You for using our stock management system


 How the code works

The whole program is in `Code.py`, about 80 lines, in three parts.

**Login.** The program opens `Credentials.txt` and goes through it line by line. Each line is stripped of its newline and split at the comma into a username and a password. The name you typed is compared with the saved one after both are converted to lowercase, so `rahul`, `Rahul` and `RAHUL` all work. The password is compared exactly, so capital letters count there. When a match is found, a flag called `auth` is set to `True` and the loop stops.

**Menu loop.** If `auth` is `True`, a `while True` loop shows the menu and reads your choice. An `if / elif` chain turns the number into two variables: which file to open (`category_filename`) and what to call the category in the heading (`category_name`). Choosing `5` prints the goodbye message and breaks out of the loop. Anything else prints an error and uses `continue` to go back to the top of the loop.

**Showing stock.** One block of code handles all four categories. It opens whichever file was selected, splits each line into name, quantity and price, and prints them. Because the four menu options only choose a file name, I didn't have to write the printing code four times.

If the login failed, none of the menu code runs. It just prints "Invalid credentials" and "Access denied".

 Known limitations

I tested the error paths and found some things that need fixing. They only show up when the data files are wrong, not when the user types something odd:

- If a stock file or `Credentials.txt` is missing, the program stops with a `FileNotFoundError`.
- If a quantity isn't a number (for example `abc`), it stops with a `ValueError`.
- If there is a blank line in a data file, it stops with an `IndexError`.
- Passwords are stored as plain text and shown on screen while you type them. That's fine for a learning project but not for a real store.
- The name comparison doesn't trim spaces, so `" Rahul"` (with a leading space) is rejected.
- The blank line between items comes from `print("" * 35)`, which prints an empty line. It isn't a dashed separator.

 Things I'd like to add

- `try / except` around the file reading so a bad file gives a clear message instead of a crash.
- Adding, selling and updating stock from inside the program and saving it back to the files.
- A warning when an item's quantity is low.
- Searching for an item across all categories.
- Hiding the password as it's typed (Python's `getpass` module) and limiting login attempts.
- Putting the code into functions and replacing the `if / elif` chain with a dictionary, so adding a category is one line.

 Project details

- **Author:** Kushagra Shukla (26BCE11637)
- **Programme:** B.Tech CSE (Core), VIT Bhopal University
- **Guide:** Prof. Dr. Dheresh Soni
- **Built with:** Python 3 (developed on 3.14), written in Visual Studio Code
