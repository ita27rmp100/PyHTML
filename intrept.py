from oop import HTMLTags as t
from oop import FileHandling as hf
from termcolor import colored

# starting the intrept console
PyHTML ="""
#  .............._............................_..................._......................
#  __......_____|.|.___.___.._.__.___...___..|.|_.___.....___..__|.__......___.__.._..._.
#  \.\./\././._.|.|/.__/._.\|.'_.`._.\./._.\.|.__/._.\.../._.\/._`.\.\./\./.|.'_.\|.|.|.|
#  .\.V..V.|..__|.|.(_|.(_).|.|.|.|.|.|..__/.|.||.(_).|.|..__|.(_|.|\.V..V._|.|_).|.|_|.|
#  ..\_/\_/.\___|_|\___\___/|_|.|_|.|_|\___|..\__\___/...\___|\__,_|.\_/\_(_|..__/.\__,.|
#  .........................................................................|_|....|___/.
"""
print(colored(PyHTML,"red"))
print(colored(("-"*24)+" MADE BY WHO GOT 14 IN HTML EXAM (ITA27) "+("-"*24),"blue"),"\r")

fileName =''
while fileName != "$stop$" :
    fileName = input(colored("PLEASE, ENTER THE FILENAME YOU WANNA INTREPT (WITHOUT EXTENSION) :   ","green"))
    try :
        # intrepting
        if fileName != "$stop$" : 
            content = open(fileName+'.py',"r").read()
            content = eval(content[content.index("#begin"):content.index("#end")].replace(';\n','+'))
            hf.run(content,fileName)
            print(colored(">>> FILE OPENED SUCCESFYLLY","green"))
        elif fileName == "$stop$" :
            print(colored(("-"*38)+" GOODBYE BRO "+("-"*38),"blue"),"\r")
    except :
        print(colored(">>> ERROR, IN INTREPTING","red"))