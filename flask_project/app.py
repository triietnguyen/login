from flask import Flask,make_response
from flask_jwt_extended import JWTManager
from routes.user_route import user_bp
from flask_cors import CORS


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'# Replace with your actual JWT secret key
jwt = JWTManager(app)


app.register_blueprint(user_bp)

# @app.after_request
# def apply_csp(response):
#     csp = "default-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com;"
#     response.headers['Content-Security-Policy'] = csp
#     return response

if __name__ == "__main__":
    app.run(debug=True)
