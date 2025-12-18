import csv

contact = []  


class Contact:
    def __init__(self, name, phone_number):
        if phone_number.isdigit():
            self.name = name
            self.phone_number = phone_number
        else:
            raise ValueError("the phone number must contain only digits!")


class PhoneBook:
    def add_contact(self, name, phone):
        c = Contact(name, phone)
        contact.append(c)


phonebook = PhoneBook()

# ------------------ MENU ------------------
while True:
    try:
        p = int(input(
            "enter 1(add) / 2(show) / 3(save & exit): "
        ))
    except ValueError:
        print("please enter a number!")
        continue

    if p == 1:
        name = input("please input a name: ")
        phone = input("please enter phone number: ")

        try:
            phonebook.add_contact(name, phone)
            print("contact added successfully.")
        except ValueError as e:
            print(e)

    elif p == 2:
        if not contact:
            print("no contacts available.")
        else:
            for c in contact:
                print(c.name, "-", c.phone_number)

    elif p == 3:
        try:
            with open("Contact.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "phone_number"])
                for c in contact:
                    writer.writerow([c.name, c.phone_number])
            print("the information has been saved.")
        except PermissionError:
            print("file permission error!")

        break

    else:
        print("please enter 1, 2 or 3.")
