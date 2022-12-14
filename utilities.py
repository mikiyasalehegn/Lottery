from random import randint
import pyodbc
import datetime


class Creatnumbers:
    """Under this class powerball numbers and users lucky number will be created inside create method.
    After each digit are created it will be appended to each empty lists accordingly"""

    def __init__(self):
        self.userwhiteball = []
        self.todayswhiteball = []
        self.userpowerball = []
        self.todayspowerball = []

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


class Backend:
    """This class consists of functions that will keep winners data on the national lottery institute's database"""

    def __init__(self):
        self.Ticket_id = randint(1000, 9999)

    def record(self, p_id, account_num, money: int):
        connect = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                 'Server};SERVER=MIKE;DATABASE=Lotto;Trusted_Connection=yes;')

        cursor = connect.cursor()
        cursor.execute("insert into [Winners] ([Ticket_id],[Personal_id],[Date_time],[Bank_account],[Amount]) "
                       "values(?,?,?,?,?)", (self.Ticket_id, p_id, datetime.datetime.now(), account_num, money))

        cursor.commit()

        cursor.close()
        connect.close()
