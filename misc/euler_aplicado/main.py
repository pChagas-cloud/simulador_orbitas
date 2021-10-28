from vpython import *
def forcaGrav(t,s):
    G = 3
    
    r_vetor = t.pos-s.pos
    r_vetor_mag = mag(r_vetor)
    r_final = r_vetor/r_vetor_mag
    forcaGravitacional = G*t.mass*s.mass/r_vetor_mag**2
    forcaGravFinal = -forcaGravitacional*r_final
    
    return forcaGravFinal
    

terra = sphere( pos=vector(0,0,0), radius=0.2, color=color.blue, mass = 2000, momentum=vector(0,0,0), make_trail=True )
lua = sphere( pos=vector(-3.62,0,0), radius=0.05, mass = 1, momentum=vector(0,30,0), make_trail=True )
satelite = sphere( pos=vector(4.19,0,0), radius=0.02, mass = 1, momentum=vector(0,30,0), make_trail=True, color=color.purple )

dt = 0.0001
t = 0
while (True):
    rate(500)
    terra.force = forcaGrav(lua ,terra) + forcaGrav(satelite,terra)
    satelite.force = forcaGrav(satelite ,terra) + forcaGrav(satelite,lua)
    lua.force = forcaGrav(lua ,terra) + forcaGrav(satelite,lua)
    terra.momentum = terra.momentum + terra.force*dt
    satelite.momentum = satelite.momentum + satelite.force*dt
    lua.momentum = lua.momentum + lua.force*dt
    terra.pos = terra.pos + terra.momentum/terra.mass*dt
    lua.pos = lua.pos + lua.momentum/lua.mass*dt
    satelite.pos = satelite.pos + satelite.momentum/satelite.mass*dt
    t = t + dt
