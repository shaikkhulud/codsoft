
contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("-" * 20)
    else:
        print("No contacts found.")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, contact_info in contacts.items():
        if search_term in (name, contact_info['phone']):
            print(f"\nName: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            found = True
    if not found:
        print(f"No contacts found for '{search_term}'.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Current Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        print("-" * 20)

        contacts[name]["phone"] = input("Enter new phone number (or press Enter to keep it unchanged): ")
        contacts[name]["email"] = input("Enter new email (or press Enter to keep it unchanged): ")
        contacts[name]["address"] = input("Enter new address (or press Enter to keep it unchanged): ")

        print("Contact information updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
