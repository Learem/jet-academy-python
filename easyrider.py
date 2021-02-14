import json
import re
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": 8.12}, {"bus_id": 128, "stop_id": 3, "stop_name": "", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, {"bus_id": 128, "stop_id": "7", "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, {"bus_id": "", "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": ""}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": "0", "stop_type": "F", "a_time": "10:12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": "512", "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": 5, "a_time": "08:16"}]
# [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street Str.", "next_stop" : "11", "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : 9, "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : "five", "stop_name" : "Bourbon street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : "", "stop_id" : "", "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : 23.9, "a_time" : 8},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : "", "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : 34.6, "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : "eleven", "stop_id" : 16, "stop_name" : "Sunset Boullevard", "next_stop" : 17.4, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska St.", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Av.", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : 3, "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : "21", "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : 13.01},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "FF", "a_time" : ""},  {"bus_id" : "", "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Av.", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "8:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "OO", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:77"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "A", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10.12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "bourbon street", "next_stop": 6, "stop_type": "S", "a_time": "38:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Fifth Avenue", "next_stop" : 4, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 4, "stop_name" : "Abbey Road", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"},  {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Santa Monica Boulevard", "next_stop" : 8, "stop_type" : "O", "a_time" : "08:25"},  {"bus_id" : 128, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 11, "stop_type" : "", "a_time" : "08:37"},  {"bus_id" : 128, "stop_id" : 11, "stop_name" : "Beale Street", "next_stop" : 12, "stop_type" : "", "a_time" : "09:20"},  {"bus_id" : 128, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 14, "stop_type" : "", "a_time" : "09:45"},  {"bus_id" : 128, "stop_id" : 14, "stop_name" : "Bourbon Street", "next_stop" : 19, "stop_type" : "O", "a_time" : "09:59"},  {"bus_id" : 128, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},  {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:13"},  {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Startowa Street", "next_stop" : 8, "stop_type" : "", "a_time" : "08:16"},  {"bus_id" : 256, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 10, "stop_type" : "", "a_time" : "08:29"},  {"bus_id" : 256, "stop_id" : 10, "stop_name" : "Lombard Street", "next_stop" : 12, "stop_type" : "", "a_time" : "08:44"},  {"bus_id" : 256, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 13, "stop_type" : "O", "a_time" : "08:46"},  {"bus_id" : 256, "stop_id" : 13, "stop_name" : "Orchard Road", "next_stop" : 16, "stop_type" : "", "a_time" : "09:13"},  {"bus_id" : 256, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 17, "stop_type" : "O", "a_time" : "09:26"},  {"bus_id" : 256, "stop_id" : 17, "stop_name" : "Khao San Road", "next_stop" : 20, "stop_type" : "O", "a_time" : "10:25"},  {"bus_id" : 256, "stop_id" : 20, "stop_name" : "Michigan Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "11:26"},  {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Arlington Road", "next_stop" : 7, "stop_type" : "S", "a_time" : "11:06"},  {"bus_id" : 512, "stop_id" : 7, "stop_name" : "Parizska Street", "next_stop" : 8, "stop_type" : "", "a_time" : "11:15"},  {"bus_id" : 512, "stop_id" : 8, "stop_name" : "Elm Street", "next_stop" : 9, "stop_type" : "", "a_time" : "11:56"},  {"bus_id" : 512, "stop_id" : 9, "stop_name" : "Niebajka Avenue", "next_stop" : 15, "stop_type" : "", "a_time" : "12:20"},  {"bus_id" : 512, "stop_id" : 15, "stop_name" : "Jakis Street", "next_stop" : 16, "stop_type" : "", "a_time" : "12:44"},  {"bus_id" : 512, "stop_id" : 16, "stop_name" : "Sunset Boulevard", "next_stop" : 18, "stop_type" : "", "a_time" : "13:01"},  {"bus_id" : 512, "stop_id" : 18, "stop_name" : "Jakas Avenue", "next_stop" : 19, "stop_type" : "", "a_time" : "14:00"},  {"bus_id" : 1024, "stop_id" : 21, "stop_name" : "Karlikowska Avenue", "next_stop" : 12, "stop_type" : "S", "a_time" : "13:01"},  {"bus_id" : 1024, "stop_id" : 12, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:00"},  {"bus_id" : 512, "stop_id" : 19, "stop_name" : "Prospekt Avenue", "next_stop" : 0, "stop_type" : "F", "a_time" : "14:11"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10:12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10:12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:17"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:07"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "", "a_time": "09:44"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10:12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"}, {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "O", "a_time": "08:19"}, {"bus_id": 128, "stop_id": 5, "stop_name": "Fifth Avenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"}, {"bus_id": 128, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "08:37"}, {"bus_id": 256, "stop_id": 2, "stop_name": "Pilotow Street", "next_stop": 3, "stop_type": "S", "a_time": "09:20"}, {"bus_id": 256, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 6, "stop_type": "", "a_time": "09:45"}, {"bus_id": 256, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 7, "stop_type": "O", "a_time": "09:59"}, {"bus_id": 256, "stop_id": 7, "stop_name": "Sesame Street", "next_stop": 0, "stop_type": "F", "a_time": "10:12"}, {"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id": 512, "stop_id": 4, "stop_name": "Bourbon Street", "next_stop": 6, "stop_type": "S", "a_time": "08:13"}, {"bus_id": 512, "stop_id": 6, "stop_name": "Sunset Boulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]
# [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
# Expected ('Abbey Road', 'Elm Street')'


