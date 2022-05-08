import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            self.contents += v * [k]
    
    def draw(self,quantity):
        removed_list = []
        if quantity > len(self.contents):
            return self.contents
        for _ in range(quantity):
            removed_item = random.choice(self.contents)
            removed_list.append(removed_item)
            self.contents.remove(removed_item)
        return removed_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_copy = hat_copy.draw(num_balls_drawn)
        expected_copy = copy.deepcopy(expected_balls)
        
        for ball in draw_copy:
            if(ball in expected_copy):
                expected_copy[ball]-=1
        
        if(all(x <= 0 for x in expected_copy.values())):
            event += 1

    return event/num_experiments
