from oop import HTMLTags as t
from oop import FileHandling as hf


content = open("app.py","r").read()

content = content[content.index("#begin"):content.index("#end")].replace(';\n','+')
# content.

print(content)