from flask import request,Flask,jsonify,session,redirect, url_for
from services.discord_oauth2 import DCoauth
from flask_cors import CORS  # Import CORS
import config as keys


# getting the blueprint for user and match route
from routes.user_route import user_bp
from routes.match_route import match_bp



# app settings
app = Flask(__name__)
app.register_blueprint(match_bp, url_prefix='/v1')
app.register_blueprint(user_bp, url_prefix='/v1')
app.secret_key = keys.flask_secret_key
CORS(app) 


# general testing 
@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/logout')
def unlink_discord():
    session.pop('user_id',None)
    session.pop('user_info',None)
    return redirect(url_for('home'))


# main 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
    