with open("sizing.txt","w") as g:
    with open("variables","r") as f:
        for line in f.readlines():  
            if "->name = " in line:
                name = (line.strip()).split("->name = ")[1].replace('"',"")
            elif "->expression = " in line:
                value = (line.strip()).split("->expression = ")[1].replace('"',"")
            elif "->index = " in line:
                g.write(f'{name}\t{value}\n')
