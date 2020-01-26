f = open("dognames.txt", "r")
text_dict = {}
while True:
    line = f.readline()
    if not line:
        break
    line.strip()
    text_dict[line] = 1
f.close()

print(text_dict)

chihuahua = "chihuahua"

print(chihuahua in text_dict)