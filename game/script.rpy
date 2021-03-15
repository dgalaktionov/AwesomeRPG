# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default player = {"money": 0}

init python:

    class Money(renpy.Displayable):
        
        def __init__(self, **kwargs):
            super(Money, self).__init__(align=(1.0,0.0), **kwargs)
            
        def render(self, width, height, st, at):
            d = Text("$%d" % (player["money"]), size=32)
            return renpy.render(d, width, height, st, at)
            
    moneyCounter = Money()
    
    def inc_money(by):
        player["money"] += by
        renpy.redraw(moneyCounter, 0)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    
    window hide
    
    call screen dungeon
    
    window show

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
