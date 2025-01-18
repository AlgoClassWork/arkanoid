from pygame import *

window = display.set_mode((700,500))
display.set_caption('Арканойд')

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

platform = GameSprite('platform.png', 350, 450)
ball = GameSprite('ball.png', 300, 300)

monsters = sprite.Group()
start_x, start_y, count = 20, 5, 9
for i in range(3): 
    y = start_y + (55 * i) 
    x = start_x + (35 * i) 

    for i in range(count):
        monster = GameSprite('enemy.png', x, y)
        monsters.add(monster)
        x += 75

    count -= 1
    
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((155,255,255))
    platform.reset()
    ball.reset()
    monsters.draw(window)

    display.update()
