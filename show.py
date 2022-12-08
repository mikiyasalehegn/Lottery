from utilities import Creatnumbers
import colors


class Show(Creatnumbers):
    """Numbers that have been created in Creatnumber class will be displayed
    Under this class by display method. there is also deletenumbers method to refresh the lists in each iteration"""
    def display(self):
        """The main objective of this method is to display the numbers as a string using for loop"""
        powerballnumber = ""
        for i in self.todayswhiteball:
            powerballnumber += f" {i}"
        print("Today's power ball winning numbers:")
        print(colors.MAGENTA+powerballnumber, colors.YELLOW+str(self.todayspowerball))

        luckynumber = ""
        for i in self.userwhiteball:
            luckynumber += f" {i}"
        print(colors.CYAN+"Your lucky numbers:")
        print(colors.MAGENTA+luckynumber,colors.YELLOW + str(self.userpowerball))

    def intersect(self):
        """This method performs conversion of list(white balls) to set and calculate intersection for them"""
        self.intersections = set(self.userwhiteball) & set(self.todayswhiteball)
        print(colors.CYAN + f"Correct White Balls: {self.intersections} = {len(self.intersections)}")
        return len(self.intersections)

    def deletenumbers(self):
        """Under this method all previous numbers will be erased for refreshing purpose"""
        del self.userwhiteball[:]
        del self.userpowerball[:]
        del self.todayswhiteball[:]
        del self.todayspowerball[:]


