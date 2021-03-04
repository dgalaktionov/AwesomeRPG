# Dungeon screen

image chicken live:
    "chicken def.png"
    pause 1.0
    "chicken alt.png"
    pause 1.0
    repeat

init python:
    class Chicken(renpy.Displayable):
    
        def __init__(self, x, y, **kwargs):
            super(Chicken, self).__init__(anchor=(0.5,1), pos=(x,y), **kwargs)
            
            #self.pos = (x, y)
            #self.exists = True
            self.d = renpy.displayable(ImageReference("chicken live"))
            
        def render(self, width, height, st, at):
            return renpy.render(self.d, width, height, st, at)

screen dungeon():
    tag awesomerpg

    add Solid("#000")
    
    text _("Dungeon Level 1") id "dun_title":
        xalign 0.5
        ypos 20
        size 40
    
    textbutton _("Skip") action Return(0):
        align (1.0, 1.0)
        xpadding 10
        ypadding 10
    
    add Solid("#FFF"):
        ysize 4
        yalign 0.5
        
    $ entities = [Chicken(100,400), Chicken(400,400), Chicken(600,400)]
    
    for entity in entities:
        add entity
        