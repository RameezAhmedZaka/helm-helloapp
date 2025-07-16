from flask import Flask
app = Flask(__name__)

@app.route("/a")
def page_a():
    return "✅ This is Page A"

@app.route("/b")
def page_b():
    return "✅ This is Page B"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
