def add(contact):
    user = input("Enter contact name: ")
    phone_no = input("Enter contact phone number: ")
    contact[user] = phone_no
    print(f"Contact {user} added.")

def search(contact):
    user = input("Enter contact name to search: ")
    if user in contact:
        print(f"{user}: {contact[user]}")
    else:
        print("Contact not found.")

def delete(contact):
    user = input("Enter contact name to delete: ")
    if user in contact:
        del contact[user]
        print(f"Contact {user} deleted.")
    else:
        print("Contact not found.")

def app():
    contact = {}
    while True:
        print("Phone Book Application")
        print("1. Add Contact")
        print("2. Search Contact By Name")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add(contact)
        elif choice == '2':
            search(contact)
        elif choice == '3':
            delete(contact)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

app()



