contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact Added!")

    elif choice == "2":
        for contact in contacts:
            print(contact["name"], "-", contact["phone"])

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")