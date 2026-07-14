# ============================================
# CONTACT MANAGER
# ============================================

from validator import (
    is_valid_phone,
    is_valid_email,
    phone_exists
)

from file_manager import save_contacts

from tabulate import tabulate
from colorama import Fore


def add_contact(contacts):

    print("\n------ Add Contact ------")

    name = input("Enter Name : ").strip()

    if name in contacts:
        print(Fore.RED + "❌ Contact already exists!")
        return contacts

    while True:

        phone = input("Enter Phone Number : ").strip()

        if not is_valid_phone(phone):
            print(Fore.RED + "❌ Invalid phone number!")
            continue

        if phone_exists(phone, contacts):
            print(Fore.RED + "❌ Phone number already exists!")
            continue

        break

    while True:

        email = input("Enter Email : ").strip()

        if not is_valid_email(email):
            print(Fore.RED + "❌ Invalid email!")
            continue

        break

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    save_contacts(contacts)

    print(Fore.GREEN + f"\n✅ {name} added successfully!")

    return contacts


def search_contact(contacts):

    print("\n------ Search Contact ------")
    print("1. Search by Name")
    print("2. Search by Phone Number")

    choice = input("Enter your choice : ")

    if choice == "1":

        name = input("Enter Name : ").strip()

        if name in contacts:

            print("\nContact Found!")
            print("----------------------------")
            print("Name  :", name)
            print("Phone :", contacts[name]["Phone"])
            print("Email :", contacts[name]["Email"])

        else:
            print(Fore.RED + "\n❌ Contact not found!")

    elif choice == "2":

        phone = input("Enter Phone Number : ").strip()

        found = False

        for name, details in contacts.items():

            if details["Phone"] == phone:

                print("\nContact Found!")
                print("----------------------------")
                print("Name  :", name)
                print("Phone :", details["Phone"])
                print("Email :", details["Email"])

                found = True
                break

        if not found:
            print(Fore.RED + "\n❌ Contact not found!")

    else:
        print(Fore.RED + "\n❌ Invalid Choice!")

    return contacts


def update_contact(contacts):

    print("\n------ Update Contact ------")

    name = input("Enter Name to Update : ").strip()

    if name not in contacts:
        print(Fore.RED + "\n❌ Contact not found!")
        return contacts

    print("\nCurrent Details")
    print("----------------------------")
    print("Phone :", contacts[name]["Phone"])
    print("Email :", contacts[name]["Email"])

    print("\n1. Update Phone")
    print("2. Update Email")
    print("3. Update Both")

    choice = input("Enter Choice : ")

    if choice == "1":

        while True:

            phone = input("Enter New Phone : ").strip()

            if not is_valid_phone(phone):
                print(Fore.RED + "❌ Invalid Phone!")
                continue

            if phone != contacts[name]["Phone"] and phone_exists(phone, contacts):
                print(Fore.RED + "❌ Phone already exists!")
                continue

            contacts[name]["Phone"] = phone
            break

    elif choice == "2":

        while True:

            email = input("Enter New Email : ").strip()

            if not is_valid_email(email):
                print(Fore.RED + "❌ Invalid Email!")
                continue

            contacts[name]["Email"] = email
            break

    elif choice == "3":

        while True:

            phone = input("Enter New Phone : ").strip()

            if not is_valid_phone(phone):
                print(Fore.RED + "❌ Invalid Phone!")
                continue

            if phone != contacts[name]["Phone"] and phone_exists(phone, contacts):
                print(Fore.RED + "❌ Phone already exists!")
                continue

            break

        while True:

            email = input("Enter New Email : ").strip()

            if not is_valid_email(email):
                print(Fore.RED + "❌ Invalid Email!")
                continue

            break

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email

    else:
        print(Fore.RED + "\n❌ Invalid Choice!")
        return contacts

    save_contacts(contacts)

    print(Fore.GREEN + "\n✅ Contact Updated Successfully!")

    return contacts


def delete_contact(contacts):

    print("\n------ Delete Contact ------")

    name = input("Enter Name : ").strip()

    if name in contacts:

        confirm = input(
            f"Are you sure you want to delete {name}? (Y/N): "
        ).upper()

        if confirm == "Y":

            del contacts[name]

            save_contacts(contacts)

            print(Fore.GREEN + "\n✅ Contact Deleted Successfully!")

        else:

            print("\nDeletion Cancelled.")

    else:

        print(Fore.RED + "\n❌ Contact not found!")

    return contacts


def view_contacts(contacts):

    if not contacts:

        print(Fore.RED + "\n❌ No contacts available.")
        return

    table = []

    for i, (name, details) in enumerate(
            sorted(contacts.items()), start=1):

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