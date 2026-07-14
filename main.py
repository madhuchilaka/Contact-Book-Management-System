# ============================================
# MAIN PROGRAM
# ============================================

from colorama import init

from ui import (
    welcome_screen,
    display_menu,
    exit_message
)

from file_manager import (
    load_contacts,
    export_contacts,
    import_contacts
)

from contact_manager import (
    add_contact,
    search_contact,
    update_contact,
    delete_contact,
    view_contacts
)

init(autoreset=True)


def main():

    contacts = load_contacts()

    welcome_screen()

    while True:

        display_menu()

        choice = input("Enter your choice : ").strip()

        if choice == "1":

            contacts = add_contact(contacts)

        elif choice == "2":

            contacts = search_contact(contacts)

        elif choice == "3":

            contacts = update_contact(contacts)

        elif choice == "4":

            contacts = delete_contact(contacts)

        elif choice == "5":

            view_contacts(contacts)

        elif choice == "6":

            export_contacts(contacts)

        elif choice == "7":

            contacts = import_contacts()

        elif choice == "8":

            exit_message()
            break

        else:

            print("\n❌ Invalid Choice!")


if __name__ == "__main__":
    main()