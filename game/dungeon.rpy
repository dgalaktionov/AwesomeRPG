# Dungeon screen

image chicken live:
    "chicken def.png"
    pause 1.0
    "chicken alt.png"
    pause 1.0
    repeat

screen dungeon():
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
    
    add "chicken def.png":
        anchor (0.5, 1)
        pos (100, 400)
    
    add "chicken live":
        anchor (0.5, 1)
        pos (400, 400)
        