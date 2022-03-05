import os
from flask import Flask, request, render_template_string, render_template
app = Flask(__name__)

@app.route('/')
def hello_ssti():
    if request.args.get('name'):
        name = request.args.get('name')
        template = '''<h2>Hello %s!</h2>''' % name
        return render_template_string(template)
    else:
        return "<h2>Enter (name) parameter</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True,host='0.0.0.0',port=port)
