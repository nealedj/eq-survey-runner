import os
import sys
import time

from app.authentication.encoder import Encoder
from app.authentication.user import USER_ID, RU_REF, RU_NAME, REF_P_START_DATE, REF_P_END_DATE, COLLECTION_EXERCISE_SID, EQ_ID, FORM_TYPE, PERIOD_ID, PERIOD_STR


def create_payload(user):
    iat = time.time()
    exp = time.time() + (5 * 60 * 60)
    return {
            USER_ID: user,
            'iat': str(int(iat)),
            'exp': str(int(exp)),
            EQ_ID: '1',
            PERIOD_STR: '2016-01-01',
            PERIOD_ID: '2016-01-01',
            FORM_TYPE: '0205',
            COLLECTION_EXERCISE_SID: "sid",
            REF_P_START_DATE: "2016-01-01",
            REF_P_END_DATE: "2016-09-01",
            RU_REF: "12346789012A",
            RU_NAME: "Apple"}


def generate_token():
    encoder = Encoder()
    user = os.getenv('USER', 'UNKNOWN')
    payload = create_payload(user)
    token = encoder.encode(payload)
    encrypted_token = encoder.encrypt(token)
    return encrypted_token

if __name__ == '__main__':

    if len(sys.argv) > 1:
        print("http://" + sys.argv[1] + "-surveys.eq.ons.digital/session?token=" + generate_token().decode())  # NOQA
    else:
        print("http://localhost:5000/session?token=" + generate_token().decode())  # NOQA
