// Your First Program

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalTime;

class Time {
    public int hour, minute, second;
    public static Time now, now_plus_2;
    public boolean dummy; // If it's just array filler

    public String toString() {
        String hours, minutes, seconds;
        if (hour >= 10) {
            hours = Integer.toString(hour);
        } else {
            hours = "0" + Integer.toString(hour);
        }
        ;
        if (minute >= 10) {
            minutes = Integer.toString(minute);
        } else {
            minutes = "0" + Integer.toString(minute);
        }
        ;
        if (second >= 10) {
            seconds = Integer.toString(second);
        } else {
            seconds = "0" + Integer.toString(second);
        }
        ;
        return hours + minutes + seconds;
    }

    public boolean is_greater(Time time) {
        if (hour < time.hour) {
            if (minute < time.minute) {
                return second > time.second;
            }
        }
        return false;
    }

    public boolean correct_time() {
        return this.is_greater(Time.now) &&
                Time.now_plus_2.is_greater(this);
    };

    public Time(int h, int m, int s) {
        hour = h;
        minute = m;
        second = s;
    }
}

class main {
    public static String get_route(String trip_id) {
        try {
            File file = new File("trip.txt");
            Scanner tripsScanner = new Scanner(file);
            String route_id = "";
            while (tripsScanner.hasNextLine()) {
                Scanner line = new Scanner(tripsScanner.nextLine()).useDelimiter(",");
                route_id = line.next();
                line.next();
                if (line.next() == trip_id) {
                    line.close();
                    break;
                }
                line.close();
            }
            tripsScanner.close();

            file = new File("routes.txt");
            Scanner fileScanner = new Scanner(file);
            String route = "";
            while (fileScanner.hasNext()) {
                Scanner line = new Scanner(tripsScanner.nextLine()).useDelimiter(",");
                if (line.next() == route_id) {
                    line.next();
                    route = line.next();
                    line.close();
                    break;
                }
                line.close();
            }
            fileScanner.close();
            return route;
        } catch (FileNotFoundException e) {
            // TODO: handle exception
        }
        return "";
    }

    public static void main(String[] args) {
        Map<String, Time[]> restultsMap = new HashMap<>();
        LocalTime now_t = LocalTime.now();
        Time.now = new Time(now_t.getHour(), now_t.getMinute(),
                now_t.getSecond());
        Time.now_plus_2 = new Time(Time.now.hour + 2, Time.now.minute,
                Time.now.second);

        try {
            File file = new File("stop_times.txt");
            Scanner stopTimeScanner = new Scanner(file);
            String trip_id, arrival_time, stop_id;
            String route_name = "";
            while (stopTimeScanner.hasNext()) {
                Scanner lineScanner = new Scanner(stopTimeScanner.nextLine()).useDelimiter(",");
                trip_id = lineScanner.next();
                lineScanner.next();
                arrival_time = lineScanner.next();
                stop_id = lineScanner.next();
                lineScanner.close();

                if (stop_id.equals(args[0])) {
                    String[] parts = arrival_time.split(":", 0);
                    Time time_arrival = new Time(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]),
                            Integer.parseInt(parts[2]));
                    if (time_arrival.correct_time()) {
                        route_name = get_route(trip_id);
                        if (restultsMap.containsKey(route_name)) {
                            if (restultsMap.get(route_name)[Integer.parseInt(args[1]) - 1]
                                    .is_greater(time_arrival)) {
                                Time to_swap = time_arrival; // Here is just to sort
                                for (int i = 0; i < restultsMap.get(route_name).length; i++) {
                                    if (to_swap.is_greater(restultsMap.get(route_name)[i])) {
                                        Time c = restultsMap.get(route_name)[i];
                                        restultsMap.get(route_name)[i] = to_swap;
                                        to_swap = c;
                                    }
                                }
                            }
                        } else {
                            Time[] temp = new Time[Integer.parseInt(args[1])];
                            Time dummy = new Time(300, 0, 0);
                            dummy.dummy = true;
                            Arrays.fill(temp, dummy);
                            restultsMap.put(route_name, temp);
                            restultsMap.get(route_name)[0] = time_arrival;
                        }
                        }
                }
            }
            
            stopTimeScanner.close();
            File stopNameFile = new File("stop.txt");
            Scanner stopNameScanner = new Scanner(stopNameFile);
            while (stopNameScanner.hasNext()) {
                String[] line = stopNameScanner.nextLine().split(",", 3);
                if (line[0] == args[0]){
                    System.out.print("Postajališče " + line[2]);
                }
            }
            stopNameScanner.close();
            for (Map.Entry<String,Time[]> entry : restultsMap.entrySet()) {
                String to_print = entry.getKey() + ": ";
                for (Time t : entry.getValue()) {
                    if (t.dummy == false) {
                        to_print += t.toString();
                    }
                }
                System.out.println(to_print);
            }
        } catch (FileNotFoundException e) {
            // TODO: handle exception
        }
    }
}