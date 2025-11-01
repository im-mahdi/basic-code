class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=float(price)
    def display_details(self):
        print(f"Titel of book : {self.title}")
        print(f"Author of book : {self.author}")
        print(f"Price of book : {self.price}$\n\n")
    def apply_discount(self,percent):
        discount_amount = self.price * (percent/100)
        self.price -= discount_amount
#        print(f"discount {percent}% actived. and the new price: {self.price}")

title=input("please enter a (Title) of first Book : ")
author=input("please enter a (Author) of first Book : ")
price=input("please enter a (Price) of first Book : ")

Book1=Book(title,author,price)


title1=input("please enter a (Title) of second Book : ")
author1=input("please enter a (Author) of second Book : ")
price1=input("please enter a (Price) of second Book : ")

Book2=Book(title1,author1,price1)

print("Before change the prices :")
Book1.display_details()
Book2.display_details()

Book1.apply_discount(10)
Book2.apply_discount(10)

print("After change the prices :")
Book1.display_details()
Book2.display_details()