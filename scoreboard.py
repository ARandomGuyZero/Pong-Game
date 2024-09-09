from turtle import Turtle

class Scoreboard(Turtle):
    """
    This class keeps the information of the score
    """
    def __init__(self):
        super().__init__()
        self.color("white") # Color of the text
        self.penup() # No writing
        self.hideturtle() # No cursor shown
        self.goto(0, 160) # Moves the scoreboard to the top of the screen
        self.l_score = 0 # Integer with the score of left paddle
        self.r_score = 0 # Integer with the score of right paddle
        self.update_score() # Show score text upon calling this class

    def update_score(self):
        """
        Update the game's score on the screen
        """
        self.clear()
        self.write(f"{self.l_score}   {self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Scores a point to left paddle
        """
        self.l_score += 1
        self.update_score()

    def r_point(self):
        """
        Scores a point to right paddle
        """
        self.r_score += 1
        self.update_score()