import json
from pathlib import Path

with Path(__file__).with_name("cve_2021.json").open(encoding="utf-8") as file:
	cve = json.load(file)

print(json.dumps(cve, indent=2))

