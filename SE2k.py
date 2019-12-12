
import matplotlib.patches as mpatches
import math

from SE2 import SE2

class SE2k(SE2):
    def __init__(self, x, y, theta, kappa):
        SE2.__init__(self, x, y, theta)
        self.kappa = kappa

    def draw(self, plt):
        SE2.draw(self, plt)

        # Calculate all the relevant values for drawing the curvature
        radius = 1.0 / math.fabs(self.kappa)
        normal_angle = 90 * math.copysign(1, self.kappa)
        cx = self.x + radius / 2 * math.cos(math.radians(self.theta + normal_angle))
        cy = self.y + radius / 2 * math.sin(math.radians(self.theta + normal_angle))

        angle = self.theta - normal_angle
        if math.copysign(1, self.kappa) == -1:
            theta1 = -20
            theta2 = 0
        else:
            theta1 = 0
            theta2 = 20

        ax = plt.gca()
        arc = mpatches.Arc((cx, cy), radius, radius, angle=angle, theta1=theta1, theta2=theta2, color='blue', linestyle='--', linewidth=3)
        ax.add_patch(arc)
