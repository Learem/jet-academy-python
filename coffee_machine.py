class CoffeeMachine:
    max_count = 1

    def __init__(self):
        self.amount_water = 400
        self.amount_milk = 540
        self.amount_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "choosing an action"
        print("Write action (buy, fill, take, remaining, exit): ")

    def user_action(self, input_string):
        if self.state == "choosing an action":
            if input_string == "buy":
                self.buy_menu()
            elif input_string == "fill":
                print()
                print("Write how many ml of water do you want to add: ")
                self.state = "filling a water"
            elif input_string == "take":
                self.take()
                print("Write action (buy, fill, take, remaining, exit): ")
            elif input_string == "remaining":
                self.status_machine()
                print("Write action (buy, fill, take, remaining, exit): ")
            elif input_string == "exit":
                self.state = "exit"
        elif self.state == "choosing a type of coffee":
            if input_string == "back":
                print()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit): ")
                return
            number_drink = int(input_string)
            if number_drink == 1:
                if self.check_resource(250, 0, 16):
                    self.amount_water -= 250
                    self.amount_beans -= 16
                    self.disposable_cups -= 1
                    self.money += 4
                    print("I have enough resources, making you a coffee!")
                    print()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit): ")
            elif number_drink == 2:
                if self.check_resource(350, 75, 20):
                    self.amount_water -= 350
                    self.amount_milk -= 75
                    self.amount_beans -= 20
                    self.disposable_cups -= 1
                    self.money += 7
                    print("I have enough resources, making you a coffee!")
                    print()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit): ")
            elif number_drink == 3:
                if self.check_resource(200, 100, 12):
                    self.amount_water -= 200
                    self.amount_milk -= 100
                    self.amount_beans -= 12
                    self.disposable_cups -= 1
                    self.money += 6
                    print("I have enough resources, making you a coffee!")
                    print()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit): ")
        elif self.state == "filling a water":
            self.amount_water += int(input_string)
            print("Write how many ml of milk do you want to add: ")
            self.state = "filling a milk"
        elif self.state == "filling a milk":
            self.amount_milk += int(input_string)
            print("Write how many grams of coffee beans do you want to add: ")
            self.state = "filling a beans"
        elif self.state == "filling a beans":
            self.amount_beans += int(input_string)
            print("Write how many disposable cups of coffee do you want to add: ")
            self.state = "filling a cups"
        elif self.state == "filling a beans":
            self.amount_beans += int(input_string)
            print("Write how many disposable cups of coffee do you want to add: ")
            self.state = "filling a cups"
        elif self.state == "filling a cups":
            self.disposable_cups += int(input_string)
            print()
            self.state = "choosing an action"
            print("Write action (buy, fill, take, remaining, exit): ")

    def status_machine(self):
        print()
        print("The coffee machine has:")
        print(f"{self.amount_water} of water")
        print(f"{self.amount_milk} of milk")
        print(f"{self.amount_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"${self.money} of money")
        print()

    def check_resource(self, water, milk, beans):
        result = True
        if self.amount_water - water < 0:
            print("Sorry, not enough water!")
            print()
            result = False
        else:
            if self.amount_milk - milk < 0:
                print("Sorry, not enough milk!")
                print()
                result = False
            else:
                if self.amount_beans - beans < 0:
                    print("Sorry, not enough coffee beans!")
                    print()
                    result = False
                else:
                    if self.disposable_cups - 1 < 0:
                        print("Sorry, not enough disposable cups!")
                        print()
                        result = False
        return result

    def buy_menu(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        self.state = "choosing a type of coffee"

    def take(self):
        print()
        print(f"I gave you ${self.money}")
        self.money = 0
        print()
        self.state = "choosing an action"


coffee_machine = CoffeeMachine()


while coffee_machine.state != "exit":
    coffee_machine.user_action(input())
