from pygame import *

window = display.set_mode((500,500))

class GameSprite():
    def __init__(self, img, x, y):
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

platform = GameSprite('platform.png', 200, 450)
ball = GameSprite('ball.png', 200, 300)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((155,255,255))
    platform.reset()
    ball.reset()

    display.update()
