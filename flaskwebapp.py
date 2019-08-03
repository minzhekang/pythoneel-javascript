from flask import Flask, render_template
app = Flask(__name__, template_folder='../python-eel-framework/web/')

@app.route('/')
def index():
  return render_template('main.html')
