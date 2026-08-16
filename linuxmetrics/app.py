from flask import Flask, jsonify
from collector import collect_metrics
from database import save_metrics, create_table


app = Flask(__name__)


# Create database table when application starts
create_table()


@app.route("/metrics")
def metrics():

    data = collect_metrics()

    save_metrics(data)

    return jsonify(data)



@app.route("/health")
def health():

    return jsonify({
        "status": "running"
    })



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8000
    )
