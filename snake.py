import turtle
import random

turtle.tracer(1,0)

SIZE_X=1000
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y)

turtle.pendown()

draw=turtle.clone()

draw.penup()
draw.goto(398, 248)
draw.pendown()
draw.goto(-398, 248)
draw.goto(-398, -248)
draw.goto(398, -248)
draw.goto(398,248)
draw.penup()
draw.hideturtle()

box_size = 15
#size_x=750
#size_y=450


turtle.penup()

SQUARE_SIZE = 20
START_LENGHT = 1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone ()
snake.shape('square')

turtle.hideturtle()

turtle.register_shape('trash.gif')

food=turtle.clone()
food.shape('trash.gif')

for i in range (START_LENGHT):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto (x_pos,y_pos)
    pos_list.append(my_pos)

    snake_stamp =snake.stamp()
    stamp_list.append(snake_stamp)

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=100

SPACEBAR = 'space'
UP=0
LEFT=1
DOWN=2
RIGHT=3

direction = UP 
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction=UP
    print ('You pressed the up key')

def down():
    global direction
    direction = DOWN
    print ('You pressed the down key')

def left():
    global direction
    direction = LEFT
    print ('You pressed the left key')

def right():
    global direction
    direction = RIGHT
    print ('You pressed the right key')

turtle.onkeypress (up, UP_ARROW)
turtle.onkeypress (down, DOWN_ARROW)
turtle.onkeypress (left, LEFT_ARROW)
turtle.onkeypress (right, RIGHT_ARROW)

turtle.listen()

def make_food():
    min_x=-int(SIZE_X/4/SQUARE_SIZE)+1
    max_x=int(SIZE_X/4/SQUARE_SIZE)-1
    min_y=-int(SIZE_X/4/SQUARE_SIZE)+1
    max_y=int(SIZE_X/4/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)* SQUARE_SIZE
    food_y = random.randint(min_y,max_y)* SQUARE_SIZE

    food.goto(food_x,food_y)
    f = (food_x,food_y)
    food_pos.append(f)
    the_stamps = food.stamp()
    food_stamps.append(the_stamps)



def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
  

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print ('You moved right!')
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print ('You moved left!')
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print ('You moved up!')
    elif direction == DOWN:
        snake.goto(x_pos , y_pos- SQUARE_SIZE)
        print ('You moved down!')

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)


    global food_stamps, food_pos
    if snake.pos() in food_pos:      
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print ('You have eaten the food!')
        make_food()
    else:
        old_stamp = stamp_list.pop (0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if new_x_pos >= RIGHT_EDGE:
        print ('You hit the right edge! Game over!')
        quit()
    if new_x_pos <= LEFT_EDGE:
        print ('You hit the left edge! Game over!')
        quit()
    if new_y_pos >= UP_EDGE:
        print ('You hit the up edge! Game over!')
        quit()
    if new_y_pos <= DOWN_EDGE:
        print ('You hit the down edge! Game over!')
        quit()

    if snake.pos() in pos_list[0:-1]:
        print('You hit yourself! Game over!')
        quit()

    
    turtle.ontimer(move_snake,TIME_STEP)
    
move_snake()



food_pos = [(100,100)]
food_stamps=[]

for i in food_pos:
    food.goto(i)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

    

    














