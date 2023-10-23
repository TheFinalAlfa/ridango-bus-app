from sys import argv
from datetime import datetime

now = datetime.now()
results = dict()
# Dinamično dodajanje linij, kot key, value je array[število avtobusov]

def get_route(trip_id): pass
# Preberi trips.txt in poišči pravi trip_id in vrni route_id 
# oz zamenjaj route_id za short name iz routes.txt
# To bi bilo inline - se ne kliče dvakrat v tem programu - mogoče takšna 
#   funkcija že obstaja v code base?
#


# Glede na calendar.txt je izpuščeno preverjanje ali trip obratuje
# Preverjal bi v koraku v katerem se išče route number/name -> dvakrat ne brskati po file
# Hitreje primerjati številke kot najdti vrednost v 1000 vrstičnem file
with open("stop_times.txt") as file:
    for line in file:
        line = line.split(",")
        if not line[3] == argv[0]: # Primerjava stop_id
            continue
        elif line[1] < now or line > now + 2 h: # Drugi del je le vzorčen
            # Time bi pretvoril v številke -> lažja primerjava
            # Tukaj bi bilo potrebno tudi paziti na ure kot so 26:00:00
            # Druga func ki prevede v navadni čas? - Samo primerjaj po Urah -> Min -> Sec (raw int)
            route = get_route(trip_id)
            if len(results[route]) > argv[2]:
                # Primerjaj zadnjega
                # Če večji vrzi ven in vstavi v razvrščen array - mogoče zamenjaj array za drugi structure
                # Nekaj kot je binary tree - samo z enim otrokom - povezano
                #   s pointerji/referencami - ni potrebno naknadno premikati elementov

print(results)