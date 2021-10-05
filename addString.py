filepath = "/Users/lixujin/Desktop/anti-AD/surge.txt"


with open(filepath) as fp:
    lines = fp.read().splitlines()


with open(filepath, "w") as fp:
    for line in lines:
        if "#" in line:
            print(line, file=fp)
        else:
            print(line + ",reject", file=fp)
