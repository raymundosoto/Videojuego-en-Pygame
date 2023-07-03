import pygame
import math
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Mover misil con mouse")

pygame.mixer.init()
sound = pygame.mixer.Sound('missilLaunch.mp3')
sound_lock = pygame.mixer.Sound('A_missile_lock.mp3')

img1 = pygame.image.load('misil22A.png')
pos_x = 400
pos_y = 300
speed = 5  # Ajusta la velocidad según tus necesidades
done = False
bg = (0, 200, 122)

follow_mouse = False  # Variable para controlar si el misil sigue el puntero del mouse
fire_missile = False  # Variable para controlar si el misil se dispara hacia adelante
direction_x = 1  # Dirección inicial del misil en el eje x
direction_y = 0  # Dirección inicial del misil en el eje y
lock_sound_active = False  # Variable para controlar si el sonido de "missil_lock.mp3" está activo

font = pygame.font.Font(None, 36)
text_render_1 = font.render("Posición de la nave", True, (255, 255, 0))
text_render_2 = font.render("Angulo de la nave", True, (255, 255, 0))
text_render_3 = font.render("0, 0", True, (255,255,0))
text_render_4 = font.render("0°", True, (255,255,0))
text_render_5 = font.render("Velocidad de la nave", True, (255,255,0))
text_render_6 = font.render("0", True, (255,255,0))



fondo = pygame.image.load("space.png")
fondo = pygame.transform.scale(fondo, (1000,700))

i = 0

while not done:
    
    
    screen.blit(fondo,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del mouse
                if not lock_sound_active:
                    if follow_mouse:
                        follow_mouse = False
                    else:
                        follow_mouse = True
                        if not fire_missile:
                            sound_lock.play()
                        else:
                            sound_lock.stop()
                            lock_sound_active = False
                else:
                    lock_sound_active = False

            elif event.button == 3:  # Botón derecho del mouse
                if not fire_missile:
                    fire_missile = True
                    follow_mouse = True
                    sound.play()
                else:
                    fire_missile = False

    if follow_mouse:
        mx, my = pygame.mouse.get_pos()
        
        
        dx = mx - pos_x
        dy = my - pos_y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            direction_x = dx / distance
            direction_y = dy / distance
            pos_x += direction_x * speed
            pos_y += direction_y * speed

    img_width, img_height = img1.get_size()
    img_pos_x = pos_x - img_width / 2
    img_pos_y = pos_y - img_height / 2

    mx, my = pygame.mouse.get_pos()
    dx = mx - pos_x
    dy = my - pos_y
    img_rotated = pygame.transform.rotate(img1, math.degrees(math.atan2(-dy, dx)))
    angulo = math.degrees(math.atan2(-dy, dx))
    screen.blit(img_rotated, (img_pos_x, img_pos_y))
    
    text_render_3 = font.render("{:.2f}, {:.2f}".format(img_pos_x, img_pos_y), True, (255,255,0))
    text_render_4 = font.render("{:.2f}°".format(angulo), True, (255,255,0))
    text_render_6 = font.render("warp {:.2f}".format(float(speed)), True, (255,255,0))
    
    
    
    screen.blit(text_render_1, (10, 10))
    screen.blit(text_render_2, (300, 10))
    screen.blit(text_render_3, (50,50))
    screen.blit(text_render_4, (380,50))
    screen.blit(text_render_5, (550,10))
    screen.blit(text_render_6, (620,50))

    pygame.display.update()

pygame.quit()
exit()