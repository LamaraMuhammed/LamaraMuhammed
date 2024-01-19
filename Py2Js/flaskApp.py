from flk.app import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return """
    <html><h2>Flask App</h2></html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8000)
