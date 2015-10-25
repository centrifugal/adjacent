from adjacent import get_connection_parameters


def main(request):

    params = get_connection_parameters(request.user)

    return dict(
        CENTRIFUGE_SOCKJS_ENDPOINT=params['sockjs_endpoint'],
        CENTRIFUGE_WS_ENDPOINT=params['ws_endpoint'],
        CENTRIFUGE_USER=params['user'],
        CENTRIFUGE_TIMESTAMP=params['timestamp'],
        CENTRIFUGE_TOKEN=params['token'],
        CENTRIFUGE_INFO=params['info']
    )
