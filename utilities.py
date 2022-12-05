from random import randint


class Creatnumbers:
    """Under this class powerball numbers and users lucky number will be created inside create method.
    After each digit are created it will be appended to each empty lists accordingly"""
    def __init__(self):
        self.userwhiteball = []
        self.todayswhiteball = []
        self.userpowerball = []
        self.todayspowerball = []
        self.intersections = set()

    def create(self):
        for i in range(5):
            usernum = randint(1, 20)
            self.userwhiteball.append(usernum)
            todaynum = randint(1, 20)
            self.todayswhiteball.append(todaynum)
        luckypowerball = randint(1, 10)
        todaypowerball = randint(1, 10)
        self.userpowerball.append(luckypowerball)
        self.todayspowerball.append(todaypowerball)




