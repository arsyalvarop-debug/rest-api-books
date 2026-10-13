from flask import Flask
from database.db import init_db
from routes.books import books_bp

app = Flask(__name__)

init_db()
app.register_blueprint(books_bp)


@app.route("/")
def home():
    return {
        "message": "Books API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)