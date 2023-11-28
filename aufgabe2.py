import pyproj
from pyproj import Transformer
import uvicorn
from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles
import json


app = FastAPI()


lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84, lv95)
t2 = Transformer.from_crs(lv95,wgs84)

@app.get("/wgs84tolv95")
async def wgs84tolv95(long: float, lat: float):
    lv95koord = list(t1.transform(lat, long))
    data = {"Longitude": lv95koord[0],
            "Latitude": lv95koord[1]}
    finaldata = json.dumps(data, indent = 2)

    return finaldata

@app.get("/lv95towgs84")
async def lv95towgs84(long:float, lat: float):
    wgs84koord = list(t2.transform(lat, long))
    data = {"Longitude": wgs84koord[0],
            "Latitude": wgs84koord[1]}
    finaldata = json.dumps(data, indent = 2)

    return finaldata



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)