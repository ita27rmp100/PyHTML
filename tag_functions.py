class html_tag:
    def DOCTYPE_html ():
        return "<! DOCTYPE html> \n"
    def html (*args):
        x = ""
        for i in args: x += str (i) + "\n"
        print(x)
        return f"<html> \n {x} \r </html>"
    def comment (* args):
        x = ""
        for i in args: x += str (i) + "\n"
        return f"<!-- {x} \r -->"
    def tag (name, properties = "", * args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<{name} {properties}> \n {x} \r </ {name}>"""
class head_tag:
        def head (* args):
            x = ""
            for i in range (len (args)): x += args [i] + "\n"
            return f"""<head> \n {x} \r </head>"""
        def title (title):
            return f"""<title> {title} </title>"""
        def meta (properties = "", * args):
            x = ""
            for i in range (len (args)): x += args [i] + "\n"
            return f""" <meta {properties} "> {x} </meta>"""
        def link (properties = "", * args):
            x = ""
            for i in range (len (args)): x += args [i] + "\n"
            return f"""<link {properties}"> {x} </link> """
        def style (* args):
            x = ""
            for i in range (len (args)): x += args [i] + "\n"
            return f"""<style> \n {x} \r </style>"""
class body_tag:
    def body (properties = "", * args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<body {properties}"> \n {x} \r </body> """
    def div (properties = "", * args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f"""<div {properties}"> \n {x} \r </div> """
    def pre (properties = "", * args):
        x = ""
        for i in range (len (args)): x += args [i] + "\n"
        return f""" <pre {properties} "> \n {x} \r </pre>"""