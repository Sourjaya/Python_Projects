import folium
import pandas as pd
data=pd.read_csv("Cities_IND.csv")
lat=list(data["lat"])
lon=list(data["lng"])
population=list(data["population"])
city=list(data["city"])

def check_population(p):
    if p<100000:
        return 'green'
    elif 100000<=p<1000000:
        return 'darkgreen'
    elif 1000000<=p<5000000:
        return 'orange'
    elif 5000000<=p<10000000:
        return 'lightred'
    else:
        return 'darkred'

map=folium.Map(location=[22.601166,88.381081],zoom_start=6,tiles="openstreetmap")
fg=folium.FeatureGroup(name="Major Cities in World")
for lt,ln,p,c in zip(lat,lon,population,city):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(c)+" with population of "+str(p),fill_color=check_population(p),color='grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")