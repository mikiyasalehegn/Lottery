
import colors
from show import Show


class Evaluator(Show):
    """In this Class the intersection of user's lucky number(self.userwhiteball) and today's powerball winning
    number(self.todayswhiteball) will be computed in order to create the wining scenarios"""
    def compute(self, intersect):
        if intersect == 5 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have correct White Balls and the Powerball\n you win $324,000,000")
        elif intersect == 5 and self.userpowerball != self.todayspowerball:
            print("Congratulations!\nYou have correct White Balls but not the Powerball\n you win $1,000,000")
        elif intersect == 4 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have 4 correct White Balls and the Powerball\n you win $10,000")
        elif intersect == 4 and self.userpowerball != self.todayspowerball:
            print("Congratulations!\nYou have 4 correct White Balls but not the Powerball\n you win $100")
        elif intersect == 3 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have 3 correct White Balls and the Powerball\n you win $100")
        elif intersect == 3 and self.userpowerball != self.todayspowerball:
            print("Congratulations!\nYou have 3 correct White Balls but not the Powerball\n you win $7")
        elif intersect == 2 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have 2 correct White Balls and the Powerball\n you win $7")
        elif intersect == 1 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have 1 correct White Balls and the Powerball\n you win $4")
        elif intersect == 0 and self.userpowerball == self.todayspowerball:
            print("Congratulations!\nYou have no correct White Balls but you have the Powerball\n you win $4")
        else:
            print("Try again")



