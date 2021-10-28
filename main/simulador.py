import math
from vpython import *
lamp = local_light(pos=vector(0,0,0), color=color.yellow)
# Unidades de acordo com o Sistema Internacional de Medidas(SI)
G = 6.67 * math.pow(10,-11)
# Massa do satélite (arbitrária)
ME = 200
# Massa da Terra
MS = 5.973 * math.pow(10,24)
#Saída inicial:
msg = "\033[1;31m=\033[m" * 55
print(msg)
print("\033[1;31mSIMULADOR DE ÓRBITAS CIRCULARES DE SATÉLITES TERRESTRES\033[m")
print(msg)
print("\033[33m•Fórmula da velocidade orbital em órbitas circulares: v = √(GM/r), que é equivalente a r = GM/v².")
print("•G é a constante da gravitação universal, que é sempre a mesma: 6,67×10-¹¹, com unidades no SI.")
print("•M será a massa da terra: aproximadamente 6×10²⁴kg.")
print("•r é o raio da órbita, que aumenta quando se aumenta a altura do satélite.")
print("•A altura, raio e velocidade serão calculados de acordo com os dados introduzidos no programa.")
print("•Atenção: alturas muito pequenas/velocidades muito elevadas fariam com que o satélite ficasse dentro da atmosfera \nterrestre, sendo assim a resistência aerodinâmica iria diminuir a velocidade dele com o tempo.")
#Entrada:
msg2 = "-" * 40
print(msg2)
mudacor = "\033[m."
sgeo = input("\033[34mDeseja um satélite geoestácionario?[S/N] ")
if sgeo.upper().strip() == "S":
    alt = 35678000
    # Raio da órbita
    RSE = 6371000 + alt
    # Força de gravitacional entre a Terra e o satélite
    FES = G * (MS * ME) / math.pow(RSE, 2)
    # Velocidade angular do satélite em relação à Terra
    wEreal = math.sqrt(FES / (ME * RSE))
    wE = wEreal * 20
    # Velocidade do satélite (m/s)
    vE = wEreal * RSE
    print("Velocidade angular do satélite em relação à Terra: ", wEreal, " rad/s")
    print("Velocidade do satélite: ", vE / 1000, " km/s")
 
    # Altura
    print("Altura do satélite: {}".format(alt))
 
    # Posição angular inicial
    theta0 = 0
 
 
    # Posição a cada instante
 
    def positionEarth(t):
        theta = theta0 + wE * t
        return theta
 
 
    def fromDaysToS(d):
        s = d * 24 * 60 * 60
        return s
 
 
    def fromStoDays(s):
        d = s / 60 / 60 / 24
        return d
 
 
    def fromDaysToh(d):
        h = d * 24
        return h
 
 
    # Graphical parameters
    # print("\nSimulation Earth-Moon-Sun motion\n")
    # days = 365
    # seconds = fromDaysToS(days)
    # print("Days: ",days)
    # print("Seconds: ",seconds)
 
    # v = vector(384,0,0)
    E = sphere(pos=vector(RSE + 1000000, 0, 0), color=color.green, radius=1000000, make_trail=True)
    S = sphere(pos=vector(0, 0, 0), radius=6371000, texture=textures.earth)
 
    t = 0
    thetaTerra1 = 0
    dt = 1
    dthetaE = positionEarth(t + dt) - positionEarth(t)
    #print("delta t:", dt, "seconds. Days:", fromStoDays(dt), "hours:", fromDaysToh(fromStoDays(dt)), sep=" ")
    #print("Variation angular position of the Earth:", dthetaE, "rad/s that's to say", degrees(dthetaE), "degrees",
          #sep=" ")
 
    # Rotação:
    # thetareal = 1 / (12000)
    theta = wE
    while True:
        rate(200)
        S.rotate(angle=theta, axis=vector(0, 1, 0))
        thetaEarth = positionEarth(t + dt) - positionEarth(t)
        # Rotation only around z axis (0,0,1)
        E.pos = rotate(E.pos, angle=thetaEarth, axis=vector(0, 1, 0))
        t += dt
