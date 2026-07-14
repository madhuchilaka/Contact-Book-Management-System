# ============================================
# USER INTERFACE
# ============================================

from colorama import Fore, Style, init

init(autoreset=True)


def welcome_screen():

    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "        📒 CONTACT BOOK MANAGEMENT SYSTEM")
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "Developed By : CH MADHU BABU")
    print(Fore.GREEN + "Version      : 1.0")
    print(Fore.CYAN + "=" * 50)


def display_menu():

    print()
    print(Fore.CYAN + "=" * 45)
    print(Fore.YELLOW + "           📒 CONTACT BOOK")
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


def exit_message():

    print()
    print(Fore.GREEN + "Thank you for using Contact Book ❤️")
    print(Fore.CYAN + "=" * 45)