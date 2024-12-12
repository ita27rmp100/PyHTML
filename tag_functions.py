class html_tag:
    x = ""
    def DOCTYPE_html ():
        return "<! DOCTYPE html> \ n"
    def html (* args):
        for i in args: x + = str (i) + "\ n"
        return f "<html> \ n {x} \ r </html>"
    def comment (* args):
        for i in args: x + = str (i) + "\ n"
        return f "<! - {x} \ r ->"
    def tag (name, properties = "", * args):
        for i in range (len (args)): x + = args [i] + "\ n"
        return f "<{name} {properties}> \ n {x} \ r </ {name}>"
class head_tag:
        x = ""
        def head (* args):
            for i in range (len (args)): x + = args [i] + "\ n"
            return f "<head> \ n {x} \ r </head>"
        def title (title):
            return f "" "<title> {title} </title>" ""
        def meta (properties = "", * args):
            for i in range (len (args)): x + = args [i] + "\ n"
            return f "" <meta {properties} "> {x} </meta>" ""
        def link (properties = "", * args):
            for i in range (len (args)): x + = args [i] + "\ n"
            return f "" "<link {properties}"> {x} </link> "" "
        def style (* args):
            for i in range (len (args)): x + = args [i] + "\ n"
            return f "<style> \ n {x} \ r </style>"
class body_tag:
    x = ""
    def body (properties = "", * args):
        for i in range (len (args)): x + = args [i] + "\ n"
        return f "" "<body {properties}"> \ n {x} \ r </body> "" "
    def div (properties = "", * args):
        for i in range (len (args)): x + = args [i] + "\ n"
        return f "" "<div {properties}"> \ n {x} \ r </div> "" "
    def pre (properties = "", * args):
        for i in range (len (args)): x + = args [i] + "\ n"
        return f "" <pre {properties} "> \ n {x} \ r </pre>" ""
