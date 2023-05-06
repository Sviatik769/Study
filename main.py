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

    def get_house(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shoping('food')
        else:
            if self.satiety >= 100
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20
                self.shoping('fuel')
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shoping(self, manage):
        #      --------------Here-----------------
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I bought delicacies')
            self.money -= 15
            self.gladness += 10
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strangth += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"fuel - {self.car.fuel}")
        print(f"strangth - {self.car.strangth}")


#      --------------Here-----------------


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
brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
    'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']