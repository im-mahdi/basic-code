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
    
    def remove_contact(self, index):
        if 0 <= index < len(self.contact):
            self.contact.pop(index)

    def save_to_csv(self,filename = "contacts.csv"):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "phone_number"])
                for c in self.contact:
                    writer.writerow([c.name, c.phone_number])
            print("the information has been saved.")
        except PermissionError:
            print("file permission error!")
    def load_from_csv(self,filename = "contacts.csv"):
        self.contact = []
        try:
            with open (filename,"r",encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    try:
                        self.add_contact(row[0], row[1])
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("not phone book found!.creat a new one.")
            