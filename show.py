from utilities import Creatnumbers
import colors


class Show(Creatnumbers):
    """Numbers that have been created in Creatnumber class will be displayed
    Under this class by display method. there is also deletenumbers method to refresh the lists in each iteration"""
    def display(self):
        powerballnumber = ""
        for i in self.todayswhiteball:
            powerballnumber += f" {i}"
        print("Today's power ball winning numbers:")
        print(colors.MAGENTA+powerballnumber, colors.YELLOW+str(self.todayspowerball[0]))

        luckynumber = ""
        for i in self.userwhiteball:
            luckynumber += f" {i}"
        print(colors.CYAN+"Your lucky numbers:")
        print(colors.MAGENTA+luckynumber,colors.YELLOW + str(self.userpowerball[0]))

    def intersect(self):
        self.intersections = set(self.userwhiteball) & set(self.todayswhiteball)
        # The above code is to evaluate how many common numbers are there in both whiteballs.
        print(colors.CYAN + f"Correct White Balls: {self.intersections} = {len(self.intersections)}")
        return len(self.intersections)

    def deletenumbers(self):
        del self.userwhiteball[:]
        del self.userpowerball[:]
        del self.todayswhiteball[:]
        del self.todayspowerball[:]


