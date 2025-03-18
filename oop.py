class HTMLTags:
    # Declarate type
    def DOCTYPE_html():
        return "<!DOCTYPE html> \n"
    # Declare main parts (html>{head,body})
    def html(*args):
        x = ""
        for i in args: x += str (i) + "\n"
        return f"<html> \n {x} \r </html>"
    def MainChild(type="",attr ={}, *args):
        x = ""
        attrSTR = ''
        for i in attr.keys() :
            attrSTR += f"{i}='{attr[i]}' "
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{type} {attrSTR}> \n {x} \r </{type}> """
    # General head tags
    def title(title):
        return f"""<title> {title} </title>"""
    def meta(attr ={}, *args):
        x = ""
        attrSTR = ''
        for i in attr.keys() :
            attrSTR += f"{i}='{attr[i]}' "
        for i in range (len (args)): x += args [i] + "\n"
        return f""" <meta {attrSTR} "> {x} </meta>"""
    def link(attr = {}, *args):
        x = ""
        attrSTR = ''
        for i in attr.keys() :
            attrSTR += f"{i}='{attr[i]}' "
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<link {attrSTR}"> {x} </link> """
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
    def tag(name,attr={},*args):
        x = ""
        attrSTR = ''
        for i in attr.keys() :
            attrSTR += f"{i}='{attr[i]}' "
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{name} {attrSTR}> \n {x} \r </{name}>"""
class FileHandling : 
    def save(content,fileName) :
        with open(f"./htmls/{fileName}.html", mode="w") as file :
            file.write(content)
    def run(content,fileName) :
        # the function will save then run the html file
        FileHandling.save(content,fileName)
        import os
        os.startfile(os.path.join(os.getcwd(),'htmls',f'{fileName}.html'))