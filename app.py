from flask import *

app = Flask(__name__)

posts = [
    {'id':'1', "title": "Hello World", "content": "This is the first post"},
    {'id':'1', "title": "Second Post", "content": "This is the second post"},
]


@app.route("/api/posts")
def post_list():
    return jsonify(posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
