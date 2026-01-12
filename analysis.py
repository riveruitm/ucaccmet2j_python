import json

seattle=[]
with open('ucaccmet2j_python/precipitation.json') as file:
    content=json.load(file)
    for measurement in content:
            if measurement["station"]=="GHCND:US1WAKG0038":
                seattle.append(measurement)
print(seattle)