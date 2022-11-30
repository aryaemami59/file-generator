from all_tags import basic


def create_files(*middle: list[str]):
    h = open("index.html", "w")
    h.writelines(basic(*middle))
    s = open("styles.css", "w")
    s.write(
        "* {\n\tmargin: 0;\n\tpadding: 0;\n\tbox-sizing: border-box;\n}\n\nhtml {\n\twidth: 100%;\n\theight: 100%;\n}\n\nbody {\n\twidth: 100%;\n\theight: 100%;\n}\n\n"
    )
    s.close()
    f = open("script.js", "w")
    f.close()
