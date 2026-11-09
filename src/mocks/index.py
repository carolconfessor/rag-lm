import json
import os

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, "cve_2021.json")

with open(file_path, enconding="utf-8") as file:
    cve=json.load(file)

print(json.dumps(cve, indent=2))

"""
Using relative path

with open("cve_2021.json", enconding="utf-8") as file:
    cve = json.load(file)

print(json.dumps(cve, ident=2))

"""