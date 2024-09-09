from turtle import Turtle

BALL_SPEED = 10

class Ball(Turtle):
    """
    This class contains the logic of the ball
    """
    def __init__(self):
        super().__init__()
        self.shape("circle") # Shape of the ball
        self.color("white") # Color of the ball
        self.penup() # No writing
        self.x_move = BALL_SPEED # Speed for x movement
        self.y_move = BALL_SPEED # Speed for y movement
        self.move_speed = 0.1 # Move speed

    def move(self):
        """
        Moves the ball to a new position
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Changes y-axis to represent a bounce
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Changes x-axis to represent a bounce
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        """
        Resets the ball's position to the center of the screen
        """
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()