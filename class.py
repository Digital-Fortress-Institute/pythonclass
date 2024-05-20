# class Car:
#     def __init__(self, brand, name):
#         self.name = name
#         self.brand= brand
    

#     def tunde(self):
#         return f'The name of my Car is {self.name} and the brand is {self.brand}'

# class Phone:
#     def __init__(self, brand, name):
#         self.name = name
#         self.brand= brand
#     def tunde(self):
#         return f'The name of my phone is {self.name} and the brand is {self.brand}'

# class School:
#     def __init__(self, brand, name):
#         self.name = name
#         self.brand= brand
#     def tunde(self):
#         return f'The name of my school is {self.name} and it is rocognise as the {self.brand}'

# import tunde 

# mycar= tunde.Car("toyota", "camary")
# myphone = tunde.Phone("samsung", "Fold") 
# myschool = tunde.School("Unilag", "First Choice")
# # print(mycar.tunde())
# for glory in (mycar, myphone, myschool):
#     print(glory.tunde())



# class Hotel1:
#     def __init__(self, name, location, capacity, country, state):
#         self.name=name
#         self.location= location
#         self.capicity= capacity
#         self.country = country
#         self.state = state
#     def glory(self):
#         return f"{self.name} {self.location} {self.capicity} {self.country} {self.state}"
# class Hotel2:
#     def __init__(self, name, location, capacity, country, state):
#         self.name=name
#         self.location= location
#         self.capicity= capacity
#         self.country = country
#         self.state = state
#     def glory(self):
#         return f"{self.name} {self.location} {self.capicity} {self.country} {self.state}"
# class Hotel3:
#     def __init__(self, name, location, capacity, country, state):
#         self.name=name
#         self.location= location
#         self.capicity= capacity
#         self.country = country
#         self.state = state
#     def glory(self):
#         return f"{self.name} {self.location} {self.capicity} {self.country} {self.state}"


# myHotel1 = Hotel1("Blue", "Ikeja", 140000, "Nigeria", "lagos")
# myHotel2 = Hotel2("Raddison", "Comasin", 13000, "Ghana", "Accra")
# myHotel3 = Hotel3("Eko", "Newyork", 120, "USA", "Washinton Dc")

# for i in (myHotel1, myHotel2, myHotel3):
#     print(i.glory())


# x = 20
# def myname():
#     tunde = 10
#     global x
 
#     def mutunde():
#         y = 15
#         print(tunde + x + y)
#     mutunde()
# myname()

# import tunde
# tunde.mysum(10, 20)

# x = tunde.employee["email"]
# print(x)

# import math

# x = abs(10.5)
# print(x)

# x= math.ceil(4.5)
# y = math.floor(4.5)
# print(x)
# print(y)

# x = math.sqrt(100)
# x = math.pi
# print(x)
# print(x)

# import random
# x = random.randint(1000000000, 100000000000)
# print(x)



# import datetime

# x = datetime.datetime.now()
# print(x.year)
# print(x.day)
# print(x.ctime())
# print(x.strftime("%B"))

import random
# lowwer_bound=1
# upper_bound =5
# guess_count =0
# guess_limit =3
# my_secret_number=3
# while guess_count < guess_limit:
#     guess = input(random.randint(lowwer_bound, upper_bound))
#     guess_count += 1
#     if guess == my_secret_number:
#         print("you won !")
#     else:
#         print("Try again")
#     break


# def guessing_game():
#     secret_number= random.randint(0, 5)
#     print(secret_number)
#     my_name=input("Plese Enter your Name: \n")
  
#     print(f" Mr/Mrs/Miss {my_name} Welcome to Baba Ijebu Enter price betting platform")
#     attempt = 0
#     while True:
#         guess =int(input("Enter your guess number   \n"))
#         attempt += 1
#         if guess > secret_number:
#             print("your guess is high so please try again")
#         elif guess < secret_number:
#             print("your guess is low so please try again")
#         else:
#             print(f"Congratulations! You have just won {secret_number}  {attempt}")
#         break
        
# guessing_game()
# pin = 1234
# card_number = 4213451234442781


# class Atm:
#     def __init__(self, name,   balance=0):
#         self.balance = balance
#         self.name = name
#         # self.pin = pin
#         # self.card_number = card_number
#     def __str__(self):
#         return f"Mr/Mrs/Miss {self.name} your curent balance is {self.balance}"
  
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return 'insufficient fund'
#         else:
#             self.balance -= amount
#             return f"withdrawl successful and current balalce is: {self.balance}"
    
#     def deposite(self, amount):
#         self.balance += amount
#         return f"Deposite successfull your current balance is: {self.balance}"
    

    
# print("welcome to Digital Fortress Micro Finance Bank")
# myname = input("Please Enter your name")
# info= int(input("Please Enter Card number"))
# if info == card_number:
#     print(f"Welcome {myname} \n")
# else:
#     print("Card does not exit")
#     exit()

# user_pin= int(input("Please Enter four digit pin: \n"))
# if user_pin == pin:
#     print("welcome ")
# else:
#     print("Incorrect pin ")
#     exit()
# # welcome_message = input("Please Enter your name")

# user = Atm(myname)

# while True:
#     choice = input("""
#         what will you like to do?
#         press 1 for deposite
#         press 2 for Withdrawl
#         press 3 to check balance
#         press 4 to exit   \n

