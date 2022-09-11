import pygame, math
import time as tm

win = pygame.display.set_mode((1000, 1000))    # initializes the screen
pygame.display.set_caption("trig demo 5") 
pygame.font.init()                             # initializes Pygame's font directory
clock = pygame.time.Clock()


class Ball(object):
    def __init__(self, x, y, radius, endpoint):
        self.x = x                                      # position of the ball on the x axis
        self.y = y                                      # position of the ball on the y axis
        self.radius = radius                            # radius of the ball
        self.endpoint = endpoint                        # a point that rests on the circumference of the ball
    
    def draw(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)                # draws the ball
    
    def drawLine(self):
        pygame.draw.line(win, (255, 255, 255), (self.x, self.y), self.endpoint, 2)       # draws a line opposite to the shortest line drawn between the cursor and the ball


def drawText(text, pos):                                                                 # function used to draw text onto the screen
    render_font = pygame.font.SysFont("corbel", 45)
    blittext = render_font.render(text, 1, (0, 0, 0))
    win.blit(blittext, pos)


def refresh():
    global counter
    
    win.fill([255, 255, 255])                                                            # screen is made white
    ent.draw()                                                                           # "ent" is an instance of the class Ball
    ent.drawLine()

    pygame.draw.line(win, (255, 0, 0), (ent.x, ent.y), (bx, by), 3)                               # line drawn between the center of "ent" and the cursor
    pygame.draw.line(win, (0, 0, 0), (ent.x, ent.y), (bx, (by - (by - ent.y))))                   # line drawn showing the horizontal component vector
    pygame.draw.line(win, (0, 0, 0), (bx, (by - (by - ent.y))), ((ent.x + (bx - ent.x)), by))     # line drawn showing the vertical component vector

    if ballHit:                                                                          # "ballHit" is a boolean signifying whether the ball has been collided with or not
        drawText(str(math.floor(tm.perf_counter() - counter)), (500, 50))                # starts the timer

def findNewPath(sy, angle, time):                                                        # estimates the path of the ball based on angle of contact, application of gravity, and a static scalar "power"
    ent.x += round(-math.cos(angle) * bounce * 2)

    velY = -math.sin(angle) * power  
    distY = (velY * time) + ((-3.7 * (time) ** 2) / 2)
    newY = round(sy - distY)

    return newY


def findNewEnd(mx, my, cx, cy):                                       # produces a point so that is plotted opposite to another point

    angle = math.atan2(my - cy, mx - cx)
    
    newX = -math.cos(angle) * 40 + cx
    newY = -math.sin(angle) * 40 + cy

    return newX, newY


def findAngle(mx, my):                                      # produces an angle based on the point at which the ball is contacted by the cursor
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

ballHit = False                                           # "ballHit" is a boolean signifying whether the ball has been collided with or not

bounce = 1                                                # "bounce" represents a number from 1 to -1 that signifies whether the ball should bounce left or right after colliding with a border                                              
angle = 0
time = 0                                                  # helps calculate the application of gravity over the time elapsed since last the ball was collided with
y = 0
counter = 0

ent = Ball(500, 500, 40, (540, 500))
main = True
while main:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            main = False
    
    bx, by = pygame.mouse.get_pos()
    getKey = pygame.key.get_pressed()

    if getKey[pygame.K_SPACE]:
        ballHit = False
        ent.x = 500
        ent.y = 500
        counter += tm.perf_counter() - counter

    if (1000 < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == 1:
        bounce = -1
    elif (1000 < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == -1:
        bounce = 1

    if bx in range((ent.x - ent.radius), (ent.x + ent.radius)):
        if by in range((ent.y - ent.radius), (ent.y + ent.radius)):
            ballHit = True
            time = 0
            bounce = 1
            y = ent.y
            power = 60
            angle = findAngle(bx, by)
    
    if ballHit:
        if ent.y < 1000 + ent.radius:
            time += 0.04
            ent.y = findNewPath(y, angle, time)
        else:
            ballHit = False
            time = 0
            ent.y = 960
            counter += tm.perf_counter() - counter
    
    refresh()
    ent.endpoint = findNewEnd(bx, by, ent.x, ent.y)

    pygame.display.update()

pygame.quit()
