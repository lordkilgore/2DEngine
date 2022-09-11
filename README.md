# 2DEngine
A small physics engine written using the Pygame module library. The design of the program takes influence from the classical model of forces interacting with one another and uses the axioms found in Euclidean geometry to determine angles, lines, and collision between a ball and the *cursor* across a two-dimensional plane.

## *Key Features*
- An **internal clock** that measures the length in which the ball has provided itself abstinence from floor collision; its "*uptime*"
- Visual indicators delineating the **vectors** applied in black, the *cursor's* **distance** from the ball in red, and the **inverse** of the *cursor's* angle from the ball in white 
  - This demonstrates the direct relation between *triangular geometry* and the application of force therein onto an object
- Application of **Newtonian Mechanics** such that the ball's interaction remains inert, predictable, and within realistic preoccupation
  - As the ball collides with a static object, in this case the *cursor* and borders of the screen, an opposite but equal force is applied to the ball
  - The ball is applied with a constant force downwards using a fixed scalar multiplied by its time since decline to simulate *gravitational acceleration*
