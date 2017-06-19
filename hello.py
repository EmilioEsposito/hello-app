import os

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page!' 
    
@app.route('/user/<username>')
def show_user(username):
    return "User %s" % str(username) 

@app.route('/hello')
def hello_world():
    # import pdb; pdb.set_trace()
    return 'hello emilio2!' 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    next_post = post_id + 1
    return "Post: %s, Next Post %s" % (str(post_id), str(next_post))

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)






















