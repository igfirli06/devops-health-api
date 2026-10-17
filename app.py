import os
from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {
        "application": "devops-health-api",
        "environment": os.getenv("APP_ENV", "development"),
    }


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8080")),
    )