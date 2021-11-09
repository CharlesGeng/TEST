import os

with open("newFile.html", "w", encoding="utf-8") as d:
    with open("托业阅读专项突破-Notebook.html", encoding="utf-8") as f:
        for l in f:
            n = l.strip()
            if "highlight_blue" in n:
                n = n.replace("""'noteText'""", """'noteText' style='color:blue'""")
            elif "highlight_pink" in n:
                n = n.replace("""'noteText'""", """'noteText' style='color:pink'""")
            elif "highlight_orange" in n:
                n = n.replace("""'noteText'""", """'noteText' style='color:orange'""")
            elif "highlight_yellow" in n:
                n = n.replace("""'noteText'""", """'noteText' style='color:yellow'""")
            if "</div>" in n:
                i = n.find("</div>")
                n = n[i + 6 :].replace("h3", "div")
            d.writelines(n)
            d.write(os.linesep)
