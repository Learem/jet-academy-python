import requests

import json


cur = input().lower()
req = requests.get(f"http://www.floatrates.com/daily/{cur}.json")
temp_dict = json.loads(req.text)
curr_dict = dict.fromkeys({"usd", "eur"})
if temp_dict.get("usd"):
    curr_dict["usd"] = temp_dict["usd"]
if temp_dict.get("eur"):
    curr_dict["eur"] = temp_dict["eur"]

while True:
    req_cur = input().lower()
    if not req_cur:
        break
    temp = input()
    if temp:
        amount = float(temp)
    else:
        break
    print("Checking the cache…")
    cur_rate = curr_dict.get(req_cur)
    if cur_rate:
        print("Oh! It is in the cache!")
        value = round(amount * cur_rate["rate"], 2)
    else:
        print("Sorry, but it is not in the cache!")
        curr_dict[req_cur] = temp_dict[req_cur]
        cur_rate = curr_dict.get(req_cur)
        value = round(amount * cur_rate["rate"], 2)
    print(f"You received {value} " + req_cur.upper() + ".")
