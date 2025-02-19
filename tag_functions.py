class html_tag:
    # Declarate type
    def DOCTYPE_html():
        return "<! DOCTYPE html> \n"
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
    def meta(properties = "", *args):
        x = ""
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