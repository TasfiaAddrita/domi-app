from flask import render_template, request, redirect, jsonify
from config import app, FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET
from fitbit import *
from model import *
from fitbit_client import *
# from model import *

SCOPES = [
    'profile',
    'activity',
    'heartrate',
    # 'location',
    # 'nutrition',
    'settings',
    'sleep',
    # 'social',
    # 'weight'
]

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/permission-screen')
def permission():
    return redirect(("https://fitbit.com/oauth2/authorize?response_type=code&client_id={client_id}&scope={scope}").format(client_id=FITBIT_CLIENT_ID, scope='%20'.join(SCOPES)))

@app.route('/oauth-redirect')
def home():
    code = request.args.get('code')
    do_fitbit_auth(code)
    return render_template('home.html', code=code)

if __name__ == "__main__":
    app.run(debug=True)
