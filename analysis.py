import json

seattle=[]
with open('ucaccmet2j_python/precipitation.json') as file:
    content=json.load(file)
    for measurement in content:
            if measurement["station"]=="GHCND:US1WAKG0038":
                seattle.append(measurement)
print(seattle)

jan_total=0
total_monthly_precipitation=[]
for measurement in seattle:
    if measurement["date"].startswith("2010-01"):
         jan_total += measurement["value"]
total_monthly_precipitation.insert(1, jan_total)
print(total_monthly_precipitation)