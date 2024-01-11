import pygame
import math
import random

WIDTH = 800
HEIGHT = 600



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False


class lil_circle():
    def __init__( self,x0,y0, angel, v0, color):
        self.x0 = x0
        self.y0 = y0
        self.t = 0
        self.v0 = v0
        self.vx = math.sin(math.radians(angel))*self.v0
        self.vy = math.cos(math.radians(angel))*self.v0
        self.color = color

    def drow(self):
        self.coor()
        pygame.draw.circle(screen, self.color, (self.x, -self.y), 7,3)

    def coor(self):

        self.v = self.vy + gravity * self.t
        self.y = self.y0 + self.vy * self.t + gravity * self.t ** 2 / 2

        self.x = self.x0 + self.vx*self.t

        # if (self.x-400)**2+(self.y-300)**2 >= 200**2:
        if self.y<=-500+3 or self.y>=-100-3:

            self.t = 0
            self.vy = -self.v
            self.y0 = self.y
            self.x0 = self.x
            self.y = -500+3 if self.y<=-500+3 else -100-3

        if self.x >= 700-3 or self.x <= 100+3:
            self.t = 0
            self.vx = -self.vx
            self.vy = self.v
            self.y0 = self.y
            self.x0 = self.x

            self.x = 700-3  if self.x >= 700-3 else 100+3

        self.t += 1


# def lil_circle(x,y,t):
#
#     pygame.draw.circle(screen, (255, 189, 211), (x, y), 7)




gravity = -0.5

c = []
for i in range(10):
    c1 = lil_circle(x0 = random.randrange(100,700),
                    y0 = random.randrange(-500,-100),
                    v0=random.randrange(0,10),
                    angel=random.randrange(-90,90),
                    color = list(random.randrange(256) for _ in range(3)))
    c.append(c1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    screen.fill((0, 0, 0))
    # большая окружность
    # pygame.draw.circle(screen, (255, 189, 211), (400, 300), 200, 5)
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400), 3)

    o = 0
    for c1 in c:
        c1.drow()
        o+=1
        print(f'{o}) x={c1.x}, y={c1.y}')



    # if c1.y >= 485:
    #     c1.v0 = -c1.v
    #     t = 0
    # else:
    #     v = c1.v0 + gravity * c1.t / 2







    pygame.display.flip()
    clock.tick(60)