import csv
class Contact:
    def __init__(self, name, phone_number):
        if phone_number.isdigit():
            self.name = name
            self.phone_number = phone_number
        else:
            raise ValueError("the phone number must contain only digits!")


class PhoneBook:
    def __init__(self):
        self.contact=[]

    def add_contact(self, name, phone):
        c = Contact(name, phone)
        self.contact.append(c)

    def save_to_csv(self,filename):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "phone_number"])
                for c in self.contact:
                    writer.writerow([c.name, c.phone_number])
            print("the information has been saved.")
        except PermissionError:
            print("file permission error!")
    def load_from_csv(self,filename):
        try:
            with open (filename,"r",encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        c=Contact(row["name"],row["phone_number"])
                        self.contact.append(c)
                    except ValueError:
                        pass
        except FileNotFoundError:
            print("not phone book found!.creat a new one.")
            
# ------------------ MENU ------------------

phonebook = PhoneBook()
phonebook.load_from_csv("Contact.csv")

while True:
    try:
        p = int(input("enter 1(add) / 2(show) / 3(save & exit): "))
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
        if not phonebook.contact:
            print("no contacts available.")
        else:
            for c in phonebook.contact:
                print(c.name, "-", c.phone_number)

    elif p == 3:
        phonebook.save_to_csv("Contact.csv")
        break
    else:
        print("please enter 1, 2 or 3.")
