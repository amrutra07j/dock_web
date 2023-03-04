from flask import Flask
import redis


app = Flask(__name__)
client = redis.Redis(host="redis-server", port=6379)
client.set("visits", 0)
@app.route("/")
def hello():
    var = int(client.get("visits"))
    client.set("visits", var+1)

    return f"<h1>Hello there you number is {var}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)