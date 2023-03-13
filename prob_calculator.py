import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for ball, quantity in kwargs.items():
            self.contents.extend([ball] * quantity)

    def draw(self, balls):
        if balls >= len(self.contents):
            drawn = self.contents.copy() # Assign the values we got into the list to a varaible.
            self.contents.clear() # Clear the list. 
        else:
            drawn = random.sample(self.contents, balls)
            for ball in drawn:
                self.contents.remove(ball)
        return drawn
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expCounter = 0
    ballsOK = 0
    while expCounter <= num_experiments:
        copyHat = copy.deepcopy(hat) # Get a copy of the hat object.
        balls = copyHat.draw(num_balls_drawn) # Call the draw method to be able to get the drawn balls.
        for key, val in expected_balls.items():
            if balls.count(key) < val:
                break
        else:
            ballsOK += 1
        expCounter += 1
    return ballsOK / num_experiments