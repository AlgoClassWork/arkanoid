from pygame import *

window = display.set_mode((500,500))
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
speed_x, speed_y = 5, 5

monsters = sprite.Group()
start_x, start_y, count = 5, 5, 9
for i in range(3): 
    y = start_y + (55 * i) 
    x = start_x + (28 * i) 

    for i in range(count):
        monster = GameSprite('enemy.png', x, y)
        monsters.add(monster)
        x += 55

    count -= 1

clock = time.Clock()
    
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((155,255,255))

    platform.reset()
    ball.reset()

    monsters.draw(window)

    mouse_x, mouse_y = mouse.get_pos()
    platform.rect.centerx = mouse_x

    ball.rect.x += speed_x 
    ball.rect.y += speed_y

    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1

    if sprite.collide_rect(platform,ball) or ball.rect.y < 0:
        speed_y *= -1

    if sprite.spritecollide(ball, monsters, True):
        speed_y *= -1

    display.update()
    clock.tick(60)
