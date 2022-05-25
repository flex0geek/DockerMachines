from flask import Flask, request, \
        render_template_string, render_template,redirect
import os, random
app = Flask(__name__)

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html'), 500

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route("/happiness",methods=["POST"])
def hello_ssti():
    output = ""
    if request.form.get('message'):
        name = request.form.get('message')
        for i in ["._","[","]"]:
            if i in name:
                return redirect(random.choice(links))
        output = render_template_string('%s' % name.replace(".","").replace("_",'').replace("[","").replace("]","").replace(" ",""))
    return render_template("happiness.html",output=output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8020))
    app.run(debug=False,host='0.0.0.0',port=port)
