# coding: utf-8
import time
from django.conf import settings
from cent.core import generate_token


def get_connection_parameters(user, user_info=None):
    timestamp = str(int(time.time()))
    user_pk = str(user.pk) if user.is_authenticated() else ""
    token = generate_token(
        settings.CENTRIFUGE_PROJECT_SECRET,
        settings.CENTRIFUGE_PROJECT_ID,
        user_pk,
        timestamp,
        user_info=user_info
    )
    return {
        'sockjs_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection',
        'ws_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection/websocket',
        'user': user_pk,
        'project': settings.CENTRIFUGE_PROJECT_ID,
        'timestamp': timestamp,
        'token': token,
        'user_info': user_info
    }
