import pygame
import random

pygame.init()


'windows settings'
win_width , win_height = 1600 , 900
pygame.display.init()
window = pygame.display.set_mode((win_width,win_height))

'constant'
game_run = True

#comet
comet_data = []
comet_speed = 1000
comet_constant = 0

#missile
missile_data = []
missile_speed = 5000

#rocket
x,y = win_width // 2 , win_height // 2
width , height = 10 , 10
speed = 4
rocket = pygame.Surface((width,height))
rocket.fill((78, 52, 46))


def calcAngel(missile_x, missile_y, x, y):
    dx = missile_x - x
    dy = missile_y - y
    length = ( dx**2 + dy**2 )**1/2
    cos_alpha = dx/length
    sin_alpha = dy/length
    return cos_alpha, sin_alpha

def spawnMissile(self, missile_x, missile_y, x, y):
    missile = pygame.draw.rect(self , (255,255,255) , (x , y , 5 , 5))
    cos_alpha , sin_alpha = calcAngel(missile_x, missile_y, x, y)
    info = {'object': missile,
            'size': [5,5],
            'color': (255,255,255),
            'target': [missile_x,missile_y],
            'pos': [x,y],
            'cos': cos_alpha,
            'sin': sin_alpha}
    missile_data.append(info)

def spawnComet(self , win_width , win_height):
    const = random.randint(1,2)
    if const == 1:
        x1, y1 = random.randint(1, win_width), 0
        const = random.randint(1, 3)
        if const == 1:
            x2, y2 = 0, random.randint(1, win_height)
        elif const == 2:
            x2, y2 = random.randint(1, win_width), win_height
        else:
            x2, y2 = win_width, random.randint(1, win_height)
    else:
        x1, y1 = 0, random.randint(1, win_height)
        const = random.randint(1, 3)
        if const == 1:
            x2, y2 = 0, random.randint(1, win_height)
        elif const == 2:
            x2, y2 = random.randint(1, win_width), win_height
        else:
            x2, y2 = win_width, random.randint(1, win_height)
    comet = pygame.draw.rect(self , (0,0,0) , (x1 , y1 , 15 , 15))
    cos_alpha, sin_alpha = calcAngel(x2 , y2 , x1 , y1)
    info = {'object': comet,
            'size': [15,15],
            'color' : (0,0,0),
            'target': [x2, y2],
            'pos': [x1, y1],
            'sin': sin_alpha,
            'cos': cos_alpha }
    comet_data.append(info)

def flightObject(self, speed, data):
    for info in data:
        target = info['target']
        pos = info['pos']
        cos_alpha = info['cos']
        sin_alpha = info['sin']
        if abs(target[0] - pos[0]) > 4 and abs(target[1] - pos[1]) > 4:
            info['pos'][0] += speed*cos_alpha
            info['pos'][1] += speed*sin_alpha
            object = pygame.draw.rect(self, info['color'] , (pos[0], pos[1], info['size'][0], info['size'][1]))
            info['object'] = object
        else:
            data.remove(info)

def drawRocket():
    pygame.time.delay(20)
    pygame.display.update()
    window.fill((46, 125, 50))
    window.blit(rocket, (x, y))

def destroyObject(target_data , destroyer_data):
    for target in target_data:
        target_pos = target['pos']
        object1 = target['object']
        for destroyer in destroyer_data:
            object2 = destroyer['object']
            destroyer_pos = destroyer['pos']
            if abs(target_pos[0] - destroyer_pos[0]) <= 15 and abs(target_pos[1] - destroyer_pos[1]) <= 15 and object1 != object2:
                target_data.remove(target)
                destroyer_data.remove(destroyer)

'main loop'

while game_run:
    comet_constant += 1
    drawRocket()
    flightObject(window, missile_speed, missile_data)
    flightObject(window, comet_speed, comet_data)
    destroyObject(comet_data , missile_data)
    destroyObject(comet_data , comet_data)
    if comet_constant == 10:
        comet_constant = 0
        spawnComet(window , win_width , win_height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            missile_x, missile_y = pygame.mouse.get_pos()
            missile_x, missile_y = int(missile_x) , int(missile_y)
            spawnMissile(window, missile_x, missile_y, x, y)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and x < win_width - 2*width:
        x += speed
    if keys[pygame.K_a] and x > width:
        x -= speed
    if keys[pygame.K_w] and y > height:
        y -= speed
    if keys[pygame.K_s] and y < win_height - 2*height:
        y += speed

