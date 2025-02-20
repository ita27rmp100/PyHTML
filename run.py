def GetVarName(name) :
    for i in list(globals().keys()) :
        if globals()[i] == name :
            return i
            break
def Run(content,fileName) :
    with open(f"{fileName}.html", mode="w") as file :
        file.write(content)
        import os
        os.startfile(f"{fileName}.html")