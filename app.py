# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Health & Fitness App'

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask
from routes.auth import auth

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth)

@app.route('/')
def hello():
    return 'Health & Fitness App'

if __name__ == '__main__':
    app.run(debug=True)
