from flask import Flask, render_template


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sims:theroot@localhost/dev'

@app.route("/")
def index():
    return render_template('index.html')