import curses
import random
import time

def game_loop(window):
    curses.curs_set(0)
    snake = [
        [10 ,15],
        [9 ,15],
        [8 ,15],
        [7 ,15],
    ]

    num_initial_fruits = 100
    

    fruits = []
    for _ in range(num_initial_fruits):
        fruits.append(get_new_fruit_position(window, snake, fruits))
    
    current_direction = curses.KEY_DOWN
    score = 0
    while True:
        draw_screen(window=window)
        draw_snake(snake = snake, window = window)
        

        for fruit_pos in fruits:
            draw_actor(actor = fruit_pos, window = window, char="⚆")

        direction = get_new_direction(window = window, timeout=100) 
        
        if direction is None:
            direction = current_direction
        
        if direction_is_opposite(direction = direction, current_direction = current_direction):
            direction = current_direction 

        snake_ate_fruit = False
        
        
        move_snake(snake=snake, direction=direction, snake_ate_fruit=False)
        for i, fruit_pos in enumerate(fruits):
            if snake_hit_fruit(snake = snake, fruit_to_check=fruit_pos):
                snake_ate_fruit = True
                
                fruits.pop(i) 
                score += 1
                fruits.append(get_new_fruit_position(window, snake, fruits))
                break 
        
        
        if not snake_ate_fruit:
            snake.pop() 
        
        if snake_hit_border(snake = snake, window =window):
            break
        if snake_hit_itself(snake = snake):
            break 
        
        current_direction = direction
        
    finish_game(score = score,window=window)
def finish_game(score,window):
    height, width = window.getmaxyx()
    s = f"Você perdeu {score} frutas!"
    y = int(height / 2)
    x = int ((width - len(s)) / 2)
    window.addstr(y,x,s)
    window.refresh()
    time.sleep(2)
    
def direction_is_opposite(direction, current_direction):
    match direction:
        case curses.KEY_UP:
            return current_direction == curses.KEY_DOWN
        case curses.KEY_DOWN:
            return current_direction == curses.KEY_UP
        case curses.KEY_LEFT:
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_RIGHT:
            return current_direction == curses.KEY_LEFT
    return False 
def get_new_fruit_position(window, snake_positions, existing_fruits_positions):
    height, width = window.getmaxyx()
    while True:
        fruit_x = random.randint(1, height - 2)
        fruit_y = random.randint(1, width - 2)
        new_fruit_pos = [fruit_x, fruit_y]
        

        if new_fruit_pos not in snake_positions and new_fruit_pos not in existing_fruits_positions:
            return new_fruit_pos

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(actor=head, window=window)

def snake_hit_fruit(snake, fruit_to_check):
    return snake[0] == fruit_to_check

def snake_hit_itself(snake):
    head = snake[0]
    body =  snake[1:]
    return head in body
    
def draw_screen(window):
    window.clear()#limpar terminal
    window.border(0)
    
def draw_snake(snake,window):
    head = snake[0]
    draw_actor(actor = head, window=window,char="@")
    body = snake[1:]
    for body_part in body:
        draw_actor(actor = body_part, window=window,char="S")
    
def draw_actor(actor,window,char):
    window.addch(actor[0], actor[1], char)
    
def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT]:
        return direction
    return None


def move_snake(snake, direction, snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor = head, direction = direction)
    snake.insert(0,head)
    

def move_actor(actor, direction):
    match  direction:
        case  curses.KEY_UP:
            actor[0] -= 1
        case  curses.KEY_DOWN:
            actor[0] += 1
        case  curses.KEY_LEFT:
            actor[1] -= 1
        case  curses.KEY_RIGHT:
            actor[1] += 1
        case _: #não apertou a tecla
            return
        
def actor_hit_border(actor,window):
    height, width = window.getmaxyx()
    if (actor[0] <= 0) or (actor[0] >= height-1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width-1):
        return True
    return False

if __name__ == "__main__":
    curses.wrapper(game_loop)
    print("Perdeu!!")