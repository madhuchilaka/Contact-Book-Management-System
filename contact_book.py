# ============================================
# IMPORTS
# ============================================

import json
import os
import csv
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

# ============================================
# GLOBAL VARIABLES
# ============================================

contacts = {}

# ============================================
# VALIDATION FUNCTIONS
# ============================================

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    return "@" in email and "." in email

def phone_exists(phone):
    for details in contacts.values():
        if details["Phone"] == phone:
            return True
    return False

# ============================================
# CONTACT OPERATIONS
# ============================================

def add_contact():

    print("\n------ Add Contact ------")

    name = input("Enter Name : ").strip()

    if name in contacts:
        print("❌ Contact already exists!")
        return

    # Phone Validation
    while True:

        phone = input("Enter Phone Number : ").strip()

        if not is_valid_phone(phone):
            print("❌ Invalid phone number! Enter exactly 10 digits.")
            continue

        if phone_exists(phone):
            print("❌ Phone number already exists!")
            continue

        break

    # Email Validation
    while True:

        email = input("Enter Email : ").strip()

        if not is_valid_email(email):
            print("❌ Invalid email address!")
            continue

        break

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    save_contacts()

    print(Fore.GREEN + f"✅ {name} added successfully!")
    

def search_contact():


    print("\n------ Search Contact ------")
    print("1. Search by Name")
    print("2. Search by Phone Number")


    choice = input("Enter your choice: ").strip()

    if choice == "1":

        name = input("Enter Name: ").strip()

        if name in contacts:

            print("\nContact Found!")
            print("-------------------------")
            print("Name  :", name)
            print("Phone :", contacts[name]["Phone"])
            print("Email :", contacts[name]["Email"])
            print("-------------------------")

        else:
            print("\n❌ Contact not found!")

    elif choice == "2":

        phone = input("Enter Phone Number: ").strip()

        found = False

        for name, details in contacts.items():

            if details["Phone"] == phone:

                print("\nContact Found!")
                print("-------------------------")
                print("Name  :", name)
                print("Phone :", details["Phone"])
                print("Email :", details["Email"])
                print("-------------------------")

                found = True
                break

        if not found:
            print(Fore.RED + "❌ Contact not found!")

    else:
        print("\n❌ Invalid Choice!")

def update_contact():

    print("\n------ Update Contact ------")

    name = input("Enter Name to Update : ").strip()

    if name not in contacts:
        print("\n❌ Contact not found!")
        return

    print("\nCurrent Details")
    print("----------------------------")
    print("Phone :", contacts[name]["Phone"])
    print("Email :", contacts[name]["Email"])

    print("\nWhat do you want to update?")
    print("1. Phone Number")
    print("2. Email Address")
    print("3. Both")

    choice = input("Enter your choice : ").strip()

    # Update Phone
    if choice == "1":

        while True:

            phone = input("Enter New Phone Number : ").strip()

            if not is_valid_phone(phone):
                print("❌ Invalid phone number!")
                continue

            if phone != contacts[name]["Phone"] and phone_exists(phone):
                print("❌ Phone number already exists!")
                continue

            contacts[name]["Phone"] = phone
            break

    # Update Email
    elif choice == "2":

        while True:

            email = input("Enter New Email : ").strip()

            if not is_valid_email(email):
                print("❌ Invalid email!")
                continue

            contacts[name]["Email"] = email
            break

    # Update Both
    elif choice == "3":

        while True:

            phone = input("Enter New Phone Number : ").strip()

            if not is_valid_phone(phone):
                print("❌ Invalid phone number!")
                continue

            if phone != contacts[name]["Phone"] and phone_exists(phone):
                print("❌ Phone number already exists!")
                continue

            break

        while True:

            email = input("Enter New Email : ").strip()

            if not is_valid_email(email):
                print("❌ Invalid email!")
                continue

            break

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email

    else:
        print("\n❌ Invalid Choice!")
        return

    save_contacts()

    print("\n✅ Contact updated successfully!")


def delete_contact():

    print("\n------ Delete Contact ------")

    name = input("Enter Name to Delete : ").strip()

    if name in contacts:

        confirm = input(f"Are you sure you want to delete {name}? (Y/N): ").strip().upper()

        if confirm == "Y":
            del contacts[name]
            print("\nContact deleted successfully!")

            save_contacts()

        else:
            print("\nDeletion cancelled.")

    else:
        print("\nContact not found!")

def view_contacts():

    if not contacts:
        print("\n❌ No contacts available.")
        return

    table = []

    for i, (name, details) in enumerate(sorted(contacts.items()), start=1):

        table.append([
            i,
            name,
            details["Phone"],
            details["Email"]
        ])

    print("\n📒 CONTACT LIST\n")

    print(tabulate(
        table,
        headers=["No", "Name", "Phone", "Email"],
        tablefmt="grid"
    ))

    print(f"\n📊 Total Contacts : {len(contacts)}")

# ============================================
# FILE OPERATIONS
# ============================================

def load_contacts():

    global contacts

    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

    except FileNotFoundError:
        contacts = {}

def save_contacts():

    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)



def export_contacts():

    if not contacts:
        print("\n❌ No contacts available to export.")
        return

    file_path = os.path.join(os.getcwd(), "contacts.csv")

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow(["Name", "Phone", "Email"])

            # Write all contacts
            for name, details in sorted(contacts.items()):

                writer.writerow([
                    name,
                    details["Phone"],
                    details["Email"]
                ])

        print("\n✅ Contacts exported successfully!")
        print(f"📁 File saved at:\n{file_path}")
        print(f"📊 Total Contacts Exported: {len(contacts)}")

    except Exception as e:
        print("\n❌ Error while exporting contacts.")
        print("Error:", e)


def import_contacts():

    global contacts

    try:
        with open("contacts.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                name = row.get("Name", "").strip()
                phone = row.get("Phone", "").strip()
                email = row.get("Email", "").strip()

                if name and phone and email:
                    contacts[name] = {
                        "Phone": phone,
                        "Email": email
                    }

        save_contacts()

        print("\n✅ Contacts imported successfully!")

    except FileNotFoundError:
        print("\n❌ contacts.csv not found!")

# ============================================
# DISPLAY FUNCTIONS
# ============================================

def display_menu():

    print(Fore.CYAN + "=" * 45)
    print(Fore.YELLOW + "          📒 CONTACT BOOK")
    print(Fore.CYAN + "=" * 45)

    print("1. ➕ Add Contact")
    print("2. 🔍 Search Contact")
    print("3. ✏️ Update Contact")
    print("4. ❌ Delete Contact")
    print("5. 📋 View Contacts")
    print("6. 📤 Export Contacts")
    print("7. 📥 Import Contacts")
    print("8. 🚪 Exit")

    print(Fore.CYAN + "=" * 45)

# ============================================
# MAIN PROGRAM
# ============================================

def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            view_contacts()

        elif choice == "6":
            export_contacts()

        elif choice == "7":
            import_contacts()

        elif choice == "8":
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\nInvalid Choice!")

if __name__ == "__main__":
    load_contacts()
    main()