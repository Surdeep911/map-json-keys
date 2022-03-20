import json

def criss_cross(ff1,ff2):
    with open(ff1, 'r') as f1:
        data1 = json.load(f1)
    with open(ff2, 'r') as f2:
        data2 = json.load(f2)
    key3 = data1.keys()
    key4 = data2.keys()
    data3 = {}
    for (i,j) in zip(key3,key4):
        data3[i] = j

    data4 = {}

    for (x,y) in zip(data1.values(),data3.values()):
        data4[y] = x
    data44 = json.dumps(data4)
    f3 = open("js3.json", "a")
    f3.write(data44)
    f3.close()
    f2.close()
    f1.close()

    return data44

criss_cross('js1.json','js2.json')