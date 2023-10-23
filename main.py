from sys import argv
from datetime import datetime

now = datetime.now()
results = dict()
# Dinamično dodajanje linij, kot key, value je array[število avtobusov]

def get_route(trip_id): pass
# Preberi trips.txt in poišči pravi trip_id in vrni route_id 
# oz zamenjaj route_id za short name iz routes.txt
# 

with open("stop_times.txt") as file:
    for line in file:
        line = line.split(",")
        if not line[3] == argv[0]: # Primerjava stop_id
            continue
        elif line[1] < now or line > now + 2 h: # Drugi del je le vzorčen
            # Tukaj bi bilo potrebno tudi paziti na ure kot so 26:00:00
            # Druga func ki prevede v navadni čas? - Samo primerjaj po Urah -> Min -> Sec
            route = get_route(trip_id)
            if len(results[route]) > argv[2]:
                # Primerjaj zadnjega
                # Če večji vrzi ven in vstavi v razvrščen array

print(results)