# Shop screen

init python:
    items = [{"name": "Rusty Knife", "price": 5},
        {"name": "Rusty Axe", "price": 20},
        {"name": "Short Sword", "price": 50},
        {"name": "Sharp Spear", "price": 100}]

screen shop():
    tag awesomerpg
    
    add Solid("#000")
    
    frame:
        align (1.0, 0.0)
        right_margin 40
        top_margin 100
        xsize 300
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
    
    