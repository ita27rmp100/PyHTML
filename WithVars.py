from oop import HTMLTags as t
from oop import FileHandling as hf

tryCode = t.DOCTYPE_html()+t.html(
        t.MainChild(
            "head","",
            t.title("test")
        ),
        t.MainChild(
            "body","",        
            t.tag(
                "div","",
                t.tag("h1","","hello world")
            )
    ))
# To run directly inside the file you had written your PyHTML code.
hf.run(tryCode,"runExample")