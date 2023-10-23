from sys import argv
from datetime import datetime

now = datetime.now().time() # HH:MM:SS
results = dict()
# Dinamično dodajanje linij, kot key, value je array[število avtobusov]

def get_route(trip_id):
    # Preberi trips.txt in poišči pravi trip_id in vrni route_id 
    # oz zamenjaj route_id za short name iz routes.txt
    # To bi bilo inline - se ne kliče dvakrat v tem programu - mogoče takšna 
    #   funkcija že obstaja v code base? - Ni inline -> bolj berljivo
    # Tukaj se ne ponavljajo imena zaradi berljivosti, vendar bi ponavadi vzel brez _t/_r,
    #   - uporabno tudi drugih programih - napisal tudi v drugi datoteki
    with open("trips.txt") as file_trips:
        for line_t in file_trips:
            line_t = line_t.split(",")
            if line_t[2] == trip_id:
                with open("routes.txt") as file_r:
                    for line_r in file_r:
                        line_r = line_r.split(",")
                        if line_r[0] == line_t[0]:
                            return line_r[2]

def greater_then_time(time1, time2):
    # sprejema str HH:MM:SS
    if (int(time1[0:2]) <= int(time2[0:2])):
        if int(time1[3:5]) <= int(time2[3:5]):
            return int(time1[6:8]) > int(time2[6:8])
    return True

def check_correct_time(time):
    # Ali je smiselno gledati tudi sekunde? In ali je smiselno stalno klicati int?
    #
    time2 = (str(now.hour) + ":" if now.hour >= 10 else (0 + str(now.hour)) + ":")
    time2 += str(now.minute) + ":" if now.minute >= 10 else 0 + str(now.minute) + ":"
    time2 += str(now.second) if now.second >= 10 else 0 + str(now.second)
    if greater_then_time(time, time2):
        time3 = str(now.hour + 2) if now.hour >= 8 else 0 + str(now.hour + 2)
        time3 += time2[2:]
        return not greater_then_time(time, time3)
    return False

# Glede na calendar.txt je izpuščeno preverjanje ali trip obratuje - napačen dan v tednu
# Preverjal bi v koraku v katerem se išče route number/name -> dvakrat ne brskati po file
# Hitreje primerjati številke kot najdti vrednost v 1000 vrstičnem file
with open("stop_times.txt") as file:
    for line in file:
        line = line.split(",")
        if not line[3] == argv[1]: # Primerjava stop_id, argv[1] - stop_id
            continue
        elif check_correct_time(line[1]):
            # Time bi pretvoril v številke -> lažja primerjava - kot tuple?
            # Tukaj bi bilo potrebno tudi paziti na ure kot so 26:00:00
            # Druga func ki prevede v navadni čas? - Samo primerjaj po Urah -> Min -> Sec (raw int)
            route = get_route(line[0])
            if route in results.keys():
                if len(results[route]) >= int(argv[2]): # argv[2] - število postaj za izpis
                    # Poglej ali je route v results
                    # Primerjaj zadnjega
                    # Če večji vrzi ven in vstavi v razvrščen array - mogoče zamenjaj array za drugi structure
                    # Nekaj kot je binary tree - samo z enim otrokom - povezano
                    #   s pointerji/referencami - ni potrebno naknadno premikati elementov
                    if greater_then_time(results[route][-1], line[1]):
                        del results[route][-1]
                        results[route].append(line[1])
                        results[route].sort()
                    # else: pass
                else: 
                    results[route].append(line[1])
                    results[route].sort()
            else:
                results[route] = [line[1]]

with open("stops.txt") as file_s:
    for line in file_s:
        line = line.split(",")
        if line[0] == argv[1]:
            print("Postajališče " + line[2])
for k in results.keys():
    # argv[3] - relativ/absolute time
    print(k, end=": ")
    first = True
    for v in results[k]:
        if argv[3] == "relative":
            if not first: 
                print(", ", end="")
            first = False
            print(str((int(v[0:2]) - now.hour) * 60 + int(v[3:5]) - now.minute), end="min")
        else:
            if not first: 
                print(", ", end="")
            first = False
            print(v, end=" ")
    print("")
