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
month_total=0
month_num=1
total_monthly_precipitation=[]
for measurement in seattle:
    cleaner_date=measurement["date"].split("-")
    cleaner_date.pop(0)
    cleaner_date.pop(-1)
    measurement["date"]=cleaner_date
    for value in measurement["date"]:
        value=int(value)
        measurement["date"]=value
        months.add(value)
print(seattle)

# for measurement["date"] in months:
#     print(measurement["date"])
if measurement["date"]==8:
        for measurement in seattle:
            month_total += measurement["value"]
            total_monthly_precipitation.append(month_total)
    # else:
    #     total_monthly_precipitation.append(month_total) 
    #     month_total=0
    #     month_num=measurement["date"]
    #     month_total += measurement["value"]
print(month_total)
print(total_monthly_precipitation)


# print(total_monthly_precipitation)
# print(sum(total_monthly_precipitation))

# # into JSON
# with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
#     json.dump(total_monthly_precipitation, file, indent=4, ensure_ascii=False)

# # Total yearly for locations:
# yr_cincinnati=0 
# yr_seattle=0
# yr_maui=0
# yr_sandiego=0
# for measurement in content:
#     if measurement["station"]=="GHCND:USW00093814":
#             yr_cincinnati += measurement["value"]
#     elif measurement["station"]=="GHCND:US1WAKG0038":
#             yr_seattle += measurement["value"]
#     elif measurement["station"]=="GHCND:USC00513317":
#             yr_maui += measurement["value"]  
#     elif measurement["station"]=="GHCND:US1CASD0032":
#             yr_sandiego += measurement["value"] 
# print(yr_cincinnati)
# print(yr_seattle)
# print(yr_maui)
# print(yr_sandiego)