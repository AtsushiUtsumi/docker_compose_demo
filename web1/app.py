from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "FUGA"#render_template('index.html')

# @app.route('/<name>')
# def hello(name):
#     return render_template('hello.html', title='webサーバ1', name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)