import json
from flask import Flask, request

app = Flask(__name__)

post = {"title": "I felt tired", "content" : "Today, as a programmer, I felt no hopes, no dreams and no lives"}
post2 = {"title": "I met a girl", "content" : "Today I met a girl, she is pretty, she loves ice cream and movies"}

posts = [
    post,
    post2
]

@app.route('/', methods=["GET", "POST"])
def posts_api():
    if request.method == "GET":
        return json.dumps(posts)
    elif request.method == "POST":
        request_body = request.get_json()
        title = request_body["title"]
        content = request_body["content"]
        post = {"title": title, "content": content}
        posts.append(post)
        return json.dumps({"code" : 1, "message": "Post added"})

if __name__ == '__main__':
    app.run()
