from flask import Flask, render_template, request
from handlers.pulls import get_pulls
app = Flask(__name__)
ip_host = '192.168.56.11'
port = 80


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pulls')
def pulls():
    state = request.args.get("state")
    return render_template("pulls.j2", pulls=get_pulls(state))


app.run(host=ip_host, port=port)
