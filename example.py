from tag_functions import html_tag , body_tag , head_tag
# an excample :
 
x = html_tag.DOCTYPE_html()+html_tag.html(
        head_tag.head(
            head_tag.title("test")
        ),
        body_tag.body("",
            body_tag.div("",
                html_tag.tag("h1","","hello world")
            )+html_tag.comment("""how to write "hello world" in html""")
    ))
y = html_tag.tag("h1","","hello world")
with open(r"test.html", mode="w") as file :
    file.write(x)
    import os
    os.startfile(r"test.html")