elif sgeo.upper().strip() == "N":
    print("Deseja colocar um valor para a altura, ou um valor para a velocidade orbital? ")
    resposta = input("Digite A para altura ou V para a velocidade: ")
    if resposta.upper().strip() == "A":
        alt = float(input("Digite a altura, em metros: "))
    elif resposta.upper().strip() == "V":
        vel = float(input("Digite a velocidade, em m/s: "))
        vE = vel
        raio = (G * MS) / math.pow(vE,2)
        alt = raio - 6371000
    else:
        while resposta.upper().strip() != "A" and resposta.upper().strip != "V":
            print("Resposta não reconhecida. Tente novamente.")
            resposta = input("Digite A para altura ou V para a velocidade.")
            if resposta.upper().strip() == "A":
                alt = float(input("Digite a altura, em metros: "))
                break
            elif resposta.upper().strip() == "V":
                vel = float(input("Digite a velocidade, em m/s: "))
                vE = vel
                raio = (G * MS) / (vE) ** 2
                alt = raio - 6371000
                break
    # Raio da órbita
    RSE = 6371000 + alt
    # Força Satélite-Terra
    FES = G*(MS*ME)/math.pow(RSE,2)
    # Velocidade angular do satélite em relação à Terra
    wEreal = math.sqrt(FES/(ME * RSE))
    wE = (math.sqrt(FES/(ME * RSE))) * 20
    # Velocidade do satélite
    vE = wEreal * RSE
    print("Velocidade angular do satélite em relação à Terra: ",wEreal," rad/s")
    print("Velocidade do satélite: ",vE/1000," km/s")
 
    # Altura
    print("Altura do satélite: {}".format(alt))
 
    # posição angular inicial
    theta0 = 0
 
    # Position at each time
 
    def positionEarth(t):
        theta = theta0 + wE * t
        return theta
 
 
    def fromDaysToS(d):
        s = d*24*60*60
        return s
 
    def fromStoDays(s):
        d = s/60/60/24
        return d
 
    def fromDaysToh(d):
        h = d * 24
        return h
 
    # Graphical parameters
    # print("\nSimulation Earth-Moon-Sun motion\n")
    #days = 365
    #seconds = fromDaysToS(days)
    #print("Days: ",days)
    #print("Seconds: ",seconds)
 
    #v = vector(384,0,0)
    E = sphere(pos = vector(RSE+1000000,0,0), color = color.green, radius = 1000000, make_trail=True)
    S = sphere(pos = vector(0,0,0), radius=6371000, texture = textures.earth)
 
    t = 0
    thetaTerra1 = 0
    dt = 1
    dthetaE = positionEarth(t+dt)- positionEarth(t)
    #print("delta t:",dt,"seconds. Days:",fromStoDays(dt),"hours:",fromDaysToh(fromStoDays(dt)),sep=" ")
    #print("Variation angular position of the Earth:",dthetaE,"rad/s that's to say",degrees(dthetaE),"degrees",sep=" ")
 
    #Rotação:
    #thetareal = 1 / (12000)
    thetarealmesmo = 7.22 * (10**-5)
    theta = thetarealmesmo * 20
    while True:
        rate(200)
        S.rotate(angle = theta, axis = vector(0,1,0))
        thetaEarth = positionEarth(t+dt) - positionEarth(t)
        # Rotation only around z axis (0,0,1)
        E.pos = rotate(E.pos,angle=thetaEarth,axis=vector(0,1,0))
        t += dt
