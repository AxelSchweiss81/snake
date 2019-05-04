import libtcodpy as tcod
from random import randint
import sys
from time import sleep
 
# ######################################################################
# Global Game Settings
# ######################################################################
# Windows Controls
FULLSCREEN = False
SCREEN_WIDTH = 40  # characters wide
SCREEN_HEIGHT = 25  # characters tall
LIMIT_FPS = 10  # 20 frames-per-second maximum
# Game Controls
TURN_BASED = False  # turn-based game
 
 
# ######################################################################
# User Input
# ######################################################################
def get_key_event(turn_based=None):
    if turn_based:
        # Turn-based game play; wait for a key stroke
        key = tcod.console_wait_for_keypress(True)
    else:
        # Real-time game play; don't wait for a player's key stroke
        key = tcod.console_check_for_keypress()
    return key
 
def place_fruit():
    global fruit_x, fruit_y

    if tcod.console_get_char(0, fruit_x, fruit_y,)==70:
        return
    else:
        fruit_x=randint(0,SCREEN_WIDTH)
        fruit_y=randint(0,SCREEN_HEIGHT)
        tcod.console_put_char(0, fruit_x, fruit_y, 'F', tcod.BKGND_NONE)

    
def snake():
        global snake_len, player_cor
        
        player_cor.append([player_x,player_y])
        
        if len(player_cor)>snake_len:

            x=player_cor[0]

            tcod.console_put_char(0, x[0], x[1], ' ', tcod.BKGND_NONE)
            
            
        if len(player_cor)>snake_len:

            player_cor=player_cor[1:]

                
        for i in player_cor:
            tcod.console_put_char(0, i[0], i[1], '1', tcod.BKGND_NONE)
    



def handle_keys():
    global player_x, player_y, player_cor, direction, direction2
 
    key = get_key_event(TURN_BASED)

 
    if key.vk == tcod.KEY_ESCAPE:
        sys.exit()
    # movement keys

    if tcod.console_is_key_pressed(tcod.KEY_UP) and direction!="down":
        direction="up"         
 
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN) and direction!="up":
        direction="down"        
 
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT) and direction!="right":
        direction="left"
 
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT) and direction!="left":
        direction="right"
    
    
    
    if direction=="up":
        player_y-=1
    elif direction=="down":
        player_y+=1
    elif direction=="left":
        player_x-=1
    elif direction=="right":
        player_x+=1
        
    if player_x==-1:
        player_x=SCREEN_WIDTH-1
    elif player_x==SCREEN_WIDTH:
        player_x=0
    elif player_y==-1:
        player_y=SCREEN_HEIGHT-1
    elif player_y==SCREEN_HEIGHT:
        player_y=0
    
 
#############################################
# Main Game Loop
#############################################

direction="up"
direction2=""
 
 
def main():
    # Setup player
    global player_x, player_y, player_cor, snake_len, fruit_x, fruit_y,high_score
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player_cor=[]
    snake_len=0
    high_score=0
    fruit_x=randint(0,80)
    fruit_y=randint(0,50)
    game_over="u lost"
 
    # Setup Font
    font_filename = 'arial10x10.png'
    tcod.console_set_custom_font(font_filename, tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
 
    # Initialize screen
    title = 'Snake'
    root=tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title, FULLSCREEN)
 
    # Set FPS
    tcod.sys_set_fps(LIMIT_FPS)


 
    exit_game = False
    while not tcod.console_is_window_closed() and not exit_game:
        tcod.console_set_default_foreground(0, tcod.white)
        tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
        tcod.console_flush()
        
        if player_x==fruit_x and player_y==fruit_y:
            snake_len+=1
            high_score+=1
        
        place_fruit()          
        snake()
        handle_keys()
        
        if tcod.console_get_char(0, player_x, player_y)==49:
            sleep(1)
            tcod.console_clear(root)
            tcod.console_flush()
            sleep(0.5)
            tcod.console_print_rect_ex(root, (SCREEN_WIDTH // 2)-len(game_over)//2, SCREEN_HEIGHT // 2, 0, 0, 0, 0, "{}".format(game_over))
            tcod.console_print_rect_ex(root, (SCREEN_WIDTH // 2)-len("Highscore: {}".format(high_score))//2, (SCREEN_HEIGHT // 2)+2, 0, 0, 0, 0, "Highscore: {}".format(high_score))
            tcod.console_flush()
            sleep(5)
            sys.exit()
    
 
 
main()