
import math

class SE2:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def draw(self, plt):
        plt.scatter(self.x, self.y, s=100)
        plt.arrow(self.x, self.y, 0.25 * math.cos(math.radians(self.theta)), 0.25 * math.sin(math.radians(self.theta)))

