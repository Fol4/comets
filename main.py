import pygame
from math import acos , degrees , cos , sin
pygame.init()


'windows settings'

pygame.display.init()
window = pygame.display.set_mode((1200,1024))


'constant'

game_run = True

'missile'
missile_data = []
missile_speed = 5

'rocket'
x,y = 50 , 50
width , height = 10 , 10
speed = 4
rocket = pygame.Surface((width,height))
rocket.fill((78, 52, 46))

def angel_calc(missile_x,missile_y,x,y):
    dx = missile_x - x
    dy = missile_y - y
    length = ( dx**2 + dy**2 )**1/2
    if dy < 0 and dx >0:
        cos_alpha = abs(dy/length)
        alpha = degrees(acos(cos_alpha))
    elif dx > 0 and dy > 0:
        cos_alpha = dy / length
        alpha = -degrees(acos(cos_alpha))
    elif dy > 0 and dx < 0 :
        cos_alpha = dy / length
        alpha = degrees(acos(cos_alpha))
    else:
        cos_alpha = dx / length
        alpha = -degrees(acos(cos_alpha))
    return alpha



def missile_spawn(self,missile_x,missile_y,x,y):
    missile = pygame.draw.rect(self , (255,255,255) , (x , y , 5 , 5))
    alpha = angel_calc(missile_x,missile_y,x,y)
    info = {'missile': missile,
            'target': [missile_x,missile_y],
             'pos': [x,y],
            'angel': alpha}
    missile_data.append(info)

def missile_flight(self,speed,data):
    for info in missile_data:
        target = info['target']
        pos = info['pos']
        alpha = info['angel']
        if abs(target[0] - pos[0]) > speed and abs(target[1] - pos[1]) > speed:
            info['pos'][0] += speed*cos(alpha)
            info['pos'][1] += speed*sin(alpha)
            missile = pygame.draw.rect(self, (255, 255, 255), (pos[0], pos[1], 5, 5))
            info['missile'] = missile


'main loop'

while game_run:
    pygame.time.delay(20)
    pygame.display.update()
    window.fill((46,125,50))
    window.blit(rocket , (x,y))
    missile_flight(window,missile_speed,missile_data)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            missile_x, missile_y = pygame.mouse.get_pos()
            missile_x, missile_y = int(missile_x) , int(missile_y)
            missile_spawn(window,missile_x,missile_y,x,y)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

