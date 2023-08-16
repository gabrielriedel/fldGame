import matplotlib.pyplot as plt
from sportypy.surfaces.baseball import MLBField
import numpy as np


class DrawingApp:
    def __init__(self):
        # Create a new figure and axis
        # Draw the rink on a matplotlib.Axes object
        self.fig2, self.ax2 = plt.subplots(1, 1, figsize=(12, 8))
        # self.ax2 = self.fig2.add_axes([0.01, 0.01, 0.99, 0.99])
        self.axbaseball = MLBField()

    def draw(self):
        # Plot the provided data on the Axes object
        # self.axbaseball.draw(self.ax2)

        x_data = np.array([0, 100, -50, -30, 0, 50])
        y_data = np.array([0, 100, 200, 200, 200, 200])

        # Create an instance of the DrawingApp class

        # Use the scatter function with sample data
        self.axbaseball.scatter(x_data, y_data, is_constrained=True, symmetrize=True, color='blue')

        self.axbaseball.draw(display_range = "infield", ax=self.ax2)

    def show(self):
        plt.show()


if __name__ == "__main__":
    # Create an instance of our DrawingApp class
    app = DrawingApp()

    # Draw the sample data on the Axes
    app.draw()

    # Show the Matplotlib window
    app.show()











# from sportypy.surfaces.baseball import MLBField
#
# mlb = MLBField()
# mlb.draw(display_range = "infield")
# print("HELLO")





