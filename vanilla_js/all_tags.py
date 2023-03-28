doctype_html = "<!DOCTYPE html>\n"
html_tag_open = '<html lang="en">\n'
head_tag_open = "\t<head>\n"
meta_tag_1 = '\t\t<meta charset="UTF-8" />\n'
meta_tag_2 = '\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n'
meta_tag_3 = (
    '\t\t<meta name="viewport" content="width=device-width,'
    ' initial-scale=1.0" />\n'
)
bootstrap_5_js_cdn = (
    "\t\t<script"
    ' src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/'
    'bootstrap.bundle.min.js"'
    ' integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jr'
    'RAoQmDKKtQBHUuLZ9AsSv4jD4Xa"'
    ' crossorigin="anonymous" defer></script>\n'
)
jquery_36_cdn = (
    '\t\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"'
    ' integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="'
    ' crossorigin="anonymous" defer></script>\n'
)
bootstrap_5_css_cdn = (
    '\t\t<link rel="stylesheet"'
    ' href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0'
    '/dist/css/bootstrap.min.css"'
    ' integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/'
    'HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"'
    ' crossorigin="anonymous" />\n'
)
html_script_defer = '\t\t<script src="script.js" defer></script>\n'
html_styles = '\t\t<link rel="stylesheet" href="styles.css" />\n'
title_tag = "\t\t<title>Document</title>\n"
head_tag_close = "\t</head>\n"
body_tag_open = "\t<body>\n"
child_of_body_tag = "\t\t\n"
html_script_body = '\t\t<script src="script.js"></script>\n'
body_tag_close = "\t</body>\n"
html_tag_close = "</html>"


def basic(middle: list[str] = [], end: list[str] = []):
    html_boilerplate_first_half = [
        doctype_html,
        html_tag_open,
        head_tag_open,
        meta_tag_1,
        meta_tag_2,
        meta_tag_3,
    ]
    html_boilerplate_second_half = [
        *middle,
        title_tag,
        head_tag_close,
        body_tag_open,
        child_of_body_tag,
        *end,
        body_tag_close,
        html_tag_close,
    ]
    return html_boilerplate_first_half + html_boilerplate_second_half
