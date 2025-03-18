import json, os, re

def call_sys(cmd):
    ret = os.system(cmd)
    if ret:
        raise RuntimeError(f"calling: \n[{cmd}]\n failed ")


if __name__ == "__main__":
    with open("version_table.json", "r") as file:
        data = json.load(file)
        print(data)

    for repo, version in data.items():

        print(f"\n{'='*12}\nHandling: [{repo}, {version}]")

        matchTag = re.match(r"tag:(\S+)", version)
        if matchTag is not None:
            version = matchTag.group(1)
            cmd = f"git -C {repo} fetch --depth=1 origin tag {version}"
            call_sys(cmd)
        else:
            cmd = f"git -C {repo} fetch --depth=1 origin {version}"
            call_sys(cmd)

        cmd = f"git -C {repo} checkout {version}"
        call_sys(cmd)
