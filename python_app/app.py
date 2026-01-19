from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"""
    <html>
      <head><title>Simple Flask App</title></head>
      <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 60px;">
        <h1>Simple Flask App</h1>
        <p>This app is running and serving a meaningful message.</p>
        <p>Current server time: <strong>{now}</strong></p>
        <p>Route: <code>/</code></p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)