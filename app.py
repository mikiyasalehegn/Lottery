from evaluator import Evaluator
import colors


def app():
    """This function was made to orchestrate all classes using while loop and other logical codes"""
    print(colors.CYAN, colors.BOLD + " " * 30 + "Welcome to Powerball")
    input("Press enter to start")
    s = Evaluator()
    while True:
        try:
            pay = int(input("Please pay $6 to get lottery: "))
            if pay >= 6:
                s.create()
                s.display()
                s.compute(s.intersect())
                s.deletenumbers()
                go = input("Do you wanna continue? y/n")
                if go == "n":
                    break
                else:
                    continue
            else:
                print()
                continue
        except ValueError:
            print("Please enter exact value")