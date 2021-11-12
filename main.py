f = open("predefined_classes","r")
f2 = open("label_map.pbtxt","w")
count = 0
Lines = f.readlines()
for line in Lines:
    count += 1
    f2.write("item {\n")
    f2.write("    name: \"{}\"\n".format(line.strip()))
    f2.write("    id: {}\n".format(count))
    f2.write("}\n")
    f2.write("\n")
f.close()