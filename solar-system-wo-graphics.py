# STARTUP (Don't edit, typically) 
from __future__ import division
from physutil import *
import math
import csv

# VISUALIZATION & GRAPH INITIALIZATION
# ===========================================

# Simple class to replace VPython's sphere
class Planet:
    def __init__(self, pos):
        self.mass = 0
        self.pos = pos
        self.vel = vector(0, 0, 0)

# Setup Display window for visualization 

# Planets
Sun = Planet(pos = vector(0, 0, 0))
Sun.m = 1.989e30

Mercury = Planet(pos = vector(math.cos(math.radians(7)) * 57.9e9, math.sin(math.radians(7)) * 57.9e9, 0))
Venus = Planet(pos = vector(math.cos(math.radians(3.39)) * 108e9, math.sin(math.radians(3.39)) * 108e9, 0))
Earth = Planet(pos = vector(149.6e9, 0, 0))
Mars = Planet(pos = vector(math.cos(math.radians(1.85)) * 228e9, math.sin(math.radians(1.85)) * 228e9, 0))
Jupiter = Planet(pos = vector(math.cos(math.radians(1.3)) * 778e9, math.sin(math.radians(1.3)) * 778e9, 0)) 
Saturn = Planet(pos = vector(math.cos(math.radians(2.49)) * 1430e9, math.sin(math.radians(2.49)) * 1430e9, 0)) 
Uranus = Planet(pos = vector(math.cos(math.radians(0.77)) * 2870e9, math.sin(math.radians(0.77)) * 2870e9, 0)) 
Neptune = Planet(pos = vector(math.cos(math.radians(1.3)) * 4500e9, math.sin(math.radians(1.3)) * 4500e9, 0)) 

planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

# Amount of days to simulate
days = 4332.59

# Planet's position to output
trackedPlanet = Jupiter

Mercury.m = 3.3022e23
Venus.m = 4.8676e24
Earth.m = 5.972e24
Mars.m = 639e21
Jupiter.m = 1.898e27
Saturn.m = 568.3e24
Uranus.m = 86.81e24
Neptune.m = 102.4e24

Mercury.vel = vector(0, 0, -47.87e3)
Venus.vel = vector(0, 0, -35.02e3)
Earth.vel = vector(0, 0, -29.8e3)
Mars.vel = vector(0, 0, -24.077e3)
Jupiter.vel = vector(0, 0, -13.07e3)
Saturn.vel = vector(0, 0, -9.69e3)
Uranus.vel = vector(0, 0, -6.81e3)
Neptune.vel = vector(0, 0, -5.43e3)

deltat = 60*60
t = 0

G = 6.67e-11


def Fgrav(planet):
    Fnet = -G * planet.m * Sun.m / (mag(planet.pos - Sun.pos)**2) * norm(planet.pos - Sun.pos)
    for i in planets:
        if i != planet:
            Fnet += -G * planet.m * i.m / (mag(planet.pos - i.pos)**2) * norm(planet.pos - i.pos)
    return Fnet

while t < deltat * 24 * days:
    for i in planets:
        i.vel = i.vel + (Fgrav(i) / i.m) * deltat
    for i in planets:
        i.pos = i.pos + i.vel * deltat
    t += deltat
    #print(t)
    
print(trackedPlanet.pos)

