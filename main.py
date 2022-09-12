import pygame, math
import time as tm

pygame.display.init()                                                               # initializes Pygame's video system

screenDimension = int(pygame.display.Info().current_w * 0.5)                        # localizes screen size
win = pygame.display.set_mode((screenDimension, screenDimension))
pygame.display.set_caption("trig demo 5")

pygame.font.init()                                                                  # initializes Pygame's font system


class Ball(object):
    def __init__(self, x, y, radius, endpoint):
        self.x = x                                              # position of the ball on the x axis
        self.y = y                                              # position of the ball on the y axis
        self.radius = radius                                    # radius of the ball
        self.endpoint = endpoint                                # a point that rests on the circumference of the ball
    
    def draw(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)                   # draws the ball       
    
    def drawLine(self):
        pygame.draw.line(win, (255, 255, 255), (self.x, self.y), self.endpoint, 2)          # draws a line opposite to the shortest line drawn between the cursor and the ball
    

def drawText(text, pos):                                            # function used to draw text onto the screen
    render_font = pygame.font.SysFont("corbel", 45)
    blittext = render_font.render(text, 1, (0, 0, 0))
    win.blit(blittext, pos)


def refresh():
    global counter
    
    win.fill([255, 255, 255])                                       # screen fills itself again so as to erase objects rendered from the previous frame
    ent.draw()                                                      # "ent" is an instance of the class Ball
    ent.drawLine()

    pygame.draw.line(win, (255, 0, 0), (ent.x, ent.y), (bx, by), 3)                               # line drawn between the center of "ent" and the cursor
    pygame.draw.line(win, (0, 0, 0), (ent.x, ent.y), (bx, (by - (by - ent.y))))                   # line drawn showing the horizontal component vector
    pygame.draw.line(win, (0, 0, 0), (bx, (by - (by - ent.y))), ((ent.x + (bx - ent.x)), by))     # line drawn showing the vertical component vector

    if ballHit:                                                                                                             # "ballHit" is a boolean signifying whether the ball has been collided with or not
        drawText(str(math.floor(tm.perf_counter() - counter)), (int(screenDimension * 0.5), int(screenDimension * 0.05)))   # draws the timer

def findNewPath(sy, angle, time):                            # estimates the path of the ball based on angle of contact, application of gravity, and a static scalar "power"
    ent.x += round(-math.cos(angle) * bounce * 2)

    velY = -math.sin(angle) * power  
    distY = (velY * time) + ((-3.7 * (time) ** 2) / 2)
    newY = round(sy - distY)

    return newY


def findNewEnd(mx, my, cx, cy):                         # produces a point so that is plotted opposite to another point

    angle = math.atan2(my - cy, mx - cx)
    
    newX = -math.cos(angle) * 40 + cx
    newY = -math.sin(angle) * 40 + cy

    return newX, newY


def findAngle(mx, my):                                  # produces an angle based on the point at which the ball is contacted by the cursor
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

ballHit = False                     # "ballHit" is a boolean signifying whether the ball has been collided with or not

bounce = 1                          # "bounce" represents a number, either 1 or -1, that signifies whether the ball should bounce or not
angle = 0                           # helps calculate the application of gravity over the time elapsed since last the ball was collided with
time = 0
counter = 0                         # simulates an "in-game" timer

ent = Ball(int(screenDimension * 0.5), int(screenDimension * 0.5), int(screenDimension * .04), (int(screenDimension * 0.54), int(screenDimension * 0.5)))   # instantiates an instance "ent" of class Ball
main = True
while main:
    for e in pygame.event.get():                # tells the game to close itself upon hitting the X button
        if e.type == pygame.QUIT:
            main = False
    
    bx, by = pygame.mouse.get_pos()             # returns the position of the cursor
    getKey = pygame.key.get_pressed()           # returns the name of any key pressed

    if getKey[pygame.K_SPACE]:                      # if space is pressed, the ball and timer are reset
        ballHit = False
        ent.x = int(screenDimension * 0.5)
        ent.y = int(screenDimension * 0.5)
        counter += tm.perf_counter() - counter

    if (screenDimension < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == 1:           # determines whether the ball should bounce or not based on its position to either border
        bounce = -1
    elif (screenDimension < ent.x + ent.radius or 0 > ent.x - ent.radius) and bounce == -1:
        bounce = 1

    if bx in range((ent.x - ent.radius), (ent.x + ent.radius)):                         # determines if the cursor is colliding with the ball
        if by in range((ent.y - ent.radius), (ent.y + ent.radius)):
            ballHit = True
            time = 0
            bounce = 1
            y = ent.y
            power = int(screenDimension * 0.06)
            angle = findAngle(bx, by)
    
    if ballHit:                                                             
        if ent.y < screenDimension + ent.radius:                # determines if the ball is still in the air
            time += screenDimension * .00004                    # increments time
            ent.y = findNewPath(y, angle, time)                 # application of gravitational acceleration 
        else:
            ballHit = False                                     # resets ball and timer
            time = 0
            ent.y = int(screenDimension * 0.96)
            counter += tm.perf_counter() - counter
    
    ent.endpoint = findNewEnd(bx, by, ent.x, ent.y)             # calculates the point on the circumference of the ball that is opposite to the position of the cursor

    refresh()                                               # re-renders the screen's objects    
    pygame.display.update()                                 # refreshes the display

pygame.quit()
