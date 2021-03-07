# Dungeon screen

image chicken live:
    "chicken def.png"
    pause 1.0
    "chicken alt.png"
    pause 1.0
    repeat
    
init python:
    import pygame
    
    class EnemyState():
        DEAD = 0
        LIVE = 1
        PAIN = 2

    class Chicken(renpy.Displayable):
    
        def __init__(self, x, y, **kwargs):
            super(Chicken, self).__init__(anchor=(0.5,1.0), pos=(x,y), **kwargs)
            
            self.pos = (x, y)
            self.max_health = 6
            self.health = self.max_health
            
            self.animation = renpy.displayable("chicken live")
            self.healthbar = self.build_healthbar(self.health)
            
            self.state = EnemyState.LIVE
            self.last_hit = 0
            
            # to be initialized in render():
            self.bbox = pygame.Rect(0,0,0,0)
            self.d = None
            
        def build_healthbar(self, h):
            huediff = -180.0 + h*180.0/self.max_health
            healthvalue = AnimatedValue(value=h, range=self.max_health, delay=0.25, old_value=self.health)
            healthbar = Bar(value=healthvalue, range=self.max_health, width=180, height=10, ysize=5, xpos=0.5, xanchor=0.5)
            return Transform(healthbar, matrixcolor=HueMatrix(huediff))
            
        def take_damage(self, st):
            if self.health > 0:
                newhealth = self.health -  1
                self.healthbar = self.build_healthbar(newhealth)
                self.health = newhealth
                self.last_hit = st
                
                if newhealth > 0:
                    self.animation = renpy.displayable("chicken pain.png")
                    self.state = EnemyState.PAIN
                else:
                    self.animation = renpy.displayable("chicken drumstick.png")
                    self.state = EnemyState.DEAD
            
        def render(self, width, height, st, at):
            if self.state == EnemyState.PAIN and (st - self.last_hit) >= 1:
                self.state = EnemyState.LIVE
                self.animation = renpy.displayable("chicken live")
            else :
                renpy.redraw(self, 1)
            
            self.d = renpy.displayable(VBox(self.animation, self.healthbar))
            r = renpy.render(self.d, width, height, st, at)
            dims = r.get_size()
            self.bbox = pygame.Rect((0,0), dims)
            
            return r
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and self.bbox.collidepoint(x,y):
                self.take_damage(st)
                renpy.redraw(self, 0)
        
        def per_interact(self):
            pass
        
        def visit(self):
            return [self.d]

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
        
    $ entities = [Chicken(100,600), Chicken(400,600), Chicken(600,600)]
    
    for entity in entities:
        add entity
        