from flask import Flask, render_template
import folium
import locator as l

latlon=[[13.09181,80.283419],[13.114966,80.282703],[13.000544,80.263239]]
app = Flask(__name__)

@app.route('/')
def index():
    latlon.append(l.findlocation())
    map = folium.Map(location=[13.08268,80.270718], zoom_start=12)
    
    for i in latlon:
        folium.Marker(location=i,popup='Ambulance',icon=folium.Icon(color="red")).add_to(map)
    # map.add_child(folium.Marker(location=latlon[0], zoom_start=10,popup='ambulance1',icon=folium.Icon(color="green")))
    map.save("templates\index.html")


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

