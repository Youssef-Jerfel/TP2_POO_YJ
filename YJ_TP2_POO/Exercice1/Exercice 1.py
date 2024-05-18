import json
import csv

with open("data.json", "r") as f:
    comp_num = json.load(f)

with open("data.csv", "w") as f2:
    write_csv = csv.writer(f2)
    write_csv.writerow(["reel", "imaginaire"])
    for i in comp_num:
        write_csv.writerow(i)

