# def mysum(x, y):
#     print(x * y)



# employee= {
#     "name":"Emeka",
#     "gender": "male",
#     "email": "emaka@gmail.com"

# }

class Car:
    def __init__(self, brand, name):
        self.name = name
        self.brand= brand
    

    def tunde(self):
        return f'The name of my Car is {self.name} and the brand is {self.brand}'

class Phone:
    def __init__(self, brand, name):
        self.name = name
        self.brand= brand
    def tunde(self):
        return f'The name of my phone is {self.name} and the brand is {self.brand}'

class School:
    def __init__(self, brand, name):
        self.name = name
        self.brand= brand
    def tunde(self):
        return f'The name of my school is {self.name} and it is rocognise as the {self.brand}'