from turtle import Turtle

class Paddle(Turtle):
    """
    This class contains the logic of the paddle
    """
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square") # Shape of the paddle
        self.penup() # No writing
        self.starting_coordinates = coordinates # Stores the starting coordinates of the paddle
        self.goto(coordinates) # Moves the paddle to one of the edges of the screen
        self.color("white") # Changes color to white
        self.shapesize(5, 1) # Changes size to reassemble a paddle

    def go_up(self):
        """
        Moves the paddle up
        """
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the paddle up
        """
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def reset(self):
        """
        Resets the paddle to its original position
        """
        self.goto(self.starting_coordinates)