from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class  Snake:
 
  def __init__(self):
    self.body_size = BODY_PARTS
    self.coordinates = []
    self.squares = []

    for i in range(0,BODY_PARTS):
      self.coordinates.append([0,0])

    for x,y in self.coordinates:
      square = Canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag="snake")
      self.squares.append(square)

class Food:
    def __init__(self):
      
      x = random.randint(0,int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
      y = random.randint(0,int(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE
      
      self.coordinates = [x,y]

      Canvas.create_oval(x, y, x + SPACE_SIZE,y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
  
  x,y = snake.coordinates[0]
   
  if direction == "up":
       y -= SPACE_SIZE
  elif  direction == "down":
       y += SPACE_SIZE
  elif direction == "left":
       x -= SPACE_SIZE
  elif direction == "right":
       x += SPACE_SIZE

  snake.coordinates.insert(0,(x,y))

  square = Canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
  
  snake.squares.insert(0, square)

  if x == food.coordinates[0] and y == food.coordinates[1]:
     
     global score

     score += 1

     label.config(text="Score:{}".format(score))

     Canvas.delete("food")

     food = Food()
  else:
     
    del snake.coordinates[-1]

    Canvas.delete(snake.squares[-1])

    del snake.squares[-1]

  if check_collisions():  
     game_over()

  else:
     window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
  
   global direction

   if new_direction == 'left':
      if direction != 'right':
         direction = new_direction
   elif new_direction == 'right':
      if direction != 'left':
         direction = new_direction
   elif new_direction == 'up':
      if direction != 'down':
         direction = new_direction
   elif new_direction == 'down':
      if direction != 'up':
         direction = new_direction

def check_collisions():
  
  x, y = snake.coordinates[0]

  if x < 0 or x >= GAME_WIDTH:
     return True
  elif y < 0 or y >= GAME_HEIGHT:
     print("GAME OVER")
     return True
    
  for body_part in snake.coordinates[1:]:
     if x == body_part[0] and y == body_part[1]:
       print("GAME OVER")
       return True

     return False
  
def game_over():
 
    Canvas.delete(ALL)
    Canvas.create_text(Canvas.winfo_width()/2, Canvas.winfo_height()/2,font=('consolas',70), text="GAME OVER",fill="red", tag="gameover")

window = Tk()
window.title("Snake game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window,text="Score:{}".format(score),font=('consolas',40))
label.pack()

Canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
Canvas.pack()

window.update()

window_width = window.winfo_width()  
window_heigth = window.winfo_height()
screen_heigth = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

x = int((screen_heigth/2) - (window_width/2))
y = int((screen_heigth/2) - (window_heigth/2))

window.geometry(f"{window_width}x{window_heigth}+{x}+{y}")

window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()