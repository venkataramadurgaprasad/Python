from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_part(self.turtles[-1].pos())

    def move(self):
        for pos_num in range(len(self.turtles) - 1, 0, -1):
            self.turtles[pos_num].goto(self.turtles[pos_num - 1].pos())
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
