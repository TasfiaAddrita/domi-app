from fitbit import *
from model import *
import base64
import requests
from config import db, FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET

db.drop_all()
db.create_all()

def fitbit_client(fitbit_credentials):
    client = fitbit.Fitbit(
        FITBIT_CLIENT_ID,
        FITBIT_CLIENT_SECRET,
        access_token=fitbit_credentials.access_token,
        refresh_token=fitbit_credentials.refresh_token
    )

def get_token():
    return base64.b64encode(
        "{}:{}".format(
            FITBIT_CLIENT_ID,
            FITBIT_CLIENT_SECRET
        ).encode('utf-8')
    ).decode('utf-8')


def get_auth_url(code):
    return 'https://api.fitbit.com/oauth2/token?code={code}&client_id={client_id}&grant_type=authorization_code'.format(
        code=code,
        client_id=FITBIT_CLIENT_ID
    )


def do_fitbit_auth(code):
    r = requests.post(
        get_auth_url(code),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic {}'.format(get_token()),
        }
    )
    r.raise_for_status()
    response = r.json()
    new_user = Users(response['access_token'], response['refresh_token'])
    db.session.add(new_user)
    db.session.commit()
    return

    # return save_fitbit_token(
    #     user.id,
    #     response['access_token'],
    #     response['refresh_token']
    # )
