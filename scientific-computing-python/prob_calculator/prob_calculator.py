import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.dic = kwargs
        self.contents = []

        for key in self.dic:
            value = int(self.dic.get(key))
            #determine number of times to store key into list given value
            for i in range(value):
                self.contents.append(key)
        self.standard = copy.deepcopy(self.contents)
        



    def draw(self, number):
        try:
            draw_list = list(random.sample(self.contents, number))
            for i in draw_list:
                if i in self.contents:
                    self.contents.remove(i)
            return draw_list
        except:
            self.contents = self.standard
            print(self.contents)
            return self.contents




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    number = num_experiments
    for i in range(num_experiments):

        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        drawn_balls = list(hat_copy.draw(num_balls_drawn))
        for ball in drawn_balls:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1

        if all(x <= 0 for x in expected_balls_copy.values()):
            count += 1

    probability = count/number
    return probability
