# from flask import Flask,request,jsonify,render_template,url_for
# app = Flask(__name__)

from flask import (Flask,render_template,jsonify,request)

# Create the application instance
# app = Flask(__name__, template_folder="templates")
app = Flask(__name__)

users = [
            {
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
            },
            {"username": "Nicholus",
            "email": "nicholus@localhost",
            "id": 43
            },
        ]

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def get_user_details():
    return jsonify (
        users
    )


@app.route('/posts/add', methods=['POST'])
def post_user_detials():
    # request_json = request.get_json()

    user = dict (
        username = request.form.get('username'),
        email = request.form.get('email'),
        id = request.form.get('id')
    )
    
    users.append(user)
    return jsonify(users)


    
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    # return render_template('index.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/")
# def main():
#     return "Hello World !"


# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/levelup')
# def ahdgah():
#     return name

# @pp.route('/tasks',methods=['POST','GET'])
# def tasks():
#     if request.method == 'GET':
#         return jsonify

# @app.route('/<string:name>')
# def hello(name):
#     return "Hello " + name


# if __name__ == '__main__':
#     # name = "Seguya Nicholus"
#     app.run()