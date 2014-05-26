# coding: utf-8
import time
from django.conf import settings
from cent.core import generate_token


def get_connection_parameters(user, user_info=None, websocket=False):
    timestamp = str(int(time.time()))
    user_pk = str(user.pk) if user.is_authenticated() else ""
    token = generate_token(
        settings.CENTRIFUGE_PROJECT_SECRET,
        settings.CENTRIFUGE_PROJECT_ID,
        user_pk,
        timestamp,
        user_info=user_info
    )
    connection_path = '/connection' if not websocket else '/connection/websocket'
    return {
        'url': settings.CENTRIFUGE_ADDRESS + connection_path,
        'user': user_pk,
        'project': settings.CENTRIFUGE_PROJECT_ID,
        'timestamp': timestamp,
        'token': token
    }
