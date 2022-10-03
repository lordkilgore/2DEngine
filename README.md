# 2DEngine
A small physics engine written using the Pygame module library. The design of the program is influenced by the classical model of forces interacting with one another, and uses the axioms found in Euclidean geometry to determine angles, key points, and collision between a ball and the *cursor* across a two-dimensional plane.

### Installation
  Requires [Python3](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/)
   
  Install [Pygame](https://www.pygame.org/wiki/GettingStarted) using the following in any command line ran as *administrator*:
  > **python3 -m pip install -U pygame**
 
  or
  > **py -m pip install pygame**
  

## *Key Features*
- An **internal clock** that measures the length of time start from which the ball has not collided with the floor; its "*uptime*"
- Visual indicators delineating the **vector components** applied in black, the *cursor's* **distance** from the ball in red, and the **inverse** of the *cursor's* angle from the ball in white 
  - This demonstrates the direct relation between *triangular geometry* and the application of force therein onto an object
- Application of **Newtonian Mechanics** such that the ball's interaction remains inert, predictable, and within realistic preoccupation
  - As the ball collides with a static object, in this case the *cursor* and borders of the screen, an opposite but equal force is applied to the ball
  - The ball is applied with a constant force downwards using a fixed scalar multiplied by its time since last contact to simulate *gravitational acceleration*

![](https://media0.giphy.com/media/qU9r485kQntWCwgWzh/giphy.gif?cid=790b7611ca4c1be972cba6f5843bb3bddf0cab5d6eb73a70&rid=giphy.gif&ct=g)

## Future Directions 
Several flaws appear in the chosen **method of collision**, where the *cursor* may collide too quickly and clip through the ball. As a result, the algorithms responsible for calculating *angular direction* malfunction and move the ball based on the position of the cursor while it is *inside* the ball, as opposed to the *surface* of the ball (i.e *as the cursor clips from below, a downward force is applied to the ball*). Moving forward, exploring other strategies to **detect collision** outside of checking-per-frame would prevent this from occurring. 

For further optimization, more work can be put into cleaning up and organizing the structure of the code. This is especially apparent in the **localization of the screen's display**, where values are often shown as the screen's native display adjusted by an arbitrary scalar, converted into an integer. With this in mind, an opportunity to increase maintainability might include assigning these values to descriptive **variables** to indicate that they are not fixed, but *mutable* values.

## Links
[Pygame Documentation](https://www.pygame.org/docs/)

[Resource Used for Mathematical Application](https://docs.python.org/3/library/math.html)
