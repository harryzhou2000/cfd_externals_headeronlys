import json, os

with open("version_table.json", "r") as file:
    data = json.load(file)
    print(data)

for repo, version in data.items():
    cmd = f"git -C {repo} fetch --depth=1 origin tag {version}"
    ret = os.system(cmd)
    if ret:
        raise RuntimeError(f"calling: \n[{cmd}]\n failed ")
    cmd = f"git -C {repo} checkout {version}"
    ret = os.system(cmd)
    if ret:
        raise RuntimeError(f"calling: \n[{cmd}]\n failed ")
