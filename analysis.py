import json
import pandas as pd

seattle=[]
with open('ucaccmet2j_python/precipitation.json') as file:
    content=json.load(file)
    for measurement in content:
            if measurement["station"]=="GHCND:US1WAKG0038":
                seattle.append(measurement)
# print(seattle)

months=set()
for measurement in seattle:
    cleaner_date=measurement["date"].split("-")
    cleaner_date.pop(0)
    cleaner_date.pop(-1)
    measurement["date"]=cleaner_date
    for value in measurement["date"]:
        value=int(value)
        measurement["date"]=value

total_monthly_precipitation_seattle={}
for measurement in seattle:
    month=measurement["date"]
    if month not in total_monthly_precipitation_seattle:
        total_monthly_precipitation_seattle[month]=0
    total_monthly_precipitation_seattle[month] += measurement["value"]
print(total_monthly_precipitation_seattle)

# into JSON
with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation_seattle, file, indent=4, ensure_ascii=False)

# Total yearly for locations:
yr_all={}
yr_cincinnati=0 
yr_seattle=0
yr_maui=0
yr_sandiego=0
for measurement in content:
    if measurement["station"]=="GHCND:USW00093814":
            yr_cincinnati += measurement["value"]
            yr_all["Cincinnati"]=yr_cincinnati
    elif measurement["station"]=="GHCND:US1WAKG0038":
            yr_seattle += measurement["value"]
            yr_all["Seattle"]=yr_seattle
    elif measurement["station"]=="GHCND:USC00513317":
            yr_maui += measurement["value"]  
            yr_all["Maui"]=yr_maui
    elif measurement["station"]=="GHCND:US1CASD0032":
            yr_sandiego += measurement["value"] 
            yr_all["San Diego"]=yr_sandiego
print(yr_all)

relative_monthly_precipitation_seattle={}
for month in total_monthly_precipitation_seattle:
    if month not in relative_monthly_precipitation_seattle:
        relative_monthly_precipitation_seattle[month]=0
    relative_monthly_precipitation_seattle[month] += total_monthly_precipitation_seattle[month]/yr_seattle
print(relative_monthly_precipitation_seattle)
with open('ucaccmet2j_python/results.json', 'a', encoding='utf-8') as file:
    json.dump(relative_monthly_precipitation_seattle, file, indent=4, ensure_ascii=False)
