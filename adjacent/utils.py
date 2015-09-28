# coding: utf-8
import time
from django.conf import settings
from cent.core import generate_token


def get_connection_parameters(user, info=''):
    timestamp = str(int(time.time()))
    user_pk = str(user.pk) if user.is_authenticated() else ""
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
