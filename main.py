from turtle_race import TurtleRace




def ask_sleep():
    while True:
        sleep = input("Do you want to sleep? [Y/N]  ").lower()
        if sleep == "y":
            return True
        elif sleep == "n":
            return False
        else:
            print("Sorry, This is not a right option...")


def select_game():
    while True:
        choice=int(input("Which game do you want to play?\n1: TurtleRace\n"))
        try:
            game_start = {
                1: TurtleRace()
            }
            game_start[choice].run()
        except Exception as e:
            print(f"Sorry, This is not a right option...")
        if ask_sleep():
            break


if __name__ == '__main__':
    select_game()