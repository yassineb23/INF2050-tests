import json

with open("template.json") as f:
    d = json.load(f)
    for i in range(15):
        with open("tests/test{}.json".format(i),"w") as file:
            json.dump(d,file,indent=4)