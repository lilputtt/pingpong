from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, speed, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_s] and self.rect.y < 500 - self.height - 5:
            self.rect.y += 5
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if key_pressed[K_DOWN] and self.rect.y < 500 - self.height - 5:
            self.rect.y += 5

clock = time.Clock()

game = True
finish = False

rocket1 = Player('палка.png', 0, 50, 50, 20, 150)
rocket2 = Player('палка.png', 0, 630, 50, 20, 150)
ball = GameSprite('bald.png', 0, 250, 250, 50, 50)

window = display.set_mode((700, 500))
background = transform.scale(image.load('небо.jpeg'), (700, 500))

font.init()
font1 = font.Font(None, 40)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180 , 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180 , 0, 0))

speed_y = 3
speed_x = 3

while game:
    if finish != True:

        window.blit(background, (0,0))

        rocket1.reset()
        rocket1.update_l()
        rocket2.reset()
        rocket2.update_r()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 650:
        finish = True
        window.blit(lose2, (200, 200))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
