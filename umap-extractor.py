#!/usr/bin/python

import re
import requests
import json
import os

r = requests.get("https://umap.openstreetmap.fr/en/map/der-lis-ihre-streckenbereisungskarte_734093")

regexp = re.compile(r'U.MAP = new U.Map[(]"map", (.+) }\)', re.DOTALL)

data = json.loads(regexp.findall(r.text, re.DOTALL)[0].replace("})","}"))

properties = data["properties"]
layers = properties["datalayers"]
map_id = properties["umap_id"]
colors = {}

def normalize_name(name) :
    return name.replace("/", "_")

print(os.cwd)
os.mkdir("data")

for layer in layers :
    layer_id = layer["id"]
    req = requests.get(f"https://umap.openstreetmap.fr/en/datalayer/{map_id}/{layer_id}/")
    options = req.json()["_umap_options"]
    nname = normalize_name(options['name'])
    os.mkdir(os.path.join("data",nname))
    with  open(os.path.join("data",nname,f"{nname}.json", "w")) as f :
        f.write(req.text)
    
#print(json.dumps(layers))
