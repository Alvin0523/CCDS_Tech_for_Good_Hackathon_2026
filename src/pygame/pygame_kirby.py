import pygame
pygame.init()

# define game, player, enemy variables
GAME_WIDTH = 800
GAME_HEIGHT = 600
TILE_SIZE = 31

PLAYER_X = GAME_WIDTH//4
PLAYER_Y = 430 
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 62

HEALTH_SIZE = 25

ENEMY_SIZE = 45
ENEMY_VELOCITY_X = 3

GRAVITY = 0.5
FRICTION = 0.5
PLAYER_VELOCITY_X = 5
PLAYER_VELOCITY_Y = -15 
FLOOR_Y = PLAYER_Y + PLAYER_HEIGHT 

def load_img(filepath, scale=None):
    image = pygame.image.load(filepath)
    if scale is not None:
        image = pygame.transform.scale(image, scale)
    return image

bg_img = load_img("images/background.jpg", (GAME_WIDTH, GAME_HEIGHT))
player_img_right = load_img("images/kirby_right.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_img_left = load_img("images/kirby_left.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_img_jump_right = load_img("images/kirby_jump_right.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_img_jump_left = load_img("images/kirby_jump_left.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
floor_tile_img = load_img("images/floor-tile.png", (TILE_SIZE, TILE_SIZE)) 
enemy_img_right = load_img("images/enemy_right.png", (ENEMY_SIZE, ENEMY_SIZE))
enemy_img_left = load_img("images/enemy_left.png", (ENEMY_SIZE, ENEMY_SIZE))
health_img = load_img("images/heart.png", (HEALTH_SIZE, HEALTH_SIZE))
restart_button_img = load_img("images/restart_button.png", (140,50))

bg_width = bg_img.get_width()
bg_x = 0

INVINCIBLE_END = pygame.USEREVENT

#----------------------------------------------------------------------------#
# [NEW CODE]: Step 1 - create Button class
class Button(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, GAME_WIDTH/2-70, GAME_HEIGHT/2+10, 140,50)
        self.image = restart_button_img
#----------------------------------------------------------------------------#

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_img_right
        self.direction = "right"
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumping = False
        self.invincible = False
        self.max_health = 5
        self.health = self.max_health

    def update_img(self):
        if self.jumping:
            if self.direction == "right":
                self.image = player_img_jump_right

            elif self.direction == "left":
                self.image = player_img_jump_left

        elif self.direction == "right":
            self.image = player_img_right

        elif self.direction == "left":
            self.image = player_img_left

    def set_invincible(self, ms=1000):
        self.invincible = True
        pygame.time.set_timer(INVINCIBLE_END, ms, 1)

class Enemy(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.image = enemy_img_left
        self.velocity_x = ENEMY_VELOCITY_X
        self.direction = "left"
        self.jumping = False
        self.start_x = 0
        self.max_x = 0

    def update_img(self):
        if self.velocity_x > 0:
            self.direction = "right"
            self.image = enemy_img_right
        
        elif self.velocity_x < 0:
            self.direction = "left"
            self.image = enemy_img_left

class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
        self.image = image

def create_map():
    # 4 horizontal tiles
    for i in range(4):
        tile = Tile((i+13)*TILE_SIZE, player.y - 2*TILE_SIZE, floor_tile_img)
        tiles.append(tile)

    # bottom row
    for i in range(60):
        if i in (0,1):
            continue
        tile = Tile(i*TILE_SIZE, player.y + 2*TILE_SIZE, floor_tile_img)
        tiles.append(tile)

    # 3 vertical tiles 
    for i in range(3):
        tile = Tile(3*TILE_SIZE, player.y + (i-1)*TILE_SIZE, floor_tile_img)
        tiles.append(tile)

def reset_game():
    global player, boo, tiles, game_over
    player = Player()
    boo = Enemy(GAME_WIDTH-ENEMY_SIZE, FLOOR_Y-ENEMY_SIZE)
    boo.start_x = GAME_WIDTH - 16*TILE_SIZE
    boo.max_x = boo.start_x + 16*TILE_SIZE
    tiles = []
    create_map()

    game_over = False

def check_tile_collision(char):
    for tile in tiles:
        if char.colliderect(tile):
            return tile
    return None

def check_tile_collision_x(char):
    tile = check_tile_collision(char)
    if tile is not None: 
        if char.velocity_x < 0:
            char.x = tile.x + tile.width 

        elif char.velocity_x > 0:
            char.x = tile.x - char.width

        # make boo turn back when he collides!
        if char == boo:
            char.velocity_x *= -1
        else:
            char.velocity_x = 0

def check_tile_collision_y(char):
    tile = check_tile_collision(char)
    if tile is not None:
        if char.velocity_y < 0:
            char.y = tile.y + tile.height 

        elif char.velocity_y > 0:
            char.y = tile.y - char.height
            char.jumping = False

        char.velocity_y = 0

def move_player_x(velocity_x):
    global bg_x
    move_map_x(velocity_x)

    tile = check_tile_collision(player)
    if tile is not None:
        move_map_x(-velocity_x)
        bg_x -= velocity_x/2

def move_map_x(velocity_x):
    """moves everything on the map except for the player"""
    for tile in tiles:
        tile.x += velocity_x

    boo.start_x += velocity_x
    boo.max_x += velocity_x
    boo.x += velocity_x    

def move():
    global game_over
    
    # player - y movement
    player.velocity_y += GRAVITY
    player.y += player.velocity_y

    check_tile_collision_y(player)

    # enemy - x movement
    boo.x += boo.velocity_x

    if boo.x > boo.max_x:
        boo.velocity_x *= -1

    check_tile_collision_x(boo)

    # only check for collisions when player is not invincible
    if not player.invincible and player.colliderect(boo):
        player.health -= 1
        player.set_invincible()

    if player.y > GAME_HEIGHT:
        player.health = 0

    # check if game over
    if player.health <= 0:
        game_over = True

def draw():
    global bg_x
    bg_x = bg_x % bg_width
    screen.blit(bg_img, (bg_x,0))
    screen.blit(bg_img, (bg_x - bg_width,0))

    for tile in tiles:
        screen.blit(tile.image, tile)

    player.update_img()
    screen.blit(player.image, player)
    boo.update_img()
    screen.blit(boo.image, boo)

    for i in range(player.health):
        screen.blit(health_img, (20+ i*(HEALTH_SIZE+5),20, HEALTH_SIZE,HEALTH_SIZE))

    #----------------------------------------------------------------------------#
    # Step 3 - draw out text & button when game is over
    if game_over:
        text_surface = game_font.render("Game Over", False, "black")
        screen.blit(text_surface, (GAME_WIDTH/2-85,GAME_HEIGHT/3+20))

        screen.blit(restart_button.image, restart_button)
    #----------------------------------------------------------------------------#

# set up game screen
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Working Mini Game") 
pygame.display.set_icon(player_img_right)
clock = pygame.time.Clock()

# set up texts
pygame.font.init()
game_font = pygame.font.SysFont("arial", 40)
game_over = False

# initialise game elements
player = Player()
boo = Enemy(GAME_WIDTH-ENEMY_SIZE, FLOOR_Y-ENEMY_SIZE)
boo.start_x = GAME_WIDTH - 16*TILE_SIZE
boo.max_x = boo.start_x + 16*TILE_SIZE
tiles = []
create_map()
#----------------------------------------------------------------------------#
# Step 2 - initialise a restart button
restart_button = Button()
#----------------------------------------------------------------------------#

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        # check for invincible event
        if event.type == INVINCIBLE_END:
            player.invincible = False

        #----------------------------------------------------------------------------#
        # [NEW CODE]: Step 4 - check for mouse click event when game is over
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # Check if the click position (event.pos) collides with the button's Rect
            if restart_button.collidepoint(event.pos):
                reset_game()
        #----------------------------------------------------------------------------#
    
    keys = pygame.key.get_pressed()
    # # if game over, press enter key to start again
    # if keys[pygame.K_RETURN] and game_over:
    #     reset_game()

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and (not player.jumping):
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.direction = "left"
        move_player_x(PLAYER_VELOCITY_X)
        bg_x += PLAYER_VELOCITY_X/2

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.direction = "right"
        move_player_x(-PLAYER_VELOCITY_X)
        bg_x -= PLAYER_VELOCITY_X/2

    # only move + update screen if game is not over
    if not game_over:
        move()
        draw()
        clock.tick(60)
        pygame.display.flip()

pygame.quit()