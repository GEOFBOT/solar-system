# STARTUP (Don't edit, typically) 
from __future__ import division
from visual import *
from physutil import *
import math
import csv

# VISUALIZATION & GRAPH INITIALIZATION
# ===========================================

# Setup Display window for visualization 
scene = display(width = 800, height = 600, range = 5e11, background = color.black, title = "Solar System by Geoffrey Mon")

smallPlanetMultiplier = 1000
largePlanetMultiplier = 500
sunMultiplier = 10

# Planets
Sun = sphere(pos = vector(0, 0, 0), material = materials.texture(materials.loadTGA("tex/sun.tga"), mapping = "spherical"), radius = 1.391e9 * sunMultiplier)
Sun.m = 1.989e30

Mercury = sphere(pos = vector(math.cos(math.radians(7)) * 57.9e9, math.sin(math.radians(7)) * 57.9e9, 0), material = materials.texture(materials.loadTGA("tex/mercury.tga"), mapping = "spherical"), radius = 2.44e6 * smallPlanetMultiplier)
Venus = sphere(pos = vector(math.cos(math.radians(3.39)) * 108e9, math.sin(math.radians(3.39)) * 108e9, 0), material = materials.texture(materials.loadTGA("tex/venus.tga"), mapping = "spherical"), radius = 6.05e6 * smallPlanetMultiplier)
Earth = sphere(pos = vector(149.6e9, 0, 0), material = materials.BlueMarble, radius = 6.4e6 * smallPlanetMultiplier)
Mars = sphere(pos = vector(math.cos(math.radians(1.85)) * 228e9, math.sin(math.radians(1.85)) * 228e9, 0), material = materials.texture(materials.loadTGA("tex/mars.tga"), mapping = "spherical"), radius = 3.395e6 * smallPlanetMultiplier)
Jupiter = sphere(pos = vector(math.cos(math.radians(1.3)) * 778e9, math.sin(math.radians(1.3)) * 778e9, 0), material = materials.texture(materials.loadTGA("tex/jupiter.tga"), mapping = "spherical"), radius = 71.5e6 * largePlanetMultiplier)
Saturn = sphere(pos = vector(math.cos(math.radians(2.49)) * 1430e9, math.sin(math.radians(2.49)) * 1430e9, 0), material = materials.texture(materials.loadTGA("tex/saturn.tga"), mapping = "spherical"), radius = 60e6 * largePlanetMultiplier)
Uranus = sphere(pos = vector(math.cos(math.radians(0.77)) * 2870e9, math.sin(math.radians(0.77)) * 2870e9, 0), material = materials.texture(materials.loadTGA("tex/uranus.tga"), mapping = "spherical"), radius = 25.9e6 * largePlanetMultiplier)
Neptune = sphere(pos = vector(math.cos(math.radians(1.3)) * 4500e9, math.sin(math.radians(1.3)) * 4500e9, 0), material = materials.texture(materials.loadTGA("tex/neptune.tga"), mapping = "spherical"), radius = 24.75e6 * largePlanetMultiplier)

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

Uranus.rotate(angle = radians(97), axis = (0, 0, 1)) # Poor Uranus, tilted like that...

trailRadius = 1e5 * smallPlanetMultiplier

trailMercury = curve(color = color.white, radius = trailRadius)
trailVenus = curve(color = color.white, radius = trailRadius)
trailEarth = curve(color = color.white, radius = trailRadius)
trailMars = curve(color = color.white, radius = trailRadius)
trailJupiter = curve(color = color.white, radius = trailRadius)
trailSaturn = curve(color = color.white, radius = trailRadius)
trailUranus = curve(color = color.white, radius = trailRadius)
trailNeptune = curve(color = color.white, radius = trailRadius)
trails = [trailMercury, trailVenus, trailEarth, trailMars, trailJupiter, trailSaturn, trailUranus, trailNeptune]

deltat = 60*60
t = 0

G = 6.67e-11

focuses = [Sun] + planets
focusIndex = 0
currentFocus = focuses[focusIndex]

scene.autocenter = False
scene.autoscale = False

def changeFocus(evt):
    global focusIndex
    global currentFocus
    if focusIndex < 8:
        focusIndex += 1
    else:
        focusIndex = 0
    currentFocus = focuses[focusIndex]
    print("Focus changed to planet " + str(focusIndex))
#    print(currentFocus.pos)
    scene.center = currentFocus.pos

scene.bind('click', changeFocus)

def Fgrav(planet):
    Fnet = -G * planet.m * Sun.m / (mag(planet.pos - Sun.pos)**2) * norm(planet.pos - Sun.pos)
    for i in planets:
        if i != planet:
            Fnet += -G * planet.m * i.m / (mag(planet.pos - i.pos)**2) * norm(planet.pos - i.pos)
    return Fnet

while t < deltat * 24 * days:
    scene.visible = False
    scene.center = currentFocus.pos
    for i in planets:
        i.vel = i.vel + (Fgrav(i) / i.m) * deltat
        i.pos = i.pos + i.vel * deltat
        trails[planets.index(i)].append(i.pos)
    t += deltat
    rate(500)
    

print(trackedPlanet.pos)