else:
    while sgeo.upper().strip() != "S" and sgeo.upper().strip() != "N":
        if sgeo.upper().strip() == "S":
            alt = 35678000
            # raio da orbita
            RSE = 6371000 + alt
            # Force Earth-Sun
            FES = G * (MS * ME) / math.pow(RSE, 2)
            # Angular velocity of the Earth with respect to the Sun(rad/s)
            wEreal = math.sqrt(FES / (ME * RSE))
            wE = (math.sqrt(FES / (ME * RSE))) * 20
            # Velocity v of the Earth (m/s)
            vE = wEreal * RSE
            print("Velocidade angular do satélite em relação à Terra ", wEreal, " rad/s")
            print("Velocidade do satélite: ", vE / 1000, " km/s")
 
            # Altura
            print("Altura do satélite: {}".format(alt))
 
            # Initial angular position
            theta0 = 0
 
 
            # Position at each time
 
            def positionEarth(t):
                theta = theta0 + wE * t
                return theta
 
 
            def fromDaysToS(d):
                s = d * 24 * 60 * 60
                return s
 
 
            def fromStoDays(s):
                d = s / 60 / 60 / 24
                return d
 
 
            def fromDaysToh(d):
                h = d * 24
                return h
 
 
            # Graphical parameters
            # print("\nSimulation Earth-Moon-Sun motion\n")
            # days = 365
            # seconds = fromDaysToS(days)
            # print("Days: ",days)
            # print("Seconds: ",seconds)
 
            # v = vector(384,0,0)
            E = sphere(pos=vector(RSE + 1000000, 0, 0), color=color.green, radius=1000000, make_trail=True)
            S = sphere(pos=vector(0, 0, 0), radius=6371000, texture=textures.earth)
 
            t = 0
            thetaTerra1 = 0
            dt = 1
            dthetaE = positionEarth(t + dt) - positionEarth(t)
            #print("delta t:", dt, "seconds. Days:", fromStoDays(dt), "hours:", fromDaysToh(fromStoDays(dt)), sep=" ")
            #print("Variation angular position of the Earth:", dthetaE, "rad/s that's to say", degrees(dthetaE),
                  #"degrees",
                  #sep=" ")
 
            # Rotação:
            # thetareal = 1 / (12000)
            theta = wE
            while True:
                rate(200)
                S.rotate(angle=theta, axis=vector(0, 1, 0))
                thetaEarth = positionEarth(t + dt) - positionEarth(t)
                # Rotation only around z axis (0,0,1)
                E.pos = rotate(E.pos, angle=thetaEarth, axis=vector(0, 1, 0))
                t += dt
        if sgeo.upper().strip() == "N":
 
            print("Deseja colocar um valor para a altura, ou um valor para a velocidade orbital? ")
            resposta = input("Digite A para altura ou V para a velocidade: ")
            if resposta.upper().strip() == "A":
                alt = float(input("Digite a altura, em metros: "))
            elif resposta.upper().strip() == "V":
                vel = float(input("Digite a velocidade, em m/s: "))
                vE = vel
                raio = (G * MS) / math.pow(vE, 2)
                alt = raio - 6371000
            else:
                while resposta.upper().strip() != "A" and resposta.upper().strip != "V":
                    print("Resposta não reconhecida. Tente novamente.")
                    resposta = input("Digite A para altura ou V para a velocidade.")
                    if resposta.upper().strip() == "A":
                        alt = float(input("Digite a altura, em metros: "))
                        break
                    elif resposta.upper().strip() == "V":
                        vel = float(input("Digite a velocidade, em m/s: "))
                        vE = vel
                        raio = (G * MS) / (vE) ** 2
                        alt = raio - 6371000
                        break
            # Radius Sun-Earth
            RSE = 6371000 + alt
            # Force Earth-Sun
            FES = G * (MS * ME) / math.pow(RSE, 2)
            # Angular velocity of the Earth with respect to the Sun(rad/s)
            wEreal = math.sqrt(FES / (ME * RSE))
            wE = (math.sqrt(FES / (ME * RSE))) * 20
            # Velocity v of the Earth (m/s)
            vE = wEreal * RSE
            print("Velocidade angular do satélite em relação à Terra: ", wEreal, " rad/s")
            print("Velocidade do satélite: ", vE / 1000, " km/s")
 
            # Altura
            print("Altura do satélite: {}".format(alt))
 
            # Initial angular position
            theta0 = 0
 
 
            # Position at each time
 
            def positionEarth(t):
                theta = theta0 + wE * t
                return theta
 
 
            def fromDaysToS(d):
                s = d * 24 * 60 * 60
                return s
 
 
            def fromStoDays(s):
                d = s / 60 / 60 / 24
                return d
 
 
            def fromDaysToh(d):
                h = d * 24
                return h
 
 
            # Graphical parameters
            # print("\nSimulation Earth-Moon-Sun motion\n")
            # days = 365
            # seconds = fromDaysToS(days)
            # print("Days: ",days)
            # print("Seconds: ",seconds)
 
            # v = vector(384,0,0)
            E = sphere(pos=vector(RSE + 1000000, 0, 0), color=color.green, radius=1000000, make_trail=True)
            S = sphere(pos=vector(0, 0, 0), radius=6371000, texture=textures.earth)
 
            t = 0
            thetaTerra1 = 0
            dt = 1
            dthetaE = positionEarth(t + dt) - positionEarth(t)
            #print("delta t:", dt, "seconds. Days:", fromStoDays(dt), "hours:", fromDaysToh(fromStoDays(dt)), sep=" ")
            #print("Variation angular position of the Earth:", dthetaE, "rad/s that's to say", degrees(dthetaE),
                  #"degrees", sep=" ")
 
            # Rotação:
            # thetareal = 1 / (12000)
            thetarealmesmo = 7.22 * (10 ** -5)
            theta = thetarealmesmo * 20
            while True:
                rate(200)
                S.rotate(angle=theta, axis=vector(0, 1, 0))
                thetaEarth = positionEarth(t + dt) - positionEarth(t)
                # Rotation only around z axis (0,0,1)
                E.pos = rotate(E.pos, angle=thetaEarth, axis=vector(0, 1, 0))
                t += dt
