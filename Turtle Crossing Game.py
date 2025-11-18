from turtle import Turtle , Screen ,xcor, ycor
import time
import random
screen=Screen()
UP=90
DOWN=270
LEFT = 180
RIGHT = 0
font="Courier",30,"bold"
FINISH_LINE_Y=280
starting_position=(0,-280)

# lets the Player choose the colour of the turtle

chosen_color=""
while chosen_color.lower() == 'black' or chosen_color == "":
    
    # Use screen.textinput() for a clean GUI prompt
    chosen_color = screen.textinput(
        title="Color Choice", 
        prompt=f"Enter a color for your turtle (DO NOT enter BLACK):"
    )

    # Check if the user clicked Cancel or provided empty input
    if chosen_color is None:
        # If the user cancels, set a default non-black color and exit the loop
        chosen_color = "white"
        break
        
    # Shows a message if they chose black or an empty string
    if chosen_color.lower() == 'black':
        # We can't display a pop-up error, so we write an error message to the screen
        print(f"ERROR: BLACK is forbidden! Please choose a different color.")

# setting up the screen:-
screen.bgcolor("black")
screen.title("Turtle crossing capstone..........")
screen.setup(width=800,height=600)
screen.tracer(0)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10        #increasing the speed of car by 10 units
# setting up our cursor:-
class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # defining the shape of our cursor(Turtle)
        self.color(chosen_color)    # defining colour of our Turtle (Pink)
        self.penup()
        self.goto(starting_position)   # starting position
        self.setheading(90)

    def down(self):                                      
        if self.heading()!=DOWN:                  #   Checks if the object is already moving down
            self.setheading(DOWN)                 #   chamges the direction to down
            self.forward(20)                      #   moves forward 20 units
        else:
            self.forward(20)                      #   If already facing down, just moves forward 20 units


# The functions up, right, and left work the same way as the down function, but they operate in their respective directions.

    def up(self):                    # Up function
        if self.heading() != UP:
            
            self.setheading(UP)
            self.forward(20)
        else:
            self.forward(20)
      

    def right(self):                 # Right function 
        if self.heading() != RIGHT:
            self.setheading(RIGHT)
            self.forward(20)
        else:
           
            self.forward(20)
        
    

    def left(self):                  # Left function
        if self.heading() != LEFT:
            self.setheading(LEFT)
            self.forward(20)
        else  :
            self.forward(20)
       

    def go_to_start(self):
        # Move the object back to the starting position coordinates.
        self.goto(starting_position)


    def is_at_finish(self):
        # Check if the object's current Y position (ycor()) is past the finish line Y constant.
        if self.ycor()> FINISH_LINE_Y:
            return True        # Crossed the finish line
        else:
            return False       # Has not crossed the finish line


# Setting up Cars

class Car(Turtle):
    """
    Manages the creation, movement, and speed of all cars in the game.
    It inherits from Turtle, but in this implementation, the Car instance
    itself is primarily a manager, while the actual cars are stored in all_cars.
    """

    def __init__(self):
        super().__init__()    # Initialize the parent class (Turtle)
        self.all_cars=[]      # List to store all individual car objects on the screen
        self.car_speed=10     # initial speed of the car

    def create_car(self):
        
        # Generates a new car object randomly, but only on occasion. This controls the traffic density.
        
        random_chance=random.randint(1,6)    # Generate a random integer from 1 to 6 
        if random_chance==1:                 # Only create a car if the random chance hits '1'
            new_car=Turtle()
            new_car.shape("square")                    # Set its shape to a square
            new_car.color(random.choice(COLORS))       # random color for the car (assuming COLORS is a predefined list)
            new_car.penup()                            #Ensure the car does not draw a line
            new_car.shapesize(stretch_len=2,stretch_wid=1)
           
            random_y=random.randint(-210,210)     # Select a random Y-coordinate for the car to spawn on the road
            new_car.goto(300,random_y)            # Position the new car far to the right, ready to move left
            self.all_cars.append(new_car)         # Add the newly created car to the list of all active cars
    
    
    def move(self):
        """
        Moves all active cars backward by a fixed amount (the current car_speed).
        This simulates the cars moving left across the screen.
        """

        for car in self.all_cars:  # Loop through every car object in the list
            car.backward(5)

    def level_up(self):
         
        # Increases the speed of the cars when the player successfully completes a level.
        self.car_speed *= MOVE_INCREMENT


# setting up the scoreboard:-

class Scoreboard(Turtle):
    """
    Displays and manages the game score (level), 
    utilizing Turtle's writing capabilities through inheritance
    """

    def __init__(self):
        super().__init__()
        
        self.hideturtle()       # keeping the scored board invisible ,so that we can only see the text 
        self.penup()
        self.goto(-290,250)     # Move the scoreboard to its display position (top-left of the screen)
        self.color("white")
        self.score=0
        self.color("white")
        self.write(f"Score : {self.score}" , align= "left", font=(font))
    
     # Increases the level/score by one and updates the display on the screen.

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}" , align= "left", font=(font))
    

    #  Game over 
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER",move=False,align="center",font=(font))



        
# --- Game Setup and Initialization ---

game_on=True
tim=Tim()
car=Car()
score=Scoreboard()
screen.listen()

# Bind the player's movement methods to the corresponding arrow keys
screen.onkey(tim.up,"Up")
screen.onkey(tim.down,"Down")
screen.onkey(tim.right,"Right")
screen.onkey(tim.left,"Left")

# --- Main Game Loop ---
while game_on:
    screen.update()
    time.sleep(0.1)          # Pause the loop execution for a short time (controls game speed/frame rate)
    car.create_car()
    car.move()

    # detects the collision between the car and our cursor
    for i in car.all_cars:
        if i.distance(tim) < 20:
            score.game_over()
            game_on=False

    # reached thefinish line
    if tim.is_at_finish():
        tim.go_to_start()
        score.update_score()
        car.speed("fastest")


screen.exitonclick()