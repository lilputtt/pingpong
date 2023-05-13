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

rocket1 = Player('бита.png', 0, 50, 50, 20, 150)
rocket2 = Player('бита.png', 0, 630, 50, 20, 150)

window = display.set_mode((700, 500))
background = transform.scale(image.load('бейп.jpg'), (700, 500))

while game:
    window.blit(background, (0,0))

    rocket1.reset()
    rocket1.update_l()
    rocket2.reset()
    rocket2.update_r()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
