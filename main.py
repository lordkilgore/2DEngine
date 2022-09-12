import pygame, math
from pyautogui import size
import time as tm

screenDimension = int(size()[1] * 0.8)
win = pygame.display.set_mode((screenDimension, screenDimension))
pygame.display.set_caption("trig demo 5")
pygame.font.init()
clock = pygame.time.Clock()


class Ball(object):
    def __init__(self, x, y, radius, endpoint):
        self.x = x
        self.y = y
        self.radius = radius
        self.endpoint = endpoint
    
    def draw(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
    
    def drawLine(self):
        pygame.draw.line(win, (255, 255, 255), (self.x, self.y), self.endpoint, 2)


def drawText(text, pos):
    render_font = pygame.font.SysFont("corbel", 45)
    blittext = render_font.render(text, 1, (0, 0, 0))
    win.blit(blittext, pos)


def refresh():
    global counter
    
    win.fill([255, 255, 255])
    ent.draw()
    ent.drawLine()

    pygame.draw.line(win, (255, 0, 0), (ent.x, ent.y), (bx, by), 3)
    pygame.draw.line(win, (0, 0, 0), (ent.x, ent.y), (bx, (by - (by - ent.y))))
    pygame.draw.line(win, (0, 0, 0), (bx, (by - (by - ent.y))), ((ent.x + (bx - ent.x)), by))

    if ballHit:
        drawText(str(math.floor(tm.perf_counter() - counter)), (int(screenDimension * 0.5), int(screenDimension * 0.05)))

def findNewPath(sy, angle, time):
    ent.x += round(-math.cos(angle) * bounce * 2)

    velY = -math.sin(angle) * power  
    distY = (velY * time) + ((-3.7 * (time) ** 2) / 2)
    newY = round(sy - distY)

    return newY


def findNewEnd(mx, my, cx, cy):

    angle = math.atan2(my - cy, mx - cx)
    
    newX = -math.cos(angle) * 40 + cx
    newY = -math.sin(angle) * 40 + cy

    return newX, newY


def findAngle(mx, my):
    sX = ent.x
    sY = ent.y
    try:
        angle = math.atan((sY - my) / (sX - mx))
    except:
        angle = math.pi / 2

    if my < sY and mx > sX:
        angle = abs(angle)
    elif my < sY and mx < sX:
        angle = math.pi - angle
    elif my > sY and mx > sX:
        angle = (math.pi * 2) - angle
    elif my > sY and mx < sX:
        angle = math.pi + abs(angle)

    return angle

ballHit = False

bounce = 1
angle = 0
time = 0
counter = 0

ent = Ball(int(screenDimension * 0.5), int(screenDimension * 0.5), int(screenDimension * .04), (int(screenDimension * 0.54), int(screenDimension * 0.5)))
main = True
while main:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            main = False
    
    bx, by = pygame.mouse.get_pos()
    getKey = pygame.key.get_pressed()

    if getKey[pygame.K_SPACE]:
        ballHit = False
        ent.x = int(screenDimension * 0.5)
        ent.y = int(screenDimension * 0.5)
        counter += tm.perf_counter() - counter

    if (screenDimension < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == 1:
        bounce = -1
    elif (screenDimension < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == -1:
        bounce = 1

    if bx in range((ent.x - ent.radius), (ent.x + ent.radius)):
        if by in range((ent.y - ent.radius), (ent.y + ent.radius)):
            ballHit = True
            time = 0
            bounce = 1
            y = ent.y
            power = int(screenDimension * 0.06)
            angle = findAngle(bx, by)
    
    if ballHit:
        if ent.y < screenDimension + ent.radius:
            time += screenDimension * .00004
            ent.y = findNewPath(y, angle, time)
        else:
            ballHit = False
            time = 0
            ent.y = int(screenDimension * 0.96)
            counter += tm.perf_counter() - counter
    
    refresh()
    ent.endpoint = findNewEnd(bx, by, ent.x, ent.y)

    pygame.display.update()

pygame.quit()
