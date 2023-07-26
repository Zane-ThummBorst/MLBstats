import json
import unidecode as uni

enc = 'utf-8'
f = open("war_daily_bat.txt", encoding=enc)
s = set()
playerList = []
for line in f:
    list = line.split(',')
    reduced = [list[0], list[2]]
    if not list[2] in s:
        s.add(list[2])
        playerList.append(uni.unidecode(list[0]))
dict = {'list': playerList}

# Serializing json
json_object = json.dumps(dict, indent=4)

# Writing to sample.json
with open("../mlb/PlayerList.json", "w") as outfile:
    outfile.write(json_object)
