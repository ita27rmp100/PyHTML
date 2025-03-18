class HTMLTags:
    # Declarate type
    def DOCTYPE_html():
        return "<!DOCTYPE html> \n"
    # Declare main parts (html>{head,body})
    def html(*args):
        x = ""
        for i in args: x += str (i) + "\n"
        return f"<html> \n {x} \r </html>"
    def MainChild(type="",properties = "", *args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{type} {properties}> \n {x} \r </{type}> """
    # General head tags
    def title(title):
        return f"""<title> {title} </title>"""
    def meta(properties ={}, *args):
        x = ""
        propertiesSTR = ''
        for 
        for i in range (len (args)): x += args [i] + "\n"
        return f""" <meta {properties} "> {x} </meta>"""
    def link(properties = "", *args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<link {properties}"> {x} </link> """
    def JsCss(type="style",*args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{type}> \n {x} \r </{type}>"""
    # comments
    def comment(*args):
        x = "\n"
        for i in args: x += str (i) + "\n"
        return f"<!-- {x} \r -->"
    # for other tags
    def tag(name, properties = "", *args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{name} {properties}> \n {x} \r </{name}>"""
class FileHandling : 
    def save(content,fileName) :
        with open(f"./htmls/{fileName}.html", mode="w") as file :
            file.write(content)
    def run(content,fileName) :
        # the function will save then run the html file
        FileHandling.save(content,fileName)
        import os
        os.startfile(os.path.join(os.getcwd(),'htmls',f'{fileName}.html'))