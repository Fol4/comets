import pygame
pygame.init()


'windows settings'

pygame.display.init()
window = pygame.display.set_mode((1600,900))


'constant'

game_run = True

'missile'
missile_data = []
missile_speed = 3500

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
    cos_alpha = dx/length
    sin_alpha = dy/length
    return cos_alpha, sin_alpha



def missile_spawn(self,missile_x,missile_y,x,y):
    missile = pygame.draw.rect(self , (255,255,255) , (x , y , 5 , 5))
    cos_alpha , sin_alpha = angel_calc(missile_x,missile_y,x,y)
    info = {'missile': missile,
            'target': [missile_x,missile_y],
            'pos': [x,y],
            'cos': cos_alpha,
            'sin': sin_alpha}
    missile_data.append(info)

def missile_flight(self,speed):
    for info in missile_data:
        target = info['target']
        pos = info['pos']
        cos_alpha = info['cos']
        sin_alpha = info['sin']
        if abs(target[0] - pos[0]) > 4 and abs(target[1] - pos[1]) > 4:
            info['pos'][0] += speed*cos_alpha
            info['pos'][1] += speed*sin_alpha
            missile = pygame.draw.rect(self, (255, 255, 255), (pos[0], pos[1], 5, 5))
            info['missile'] = missile


'main loop'

while game_run:
    pygame.time.delay(20)
    pygame.display.update()
    window.fill((46,125,50))
    window.blit(rocket , (x,y))
    missile_flight(window,missile_speed)
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

