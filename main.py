import pygame
pygame.init()


'windows settings'

pygame.display.init()
window = pygame.display.set_mode((1200,1024))


'constant'

'rocket'

x,y = 50 , 50
width , height = 10 , 10
speed = 5
# button = 0


# def rocket_move(x,y,keys):
#     keys = 0
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_d]:
#         x += speed
#     if keys[pygame.K_a]:
#         x -= speed
#     if keys[pygame.K_w]:
#         y -= speed
#     if keys[pygame.K_s]:
#         y += speed
#
#     keys = []

'main loop'

while True:
    pygame.time.delay(20)
    pygame.display.update()
    window.fill((46,125,50))
    pygame.draw.rect(window, (78, 52, 46), (x, y, width, height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # rocket_move(x,y,button)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

    keys = []

