nbdv = 353
bre =37
# name = [var_name for var_name,var_value in globals().items if var_value is x]
# print(name)
# print("globals",globals().keys())


def GetVarName(x) :
    for i in list(globals().keys()) :
        if globals()[i] == x :
            return i
            break

print(GetVarName(bre))