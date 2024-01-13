import pygame
import math
import random
import gc


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
        self.angel = angel

    def drow(self):
        self.coor()
        pygame.draw.circle(screen, self.color, (self.x, -self.y), 10,5)

        # print('x=', self.x, 'y=', self.y, 'vx=', self.vx, 'vy=', self.vx)
    def coor(self):

        self.y = self.y0 + self.vy * self.t + gravity * self.t ** 2 / 2

        self.x = self.x0 + self.vx * self.t
        # print('x=', self.x, 'y=', self.y)
        # if (self.x-400)**2+(self.y-300)**2 >= 200**2:

        if self.x-self.y <= sum(pos1):
            a = 225
            self.maths(a)
            self.x = sum(pos1)+5+self.y

        if self.x-self.y >= sum(pos3):
            a = 45
            self.maths(a)
            self.x = sum(pos3) + self.y

        if -self.y-self.x >= pos2[1]-pos2[0]:
            a = 135
            self.maths(a)
            self.x =  -self.y-145


        if self.x+self.y >= pos1[0]-pos1[1]:
            a = 315
            self.maths(a)
            self.x = 345 - self.y

        self.t += 1


    def maths(self, a):
        if self.vy*self.t == 0:
            self.angel = 180
        else:
            self.angel = math.degrees(math.atan(self.vx/(self.vy*self.t)))
        self.v = math.sqrt((self.vy + gravity * self.t) ** 2 + self.vx ** 2)
        if abs(self.angel)<45:
            self.vx = -self.v * math.sin(math.radians(2 * a - self.angel))
            self.vy = -self.v * math.cos(math.radians(2 * a - self.angel))
            self.angel = 2 * a - self.angel
        else:
            self.vx = -self.v * math.cos(math.radians(3*self.angel-2*a))
            self.vy = -self.v * math.sin(math.radians(3*self.angel-2*a))
            self.angel = 3*self.angel-2*a

        self.x0 = self.x
        self.y0 = self.y

        self.t = 0

        if self.y < -550:
            self.y = -540
            self.x = 400
            print('f')


        s.play()


    def __del__(self):
        print('Шар уничтожен!')








# def lil_circle(x,y,t):
#
#     pygame.draw.circle(screen, (255, 189, 211), (x, y), 7)




gravity = -0.5
s = pygame.mixer.Sound('6669.mp3')

diamondWidth = 500
diamondHeight = 500
pos1 = (WIDTH/2, HEIGHT/2 - diamondHeight/2)
pos2 = (pos1[0] - diamondWidth/2, pos1[1] + diamondHeight/2)
pos3 = (pos1[0], pos1[1]+diamondHeight)
pos4 = (pos2[0]+diamondWidth, pos2[1])
points = [pos1, pos2, pos3, pos4]
print(points)

c = []


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                c1 = lil_circle(x0=event.pos[0],
                                y0=-event.pos[1],
                                v0=random.randrange(0, 10),
                                angel=random.randrange(-90, 90),
                                color=list(random.randrange(256) for _ in range(3)))
                c.append(c1)
                print(f'x0={event.pos[0]}, y0={event.pos[1]}')


    screen.fill((0, 0, 0))
    # большая окружность
    # pygame.draw.circle(screen, (255, 189, 211), (400, 300), 200, 5)
    # pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400), 3)
    pygame.draw.polygon(screen, (255, 255, 255), points, 3)

    for c1 in c:
        if c1.y0 > -550:
            c1.drow()
        else:
            del c1








    # if c1.y >= 485:
    #     c1.v0 = -c1.v
    #     t = 0
    # else:
    #     v = c1.v0 + gravity * c1.t / 2







    pygame.display.flip()
    clock.tick(60)