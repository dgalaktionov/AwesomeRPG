# Dungeon screen

image chicken live:
    "chicken def.png"
    pause 1.0
    "chicken alt.png"
    pause 1.0
    repeat
    
image chicken hit:
    "chicken pain.png"
    pause 1.0
    repeat
    
image chicken dead:
    "chicken drumstick.png"
    
image cloud live:
    "monstur.png"
    pause 1.0
    "monstur2.png"
    pause 1.0
    repeat
    
image cloud hit:
    "monstur pain.png"
    pause 1.0
    repeat
    
image cloud dead:
    "monstur pain.png"

init python:
    import pygame
    
    class EnemyState():
        DEAD = 0
        LIVE = 1
        PAIN = 2

    class Enemy(renpy.Displayable):
    
        def __init__(self, x, y, prefix, max_health=10, reward=1, **kwargs):
            super(Enemy, self).__init__(anchor=(0.5,1.0), pos=(x,y), **kwargs)
            
            self.prefix = prefix
            self.max_health = max_health
            self.health = self.max_health
            self.reward = reward
            
            self.animation = renpy.displayable(self.prefix + " live")
            self.healthbar = self.build_healthbar(self.health)
            
            self.state = EnemyState.LIVE
            self.last_hit = 0
            
            # to be initialized in render():
            self.hitbox = pygame.Rect(0,0,0,0)
            self.d = Null()
            
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
                    self.animation = renpy.displayable(self.prefix + " hit")
                    self.state = EnemyState.PAIN
                else:
                    self.animation = renpy.displayable(self.prefix + " dead")
                    self.state = EnemyState.DEAD
                    inc_money(self.reward)
            
        def render(self, width, height, st, at):
            if self.state == EnemyState.PAIN and (st - self.last_hit) >= 1:
                self.state = EnemyState.LIVE
                self.animation = renpy.displayable(self.prefix + " live")
            
            self.d = renpy.displayable(VBox(self.animation, self.healthbar))
            r = renpy.render(self.d, width, height, st, at)
            dims = r.get_size()
            self.hitbox = pygame.Rect((0,0), dims)
            
            return r
        
        def event(self, ev, x, y, st):
            global player, moneyCounter
            
            if ev.type == pygame.MOUSEBUTTONDOWN and self.hitbox.collidepoint(x,y):
                self.take_damage(st)
                renpy.redraw(self, 0)
        
        def per_interact(self):
            pass
        
        def visit(self):
            return [self.d]
            
            
    class Chicken(Enemy):
        def __init__(self, x, y, **kwargs):
            super(Chicken, self).__init__(x,y, "chicken", max_health=6, reward=2, **kwargs)
            
    class Cloud(Enemy):
        def __init__(self, x, y, **kwargs):
            super(Cloud, self).__init__(x,y, "cloud", max_health=4, **kwargs)
            
        def take_damage(self, st):
            super(Cloud, self).take_damage(st)
            
            # disappear when dead
            if self.state == EnemyState.DEAD:
                self.animation = Null()
                self.healthbar = Null()

screen dungeon():
    tag awesomerpg
    
    default initialized = False

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
    
    
    $ entities = [Cloud(200,250), Cloud(500,350), Cloud(1000,250), 
        Chicken(100,600), Chicken(400,600), Chicken(600,600)]
    
    for entity in entities:
        add entity
    
    add moneyCounter
    