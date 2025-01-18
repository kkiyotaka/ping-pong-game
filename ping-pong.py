from pygame import *
from random import choice
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = [1, 0] 

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed     

window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Пинг-понг')

background = transform.scale(image.load('background1.jpg'), (700, 500))
racketL = Player('racket.png', 4, 5, 200)
racketR = Player('racket.png', 4, 645, 200)
ball = GameSprite('tennis_ball.png', 4, 350, 250)
font = font.Font(None, 36)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        racketL.reset()
        racketL.update_l()
        racketR.reset()
        racketR.update_r()
        ball.update()
        ball.reset()

        if ball.rect.colliderect(racketL.rect) or ball.rect.colliderect(racketR.rect):
            ball.direction[0] = -ball.direction[0]  
            ball.direction[1] = choice([-1, 1]) 

        if ball.rect.top <= 0 or ball.rect.bottom >= 500:
            ball.direction[1] = -ball.direction[1]  

        if ball.rect.x < 0:
            L_win = font.render('ПОБЕДИЛА ПРАВАЯ СТОРОНА', False, (0, 255, 0))
            window.blit(L_win, (150, 225))
            finish = True
        if ball.rect.x > 700:
            R_win = font.render('ПОБЕДИЛА ЛЕВАЯ СТОРОНА', False, (0, 255, 0))
            window.blit(R_win, (150, 225))
    display.flip()
    clock.tick(60)
