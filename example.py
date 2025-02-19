from tag_functions import html_tag
 
x = html_tag.DOCTYPE_html()+html_tag.html(
        html_tag.MainChild(
            "head","",
            html_tag.title("test")
        ),
        html_tag.MainChild(
            "body","",        
            html_tag.tag(
                "div","",
                html_tag.tag("h1","","hello world")
            )+html_tag.comment("""how to write "hello world" in html""")
    ))
y = html_tag.tag("h1","","hello world")
with open(r"test.html", mode="w") as file :
    file.write(x)
    import os
    os.startfile(r"test.html")