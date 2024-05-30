# Classes + Objects

class Computer:

    def __init__(self, name, lbs, ssd, ram):
        self.name = name
        self.weight = lbs
        self.ssd = ssd
        self.ram = ram

    def is_big_computer(self):
        if self.ssd >= 1024 and self.ram >= 16:
            return True
        else:
            return False

    def turn_on(self):
        print("Your computer turns on.")

    def run_website(self):
        print("Your computer runs a website.")

    def shut_down(self):
        print("Your computer turns off.")



