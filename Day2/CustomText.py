import pygame

pygame.init()
screen_width = 1800
screen_height = 200
screen = pygame.display.set_mode((screen_width,screen_height))

done = False
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

pygame.font.init()
# font = pygame.font.Font('../fonts/Doctor Glitch.otf', 80)
font2 = pygame.font.Font('../fonts/Salsa-Regular.ttf', 80)
text = font2.render('Jatin Suyal', False, white)
text2 = font2.render('Graphic Programming Enthusiast', False, red)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x = (screen_width - text.get_width()) / 2
    y = (screen_height - text.get_height()) / 2
    screen.blit(text, (x, y))
    screen.blit(text2, (10, 10))
    pygame.display.update()
pygame.quit()
