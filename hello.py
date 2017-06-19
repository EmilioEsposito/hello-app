import os

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page!' 
    
@app.route('/user/<username>')
def show_user(username):
    return "what's up " + str(username) 

@app.route('/hello')
def hello_world():
    # import pdb; pdb.set_trace()
    return 'hello emilio2!' 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    next_post = post_id + 1
    return "Post: " + str(post_id) + ", Next Post: " + str(next_post)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)






















