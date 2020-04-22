from flask import Flask
import random

html_tmpl = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
    html {{ min-height: 32em; overflow: hidden; }}
    </style>
</head>
<body>
{content}
</body>
</html>"""

def mkdiv(content, **kwargs):
    if 'position' not in kwargs:
        kwargs['position'] = 'absolute'
    style_str = ' '.join([": ".join((k.replace('_', '-'), v))+";" for k, v in kwargs.items()])
    return f"<div style='{style_str}'>{content}</div>"

app = Flask(__name__)

@app.route('/')
def show():
    divs = []
    for i in range(1000):
        x = random.random() * 100
        y = random.random() * 100
        size = random.randrange(4, 32)
        alpha = random.random()
        this_div = mkdiv("★",
                         left=f"{x}%",
                         top=f"{y}%",
                         transform="translate(-50%, -50%)",
                         font_size=f"{size}pt",
                         color=f"rgba(0,0,0,{alpha})")
        divs.append(this_div)
    html_src = html_tmpl.format(title="Centered stars of different sizes", content="".join(divs))
    return html_src

if __name__ == '__main__':
  app.run()