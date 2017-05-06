from flask import Flask, render_template
import hexcalc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_chsum/<input_hex>', methods=['POST'])
def get_chsum(input_hex):
    return hexcalc.get_new_hex(input_hex);

if __name__ == "__main__":
    app.run(debug=True)