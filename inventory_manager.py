# Name: MI ASJATH AHAMED
# Roll Number: iitp_aimltn_2602113 
# Assignment: Working with Files and JSON in Python

import json
import os

filename = "inventory.json"

# Starter inventory (will be created automatically if file doesn't exist)
starter_inventory = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
    {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
]

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# -------------------------------
# STEP 1: Create file if not exists
# -------------------------------
if not os.path.exists(filename):
    with open(filename, "w") as file:
        json.dump(starter_inventory, file, indent=4)

# -------------------------------
# STEP 2: Read the inventory
# -------------------------------
with open(filename, "r") as file:
    inventory = json.load(file)

print("Total number of books:", len(inventory))

# -------------------------------
# STEP 3: Append new book
# -------------------------------
inventory.append(new_book)

# -------------------------------
# STEP 4: Save updated inventory
# -------------------------------
with open(filename, "w") as file:
    json.dump(inventory, file, indent=4)

# -------------------------------
# STEP 5: Display inventory
# -------------------------------
with open(filename, "r") as file:
    updated_inventory = json.load(file)

print("\nUpdated Inventory:\n")

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
