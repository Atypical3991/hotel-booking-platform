from datetime import datetime, timedelta

import jwt
from django.conf import settings


def generate_jwt_token(user_id, role):
    """
    Generate a JWT token for authentication.
    """
    # Set the expiration time for the token (e.g., 1 day from now)
    expiration_time = datetime.utcnow() + timedelta(days=1)

    # Define the payload for the token
    payload = {
        'user_id': user_id,
        'exp': expiration_time,
        'role': role
    }

    # Generate the JWT token
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token  # Decode from bytes to string for easier use


def decode_jwt_token(token):
    """
    Decode a JWT token to retrieve the payload.
    """
    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Handle the case where the token has expired
        print('Token has expired')
        return None
    except jwt.InvalidTokenError:
        # Handle other invalid token scenarios
        print('Invalid token')
        return None
