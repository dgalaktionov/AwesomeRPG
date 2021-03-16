# Shop screen

init python:
    items = [{"name": "Rusty Knife", "price": 5},
        {"name": "Rusty Axe", "price": 20},
        {"name": "Short Sword", "price": 50},
        {"name": "Sharp Spear", "price": 100}]

screen shop():
    tag awesomerpg
    
    add Solid("#000")
    
    add Solid("#FFF"):
        ysize 4
        xsize 600
        ypos 380
        
    add Solid("#FFF"):
        ysize 6
        xsize 650
        ypos 460
        
    add Solid("#FFF"):
        ysize 4
        xsize 97
        xpos 576
        ypos 375
        rotate 58.0
        
    add Solid("#FFF"):
        xsize 6
        xpos 645
        ypos 462
    
    add "merchant":
        xsize 600
        ysize 450
    
    frame:
        align (1.0, 0.0)
        right_margin 80
        top_margin 100
        xsize 360
        vbox:
            text "Awesome Shop":
                size 32
                
            null height 25
        
            for i in items:
                hbox:
                    xfill True
                    text i["name"]
                    text "[i[price]]$":
                        xalign 1.0

    add moneyCounter
    
    