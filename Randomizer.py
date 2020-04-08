import random
from Init import Init


# Random Machine
class RandomClue(Init):
    def __init__(self):
        super().__init__()
        self.random_1 = random.randint(0, len(self.four_legs) - 1)
        self.random_2 = random.randint(0, len(self.two_legs) - 1)

        self.animals = [self.four_legs[self.random_1],
                        self.two_legs[self.random_2]]
        self.random_3 = random.randint(0, len(self.animals) - 1)

        if self.random_3 == 0:
            self.clue = self.clue_2
        else:
            self.clue = self.clue_1

        random_words = self.animals[self.random_3]

        self.words = random_words



