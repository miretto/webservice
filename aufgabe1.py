import uvicorn
from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles


app = FastAPI()

d = {}
file = open("PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)

for line in file:
   data = line.strip().split(";")
   ortschaftsname = data[0]
   plz = data[1]
   zusatzziffer = data[2]
   gemeindename = data[3]
   bfs_nr = data[4]
   kanton = data[5]
   east = data[6]
   north = data[7]
   sprache = data[8]
   d[gemeindename] = { "Ortschaftsname": ortschaftsname,
                      "PLZ": plz,
                      "Zusatzziffer": zusatzziffer,
                      "Gemeindename": gemeindename,
                      "BFS-Nr": bfs_nr,
                      "Kantonskürzel": kanton,
                      "E": east,
                      "N": north,
                      "Sprache": sprache
                      }

file.close()

@app.get("/search")
async def search(gemeindename: str):
    matches = []
    if gemeindename in d:
        return d[gemeindename]
    else:
        pass
    return matches
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
