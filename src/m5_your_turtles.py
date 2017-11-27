"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Megan Hawksworth.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
Justin = rg.SimpleTurtle('turtle')
Justin.pen = rg.Pen('OrangeRed',2)
Justin.speed = 20
size = 155

for k in range(20):

    Justin.draw_circle(size)
    Justin.pen_up()
    Justin.left(18)
    Justin.pen_down()


Zach = rg.SimpleTurtle('turtle')
Zach.pen = rg.Pen('cyan3',2)
Zach.speed = 1000000000
size = 0

for k in range(133):

    Zach.forward(size)
    Zach.pen_up()
    Zach.left(12)
    Zach.pen_down()
    size = size+0.5



window.close_on_mouse_click()