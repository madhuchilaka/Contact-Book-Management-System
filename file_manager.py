# ============================================
# FILE MANAGER
# ============================================

import json
import csv
import os


def load_contacts():

    try:
        with open("contacts.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_contacts(contacts):

    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def export_contacts(contacts):

    if not contacts:
        print("\n❌ No contacts available to export.")
        return

    file_path = os.path.join(os.getcwd(), "contacts.csv")

    try:

        with open(file_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # Header
            writer.writerow(["Name", "Phone", "Email"])

            # Contact Data
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

    contacts = {}

    try:

        with open("contacts.csv", "r", newline="", encoding="utf-8") as file:

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

        save_contacts(contacts)

        print("\n✅ Contacts imported successfully!")

        return contacts

    except FileNotFoundError:

        print("\n❌ contacts.csv not found!")

        return {}