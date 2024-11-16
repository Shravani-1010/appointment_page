from flask import Flask, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page_name>')
def render_page(page_name):
    try:
        return render_template(f"{page_name}.html")
    except TemplateNotFound:
        return "Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)
