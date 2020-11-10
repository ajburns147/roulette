import random

class Roulette:
    def __init__(self):
        self.list_memory = []
        self.pot = 1000
        self.current_bet = 0

    def main(self):
        R1 = Roulette
        while (0 < self.pot < 2000):
            R1.spin(self)
            R1.choose(self)



        print("pot = ", self.pot)

    def spin(self):

        if random.randint(1, 38) < 17:
            self.list_memory.insert(0, "Win")

        else:
            self.list_memory.insert(0, "Lose")

    def choose(self):
        if self.list_memory[0:4] == ['Lose', 'Lose', 'Lose', "Lose"]:
            for i in self.list_memory:
                if i == "Win":
                    self.current_bet = 10
                    break
                else:
                    self.current_bet*=2

            Roulette.spin(self)

            if self.list_memory[0] == "Lose":
                self.pot -= self.current_bet

            elif self.list_memory[0] == "Win":
                self.pot += self.current_bet
                self.current_bet = 0
            print("pot = ", self.pot)




def main():
    n = 0
    R = Roulette()
    R.main()



main()