def time_is_more(start_time, finish_time):
    hour1, minute1 = start_time.split(":")
    hour2, minute2 = finish_time.split(":")
    result = int(hour2) > int(hour1) or (int(hour2) == int(hour1) and int(minute2) > int(minute1))
    return result


json_object = input()
# json_object =

# print(json.dumps(json_object))
data_string = json.loads(json_object)
# print(json.dumps(data_string, indent=4))

error_list = []
bus_suffixes = ["Road", "Avenue", "Boulevard", "Street"]
bus_proper_names = ["Sesame Street", "Fifth Avenue", "Sunset Boulevard", "Elm Street", "Bourbon Street", "Prospekt Avenue", "Pilotow Street"]
bus_lines = {}
start_stops = []
finish_stops = []
transfer_stops = []
on_demand_stops = []
other_stops = []
has_error_stops = 0
time_test_id = []
time_test_stop_name = []

for route in data_string:
    has_error = False
    if not isinstance(route["bus_id"], int):
        error_list.append("bus_id")
        has_error = True
    if not isinstance(route["stop_id"], int):
        error_list.append("stop_id")
        has_error = True
    if not isinstance(route["stop_name"], str):
        error_list.append("stop_name")
        has_error = True
    else:
        bus_stops = route["stop_name"].split()
        if len(bus_stops) < 2 or bus_stops[0][0].upper() != bus_stops[0][0] or not bus_stops[len(bus_stops) - 1] in bus_suffixes:
            error_list.append("stop_name")
            has_error = True
    if not isinstance(route["next_stop"], int):
        error_list.append("next_stop")
        has_error = True
    if not isinstance(route["stop_type"], str) or not route["stop_type"] in ["", "S", "O", "F"]:
        error_list.append("stop_type")
        has_error = True
    if not isinstance(route["a_time"], str) or not route["a_time"]:
        error_list.append("a_time")
        has_error = True
    elif not re.match(r"[01]\d:[0-5]\d\Z", route["a_time"]):
        error_list.append("a_time")
        has_error = True
    if not has_error:
        if bus_lines.get(route["bus_id"]):
            if route["stop_name"] in (set(start_stops) | set(finish_stops) | set(other_stops) - set(transfer_stops)):
                transfer_stops.append(route["stop_name"])
            bus_line = bus_lines[route["bus_id"]]
            if not route["bus_id"] in time_test_id:
                if bus_line.get("a_time"):
                    if time_is_more(bus_line["a_time"], route["a_time"]):
                        bus_line["a_time"] = route["a_time"]
                    else:
                        time_test_id.append(route["bus_id"])
                        time_test_stop_name.append(route["stop_name"])
                else:
                    bus_line["a_time"] = route["a_time"]
            if route["stop_type"] == "S":
                if bus_line.get("start"):
                    has_over_stops = route["bus_id"]
                    break
                else:
                    bus_line["start"] = route["stop_name"]
                    if not route["stop_name"] in start_stops:
                        start_stops.append(route["stop_name"])
            elif route["stop_type"] == "F":
                if bus_line.get("finish"):
                    has_over_stops = route["bus_id"]
                    break
                else:
                    bus_line["finish"] = route["stop_name"]
                    if not route["stop_name"] in finish_stops:
                        finish_stops.append(route["stop_name"])
            elif route["stop_type"] == "O":
                if not route["stop_name"] in on_demand_stops:
                    on_demand_stops.append(route["stop_name"])
            elif not route["stop_name"] in other_stops:
                other_stops.append(route["stop_name"])
        else:
            if route["stop_name"] in (set(start_stops) | set(finish_stops) | set(other_stops) - set(transfer_stops)):
                transfer_stops.append(route["stop_name"])
            bus_line = dict()
            bus_lines[route["bus_id"]] = bus_line
            bus_line["a_time"] = route["a_time"]
            if route["stop_type"] == "S":
                bus_line["start"] = route["stop_name"]
                if not route["stop_name"] in start_stops:
                    start_stops.append(route["stop_name"])
            elif route["stop_type"] == "F":
                bus_line["finish"] = route["stop_name"]
                if not route["stop_name"] in finish_stops:
                    finish_stops.append(route["stop_name"])
            elif route["stop_type"] == "O":
                if not route["stop_name"] in on_demand_stops:
                    on_demand_stops.append(route["stop_name"])
            elif not route["stop_name"] in other_stops:
                other_stops.append(route["stop_name"])


if has_error_stops:
    print(f"There is no start or end stop for the line: {has_error_stops}.")
else:
    for line in bus_lines:
        if not (bus_lines[line].get("start") and bus_lines[line].get("finish")):
            has_error_stops = line
            print(f"There is no start or end stop for the line: {has_error_stops}.")
            break
    if not has_error_stops:
        print("On demand stops test:")
        for stop_name in on_demand_stops:
            if stop_name not in set(start_stops) | set(finish_stops) | set(transfer_stops) | set(other_stops):
                on_demand_stops.remove(stop_name)
        if on_demand_stops:
            print("Wrong stop type:", sorted(on_demand_stops))
        else:
            print("OK")
