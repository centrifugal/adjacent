# coding: utf-8
import time
from django.conf import settings
from cent.core import generate_token


# In django.VERSION >= (1, 10) user.is_authenticated is not callable anymore
def is_authenticated(user):
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated


def get_connection_parameters(user, info=''):
    timestamp = str(int(time.time()))
    user_pk = str(user.pk) if is_authenticated(user) else ""
    token = generate_token(
        settings.CENTRIFUGE_SECRET,
        user_pk,
        timestamp,
        info=info
    )
    return {
        'sockjs_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection',
        'ws_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection/websocket',
        'user': user_pk,
        'timestamp': timestamp,
        'token': token,
        'info': info
    }
