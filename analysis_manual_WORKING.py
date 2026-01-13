import json

all_states=[]
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
            measurement["date"]=value
        if measurement["station"]=="GHCND:US1WAKG0038":
            measurement["city"]="Seattle"
            all_states.append(measurement)
            seattle.append(measurement)
        elif measurement["station"]=="GHCND:USW00093814":
            measurement["city"]="Cincinnati"
            all_states.append(measurement)
            cincinnati.append(measurement)
        elif measurement["station"]=="GHCND:USC00513317":
            measurement["city"]="Maui"
            all_states.append(measurement)
            maui.append(measurement)
        elif measurement["station"]=="GHCND:US1CASD0032":
            measurement["city"]="Sandiego"
            all_states.append(measurement)  
            sandiego.append(measurement)
# print(all_states)


months=set()

total_monthly_precipitation_all={}
total_monthly_precipitation_area={}

# chosen_city="none"
# for measurement in all_states:
#     month=measurement["date"]
#     city=measurement["city"]
#     if chosen_city==city:
#         if month not in total_monthly_precipitation_area:
#             total_monthly_precipitation_area[month]=0
#         total_monthly_precipitation_area[month] += measurement["value"]
#         total_monthly_precipitation_all[city]=total_monthly_precipitation_area
#     chosen_city=city
#     if month not in total_monthly_precipitation_area:
#         total_monthly_precipitation_area[month]=0
#         total_monthly_precipitation_area[month] += measurement["value"]
#         total_monthly_precipitation_all[city]=total_monthly_precipitation_area
    
# print(total_monthly_precipitation_all)


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


total_monthly_precipitation_all["Cincinnati"]=total_monthly_precipitation_cincinnati
total_monthly_precipitation_all["Seattle"]=total_monthly_precipitation_seattle
total_monthly_precipitation_all["Maui"]=total_monthly_precipitation_maui
total_monthly_precipitation_all["San Diego"]=total_monthly_precipitation_sandiego
# print(total_monthly_precipitation_all)

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

print(yr_all)
with open('ucaccmet2j_python/results.json', 'a', encoding='utf-8') as file:
    json.dump(yr_all, file, indent=4, ensure_ascii=False)


rel_cincinnati={}
for measurement in cincinnati:
    month=measurement["date"]
    if month not in rel_cincinnati:
        rel_cincinnati[month]=0
    rel_cincinnati[month] = total_monthly_precipitation_cincinnati[month]/yr_cincinnati
# print(rel_cincinnati)

rel_seattle={}
for measurement in seattle:
    month=measurement["date"]
    if month not in rel_seattle:
        rel_seattle[month]=0
    rel_seattle[month] = total_monthly_precipitation_seattle[month]/yr_seattle
# print(rel_seattle)

rel_maui={}
for measurement in maui:
    month=measurement["date"]
    if month not in rel_maui:
        rel_maui[month]=0
    rel_maui[month] = total_monthly_precipitation_maui[month]/yr_maui
# print(rel_maui)

rel_sandiego={}
for measurement in sandiego:
    month=measurement["date"]
    if month not in rel_sandiego:
        rel_sandiego[month]=0
    rel_sandiego[month] = total_monthly_precipitation_sandiego[month]/yr_sandiego
# print(rel_sandiego)

relative_monthly_precipitation_all={}

relative_monthly_precipitation_all["Cincinnati"]=rel_cincinnati
relative_monthly_precipitation_all["Seattle"]=rel_seattle
relative_monthly_precipitation_all["Maui"]=rel_maui
relative_monthly_precipitation_all["Sandiego"]=rel_sandiego

print(relative_monthly_precipitation_all)

with open('ucaccmet2j_python/results.json', 'a', encoding='utf-8') as file:
    json.dump(relative_monthly_precipitation_all, file, indent=4, ensure_ascii=False)

