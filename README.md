# 2DEngine
A small physics engine written using the Pygame module library. The design of the program takes influence from the classical model of forces interacting with one another and uses the axioms found in Euclidean geometry to determine angles, lines, and collision between a ball and the *cursor* across a two-dimensional plane.

### Installation
  Requires [Python3](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/)
   
  Install [Pygame](https://www.pygame.org/wiki/GettingStarted) using the following in any command line ran as *administrator*:
  > **python3 -m pip install -U pygame**
 
  or
  > **py -m pip install pygame**
  

## *Key Features*
- An **internal clock** that measures the length in which the ball has provided itself abstinence from floor collision; its "*uptime*"
- Visual indicators delineating the **vectors** applied in black, the *cursor's* **distance** from the ball in red, and the **inverse** of the *cursor's* angle from the ball in white 
  - This demonstrates the direct relation between *triangular geometry* and the application of force therein onto an object
- Application of **Newtonian Mechanics** such that the ball's interaction remains inert, predictable, and within realistic preoccupation
  - As the ball collides with a static object, in this case the *cursor* and borders of the screen, an opposite but equal force is applied to the ball
  - The ball is applied with a constant force downwards using a fixed scalar multiplied by its time since last contact to simulate *gravitational acceleration*

## Future Directions 
Several flaws appear in the chosen **method of collision**, where the *cursor* may collide too quickly with the ball and clip through there-on. Additionally, this would cause the algorithms used to calculate *angular velocity* to apply force to the ball at an angle opposite to where the *cursor* was last known approaching (i.e *as the cursor clips from below, a downward force is applied to the ball*). Moving forward from this, a solution may exist in exploring other methods of **collision detection** outside of checking-per-frame, with additional research prescribing the necessary action onward in its own vitality.

## Links
[Pygame Documentation](https://www.pygame.org/docs/)

[Resource Used for Mathematical Application](https://docs.python.org/3/library/math.html)
