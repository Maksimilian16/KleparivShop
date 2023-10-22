from datetime import datetime, timedelta
from typing import Optional
import jwt
import time
from KleparivShop.settings import JWT_AUTH
from django.http import HttpResponse

# Define your JWT_SECRET and ALGORITHMS based on your settings
JWT_SECRET = JWT_AUTH['JWT_SECRET_KEY']
ALGORITHMS = JWT_AUTH['JWT_ALGORITHM']


class VerifyToken:
    def __init__(self, token):
        self.token = token

    def verify(self):
        print(self.token)
        decoded_token = jwt.decode(self.token, JWT_SECRET, algorithms=ALGORITHMS)
        return decoded_token


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Use JWT_SECRET and ALGORITHMS from your settings
    encoded_jwt = jwt.encode(data, JWT_SECRET, algorithm=ALGORITHMS)
    return encoded_jwt


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str) -> dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    # Use JWT_SECRET and ALGORITHMS from your settings
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHMS[0])
    return token_response(token)


def verify_token(token):
    decoded_token = VerifyToken(token).verify()
    if decoded_token.get("status"):
        return HttpResponse(status=401)  # Unauthorized
    return decoded_token
