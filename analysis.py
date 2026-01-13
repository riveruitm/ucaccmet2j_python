import json
import pandas as pd

seattle=[]
cincinnati=[]
maui=[]
sandiego=[]
with open('ucaccmet2j_python/precipitation.json') as file:
    content=json.load(file)
    for measurement in content:
        cleaner_date=measurement["date"].split("-")
        cleaner_date.pop(0)
        cleaner_date.pop(-1)
        measurement["date"]=cleaner_date
        for value in measurement["date"]:
            value=int(value)
            measurement["date"]=value
            if measurement["station"]=="GHCND:US1WAKG0038":
                seattle.append(measurement)
            if measurement["station"]=="GHCND:USW00093814":
                cincinnati.append(measurement)
            if measurement["station"]=="GHCND:USC00513317":
                maui.append(measurement)
            if measurement["station"]=="GHCND:US1WAKG0038":
                sandiego.append(measurement)
# print(seattle)

months=set()

total_monthly_precipitation_cincinnati={}
for measurement in cincinnati:
    month=measurement["date"]
    if month not in total_monthly_precipitation_cincinnati:
        total_monthly_precipitation_cincinnati[month]=0
    total_monthly_precipitation_cincinnati[month] += measurement["value"]
print(f"Cincinnati: {total_monthly_precipitation_cincinnati}")

total_monthly_precipitation_seattle={}
for measurement in seattle:
    month=measurement["date"]
    if month not in total_monthly_precipitation_seattle:
        total_monthly_precipitation_seattle[month]=0
    total_monthly_precipitation_seattle[month] += measurement["value"]
print(f"Seattle: {total_monthly_precipitation_seattle}")

total_monthly_precipitation_maui={}
for measurement in maui:
    month=measurement["date"]
    if month not in total_monthly_precipitation_maui:
        total_monthly_precipitation_maui[month]=0
    total_monthly_precipitation_maui[month] += measurement["value"]
print(f"Maui: {total_monthly_precipitation_maui}")

total_monthly_precipitation_sandiego={}
for measurement in sandiego:
    month=measurement["date"]
    if month not in total_monthly_precipitation_sandiego:
        total_monthly_precipitation_sandiego[month]=0
    total_monthly_precipitation_sandiego[month] += measurement["value"]
print(f"San Diego: {total_monthly_precipitation_sandiego}")

total_monthly_precipitation_all=[]
total_monthly_precipitation_all.append("Cincinnati:")
total_monthly_precipitation_all.append(total_monthly_precipitation_cincinnati)
total_monthly_precipitation_all.append("Seattle:")
total_monthly_precipitation_all.append(total_monthly_precipitation_seattle)
total_monthly_precipitation_all.append("Maui:")
total_monthly_precipitation_all.append(total_monthly_precipitation_maui)
total_monthly_precipitation_all.append("San Diego:")
total_monthly_precipitation_all.append(total_monthly_precipitation_sandiego)


# into JSON
with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation_all, file, indent=4, ensure_ascii=False)

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


# relative_monthly_precipitation_area={}
# for month in total_monthly_precipitation_area:
#     if month not in relative_monthly_precipitation_area:
#         relative_monthly_precipitation_area[month]=0
#     relative_monthly_precipitation_area[month] += total_monthly_precipitation_seattle[month]/yr_seattle
# print(relative_monthly_precipitation_area)

# relative_monthly_precipitation_all=[]
# relative_monthly_precipitation_all.append(relative_monthly_precipitation_area)

# with open('ucaccmet2j_python/results.json', 'a', encoding='utf-8') as file:
#     json.dump(relative_monthly_precipitation_all, file, indent=4, ensure_ascii=False)
