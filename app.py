import json
from flask import Flask

app = Flask(__name__)

post = {"title": "Today I felt tired", "content" : "Today, as a programmer, I felt no hopes, no dreams and no lives"}
post2 = {"title": "Today I met a girl", "content" : "Today I met a girl, she is pretty, she loves ice cream and movies"}

posts = [
    post,
    post2
]

@app.route('/')
def posts_api():
    return json.dumps(posts)


if __name__ == '__main__':
    app.run()
