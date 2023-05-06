import random


class Human:
    def __init__(self, name='Human', job=None, Home=None, Car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strangth = brand_list[self.brand]['strangth']
        self.consuption = brand_list[self.brand]['consuption']

    def drive(self):
        if self.strangth > 0 and self.fuel >= self.consuption
            self.fuel -= self.consuption
            self.strangth -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    'Java developer': {'salary': 50, 'gladness_less': 10};
    'Pyton developer': {'salary': 40, 'gladness_less': 3};
    'C++ developer': {'salary': 45, 'gladness_less': 25};
    'Rust developer': {'salary': 70, 'gladness_less': 1};
}
brand_of_car = {
    'BMW': {'fuel': 100, 'strangth': 100, 'consuption': 6};
    'Lada': {'fuel': 50, 'strangth': 40, 'consuption': 10};
    'Volvo': {'fuel': 70, 'strangth': 150, 'consuption': 8};
    'BMW': {'fuel': 100, 'strangth': 100, 'consuption': 6};
}