from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    allow_headers="*",
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
)
posts = [
    {"id": "1", "title": "Hello World", "content": "This is the first post"},
    {"id": "1", "title": "Second Post", "content": "This is the second post"},
]


@app.route("/api/posts")
def post_list():
    return jsonify(posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