#         """)
#     if choice == '3':
#         print(user)
#     elif choice == '1':
#         amount=int(input("Enter your deposite amount"))
#         if amount <=0:
#             print("invalidn Transaction")
#         else:
#             print(user.deposite(amount))
#     elif choice == '2':
#         amount=int(input("Enter your withdrawl amount"))
#         if amount <=0:
#             print("invalidn Transaction")
#         else:
#             print(user.withdraw(amount))
#     if choice == "4":
#         print(f"Mr/Miss/ Mrs {myname} thank you for banking with us")
#         break

# tunde = {10, 20, 10, 30, 40, 30}
# print(tunde)


# def duplicate(x):
#     name =input("Enter some charater")
#     x= name.lower()
#     name = set()
#     tunde = []
#     # tunde.append(name)
#     # for name1 in name:
#     #     if name1 not in tunde:
#     #         print(tunde)

#     for i in x:
        
#         if i not in name:
#             name.add(i)
#             tunde.append(i)
#     return tunde
          
# print(duplicate(''))
#     return tunde
# print(duplicate('HetbertyMacualyUniversity'))
# def addition(x, y):
#     return x + y

# def subtraction(x,y):
#     return x - y

# def multiplication(x, y):
#     return x  * y

# def addition(x, y):
#     return x  + y

# def division(x,y):
#     return x / y 

# num1 = int(input("Enter your first number  \n"))
# num2 = int(input('Enter your second number   \n'))

# while True:
#     choice =int(
#          input('''
#     1 is for addition
#     2 is for subtraction
#     3 is for multiplication
#     4 is for division
#     5 is to quit

#     ''')
#     )

#     if choice == 1:
#         print(addition(num1, num2))
#     elif choice == 2:
#         print(subtraction(num1, num2))

#     elif choice == 3:
#         print(multiplication(num1, num2))

#     elif choice == 4:
#         print(division(num1, num2))
#     elif choice == 5:
#         print('thanks for using my caculator')
#         exit()
#     else:
#         print('Invalid request')
#         exit()
#     break

     














# myvar=[10, 20, 30, ['digital','software', ['tech', ['class', 'Akowonjo']],'analysis', ['training', 100, 'frontend'], ['backend', ['fullstack']]]]
# # print(myvar[3][3][2])
# print(myvar[3][2][1][1])


# myclass= [
#     {
#         'name':'Lola',
#         'state':'ogun',
#         'country':'Nigeria',
#         'occupation': 'Engineer',
#         'lga':'Eti-Osa'

#     },
#      {
#         'name':'Lola',
#         'state':'ogun',
#         'country':'Nigeria',
#         'occupation': 'Engineer',
#         'lga':'Eti-Osa'

#     },
#      {
#         'name':'John',
#         'state':'New york',
#         'country':'Usa',
#         'occupation': ['Engineer', 'Business', 'DevOps'],
#         'lga':'Eti-Osa'

#     },
#      {
#         'name':'Tolu',
#         'state':'ogun',
#         'country':'Nigeria',
#         'occupation': 'Engineer',
#         'lga':'Eti-Osa'

#     },
# ]
# print(myclass[2]['occupation'][2])
# from tkinter import *
# from tkinter import simpledialog

# def display():
#     root = Tk()
#     root.title("My display")

#     label = Label(root, text='Hello Tkinter')
#     label.pack()

#     root.mainloop()
# display()

# def mydisplay():

#     root=Tk()
#     root.title('Message Box')

#     def mymessage():
#         name = simpledialog.askstring("Name", "Please Enter your name")
#         if name:
#             mygreeting.config(text=f'Hello, {name}' )
#     root.after(0, mymessage)
#     mygreeting = Label(root, text='')
#     mygreeting.pack(pady=20)
#     root.mainloop()
# mydisplay()


# def mysum():
#     root=Tk()
#     root.title("Our Sum Caculator")

#     def mytwonumbers():
#         try:
#             num1=float(entry1.get())
#             num2 = float(entry2.get())
#             mylabel.config(text=f'Sum: {num1} + {num2} = {num1 + num2} ')
#             print(mylabel)
#         except ValueError:
#             mylabel.config(text='Please Enter a valid number')
        
    
#     entry1 = Entry(root)
#     entry1.pack()

#     entry2 = Entry(root)
#     entry2.pack()
#     mylabel = Label(root, text='')
#     mylabel.pack()

#     myplus = Button(root, text='Add', command=mytwonumbers)
#     myplus.pack(pady=5)
#     root.mainloop()
# mysum()



# def myadd(x , y):
#     try:
#         return(kx + y)
#     except TypeError:
#         return ('Strings can not be evaluated')
#     except NameError:
#         return ("Invalid Parameter")
# print(myadd(20, 30))
# print(myadd('a', 30))
# print(myadd(20, 30))
# print('Success')
# print('Application Running End Here')




# import tkinter as tk


# def mydrawing():
#     root=tk.Tk()
#     root.title("My Canva")
#     mycanvabox = tk.Canvas(root, bg='white', width=500, height=500)
#     mycanvabox.pack()

#     x, y = None, None

#     def mybuttondrag(e):
#         x, y 
#         x, y =e.x, e.y



#     click.bind('<ButtonPress-1>', on_click_button)

#     root.mainloop()

# mydrawing()